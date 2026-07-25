"""
RSU Campus Buddy — Flask Backend (Single File)
===================================================
3-file project: app.py | frontend.html | database.json

Run:
  pip install flask flask-cors requests
  set VISION_API_KEY=your_google_vision_key   (Windows)
  export VISION_API_KEY=your_google_vision_key (Mac/Linux)
  python app.py

The app serves frontend.html at http://localhost:5000
"""

import os
import json
import math
import heapq
import re
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app  = Flask(__name__)
CORS(app)

# ── Paths ────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DB_PATH   = os.path.join(BASE_DIR, "database.json")
FRONT_DIR = BASE_DIR   # frontend.html lives next to app.py

# ── Load database ────────────────────────────────────────────────
def load_db():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

DB = load_db()

# ── Google Cloud Vision (optional) ──────────────────────────────
VISION_KEY = os.environ.get("VISION_API_KEY", "")
VISION_URL = f"https://vision.googleapis.com/v1/images:annotate?key={VISION_KEY}"

# ════════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ════════════════════════════════════════════════════════════════

def strip_keywords(b: dict) -> dict:
    """Remove internal keyword list before sending to client."""
    return {k: v for k, v in b.items() if k != "keywords"}


def match_building_from_labels(labels: list) -> dict | None:
    """
    Match Vision API or Teachable Machine labels
    against each building's keyword list.
    Returns { buildingID, confidence, matchedLabels } or None.
    """
    detected = [l.lower() for l in labels]
    scores, hit_map = {}, {}
    for bid, b in DB["buildings"].items():
        kws  = [k.lower() for k in b.get("keywords", [])]
        hits = [d for d in detected if any(kw in d or d in kw for kw in kws)]
        scores[bid] = len(hits)
        hit_map[bid] = hits

    if not scores:
        return None
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return None

    conf = "High" if scores[best] >= 4 else "Medium" if scores[best] >= 2 else "Low"
    return {"buildingID": best, "confidence": conf, "matchedLabels": hit_map[best]}


def keyword_text_search(text: str) -> dict | None:
    """Simple keyword match for text chat queries."""
    t = text.lower()
    for bid, b in DB["buildings"].items():
        kws = b.get("keywords", [])
        if any(kw in t for kw in kws):
            return b
    return None


def normalize_tm_label(value: str) -> str:
    """Normalize Teachable Machine labels for tolerant matching."""
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def resolve_tm_building_id(label: str, label_map: dict) -> str | None:
    """
    Resolve a Teachable Machine class label to a building ID.
    Supports exact mappings, normalized mappings, direct building IDs,
    and common name/number variants like "B11" or "Building 11".
    """
    if not label:
        return None

    if label in label_map:
        return label_map[label]

    normalized_label = normalize_tm_label(label)
    normalized_map = {
        normalize_tm_label(map_label): building_id
        for map_label, building_id in label_map.items()
        if not str(map_label).startswith("_")
    }
    if normalized_label in normalized_map:
        return normalized_map[normalized_label]

    for bid, building in DB["buildings"].items():
        candidates = {
            bid,
            building.get("id", ""),
            building.get("number", ""),
            building.get("shortName", ""),
            building.get("name", ""),
            f"building {building.get('number', '')}",
            f"b{building.get('number', '')}",
        }
        normalized_candidates = {normalize_tm_label(c) for c in candidates if c}
        if normalized_label in normalized_candidates:
            return bid

    return None


# ════════════════════════════════════════════════════════════════
#  ROUTING / PATHFINDING (Dijkstra)
# ════════════════════════════════════════════════════════════════

def dijkstra(start_id: str, end_id: str) -> dict:
    """
    Run Dijkstra's algorithm on the navigation graph
    stored in database.json under navigation.nodes and .edges.

    Returns:
      { path: [nodeID, ...], totalWeight: int, steps: [...] }
    """
    nodes = {n["id"]: n for n in DB["navigation"]["nodes"]}
    edges = DB["navigation"]["edges"]

    # Build adjacency list (undirected)
    adj = {nid: [] for nid in nodes}
    for e in edges:
        adj[e["from"]].append((e["to"],   e["weight"], e))
        adj[e["to"]].append(  (e["from"], e["weight"], e))

    # Priority queue: (cost, nodeID, path)
    heap = [(0, start_id, [start_id])]
    visited = set()

    while heap:
        cost, nid, path = heapq.heappop(heap)
        if nid in visited:
            continue
        visited.add(nid)
        if nid == end_id:
            return _build_path_result(path, cost, nodes, edges)
        for nb, w, _ in adj.get(nid, []):
            if nb not in visited:
                heapq.heappush(heap, (cost + w, nb, path + [nb]))

    return {"path": [], "totalWeight": 0, "steps": [], "error": "No path found"}


def _build_path_result(path: list, total: int, nodes: dict, edges: list) -> dict:
    """Convert raw node path to human-readable steps."""
    steps = []
    edge_map = {}
    for e in edges:
        edge_map[(e["from"], e["to"])] = e
        edge_map[(e["to"], e["from"])] = e

    for i, nid in enumerate(path):
        node = nodes[nid]
        if i == 0:
            steps.append({"step": 1, "instruction": f"Start at <strong>{node['label']}</strong>",
                          "type": "start", "node": nid})
        elif i == len(path) - 1:
            steps.append({"step": i + 1, "instruction": f"Arrive at <strong>{node['label']}</strong>",
                          "type": "end", "node": nid})
        else:
            e = edge_map.get((path[i-1], nid), {})
            etype = e.get("type","walk")
            if etype == "lift":
                b   = nodes[nid].get("building","")
                fl  = nodes[nid].get("floor", "?")
                steps.append({"step": i + 1,
                    "instruction": f"Take the <strong>lift</strong> in {b} to <strong>Floor {fl}</strong>",
                    "type": "lift", "node": nid})
            elif etype == "outdoor":
                steps.append({"step": i + 1,
                    "instruction": f"Walk to <strong>{node['label']}</strong>",
                    "type": "walk", "node": nid})
            else:
                steps.append({"step": i + 1,
                    "instruction": f"Go to <strong>{node['label']}</strong>",
                    "type": "indoor", "node": nid})

    mins = max(1, round(total / 80))  # ~80m per minute walking
    return {
        "path": path,
        "totalWeight": total,
        "estimatedMinutes": mins,
        "steps": steps,
        "nodeDetails": [nodes[n] for n in path]
    }


def find_node_for_room(room_id: str) -> str | None:
    """Find the navigation node ID that corresponds to a room ID."""
    for n in DB["navigation"]["nodes"]:
        if n.get("roomID") == room_id:
            return n["id"]
    return None


def find_entry_node(building_id: str) -> str | None:
    """Find the entrance node for a building."""
    for n in DB["navigation"]["nodes"]:
        if n.get("building") == building_id and n.get("type") == "entrance":
            return n["id"]
    return None


# ════════════════════════════════════════════════════════════════
#  ROUTES — Serve Files
# ════════════════════════════════════════════════════════════════

@app.route("/")
def index():
    return send_from_directory(FRONT_DIR, "frontend.html")


# ════════════════════════════════════════════════════════════════
#  ROUTES — Campus Data
# ════════════════════════════════════════════════════════════════

@app.route("/api/campus", methods=["GET"])
def api_all_campus():
    """Return all campus data (buildings stripped of keywords)."""
    return jsonify({
        "success":   True,
        "campus":    DB["campus"],
        "buildings": [strip_keywords(b) for b in DB["buildings"].values()],
    })


@app.route("/api/bootstrap", methods=["GET"])
def api_bootstrap():
    """Return all frontend bootstrap data from the backend in one payload."""
    return jsonify({
        "success": True,
        "campus": DB["campus"],
        "buildings": [strip_keywords(b) for b in DB["buildings"].values()],
        "navigation": DB["navigation"],
        "teachable_machine": DB.get("teachable_machine", {}),
    })


@app.route("/api/campus/<bid>", methods=["GET"])
def api_one_building(bid):
    b = DB["buildings"].get(bid.upper())
    if not b:
        return jsonify({"success": False, "error": f"Building '{bid}' not found"}), 404
    return jsonify({"success": True, "building": strip_keywords(b)})


# ════════════════════════════════════════════════════════════════
#  ROUTES — Image Recognition
# ════════════════════════════════════════════════════════════════

@app.route("/api/recognize", methods=["POST"])
def api_recognize():
    """
    Accepts a base64 image.
    If VISION_API_KEY is set → uses Google Cloud Vision.
    Otherwise → returns a prompt for Teachable Machine (client-side).

    Body: { "image": "<base64>", "mimeType": "image/jpeg",
            "teachable_labels": [{"label":"...", "confidence":0.9}, ...] }
    """
    try:
        body    = request.get_json(force=True)
        img_b64 = body.get("image")
        tm_labels = body.get("teachable_labels")  # from Teachable Machine (client-side)

        if not img_b64 and not tm_labels:
            return jsonify({"success": False, "error": "No image or labels provided"}), 400

        labels = []

        # ── Path 1: Teachable Machine labels sent from frontend ──
        if tm_labels:
            tm_cfg = DB.get("teachable_machine", {})
            label_map = tm_cfg.get("labels", {})
            threshold = tm_cfg.get("confidence_threshold", 0.75)
            building_scores = {}
            building_labels = {}
            for item in tm_labels:
                conf = item.get("confidence", 0)
                mapped_bid = resolve_tm_building_id(item.get("label"), label_map)
                if not mapped_bid:
                    continue
                building_scores[mapped_bid] = building_scores.get(mapped_bid, 0) + conf
                building_labels.setdefault(mapped_bid, []).append(
                    f"{item.get('label')} ({int(conf * 100)}%)"
                )

            if building_scores:
                best_bid = max(building_scores, key=building_scores.get)
                combined_conf = building_scores[best_bid]
                b = DB["buildings"].get(best_bid)
                if b and combined_conf >= max(threshold, 0.5):
                    return jsonify({"success": True, "result": {
                        "type":          "recognized",
                        "buildingID":    best_bid,
                        "confidence":    "High" if combined_conf >= 0.9 else "Medium" if combined_conf >= 0.75 else "Low",
                        "matchedLabels": building_labels.get(best_bid, []),
                        "reasoning":     f"Teachable Machine combined confidence for {best_bid}: {int(combined_conf*100)}%",
                        "building":      strip_keywords(b),
                    }})
            # No confident match from TM
            return jsonify({"success": True, "result": {
                "type": "unrecognized",
                "detectedLabels": [f"{i['label']} ({int(i.get('confidence', 0) * 100)}%)" for i in tm_labels],
                "message": "The model predicted labels, but none reached the configured confidence threshold."
            }})

        # ── Path 2: Google Cloud Vision ──────────────────────────
        if not VISION_KEY or VISION_KEY == "":
            return jsonify({"success": False,
                "error": "No VISION_API_KEY set and no Teachable Machine labels provided. "
                         "Set VISION_API_KEY or enable Teachable Machine in database.json"}), 400

        payload = {"requests": [{"image": {"content": img_b64},
            "features": [
                {"type": "LABEL_DETECTION",     "maxResults": 25},
                {"type": "LANDMARK_DETECTION",  "maxResults": 5},
                {"type": "OBJECT_LOCALIZATION", "maxResults": 15},
            ]}]}
        resp = requests.post(VISION_URL, json=payload, timeout=12)
        resp.raise_for_status()
        res = resp.json().get("responses", [{}])[0]

        label_set = set()
        for item in res.get("labelAnnotations", []):         label_set.add(item["description"].lower())
        for item in res.get("localizedObjectAnnotations",[]): label_set.add(item["name"].lower())
        for item in res.get("landmarkAnnotations", []):      label_set.add(item["description"].lower())
        labels = list(label_set)

        match = match_building_from_labels(labels)
        if not match:
            return jsonify({"success": True, "result": {
                "type": "unrecognized",
                "detectedLabels": labels[:14],
                "message": ("Couldn't match this image to a known RSU building. "
                            "Try a clearer photo of any campus building.")
            }})

        b = DB["buildings"][match["buildingID"]]
        return jsonify({"success": True, "result": {
            "type":          "recognized",
            "buildingID":    match["buildingID"],
            "confidence":    match["confidence"],
            "matchedLabels": match["matchedLabels"],
            "reasoning":     f"Google Vision detected: {', '.join(match['matchedLabels'][:5])}",
            "building":      strip_keywords(b),
        }})

    except requests.exceptions.HTTPError as e:
        code = e.response.status_code if e.response else 500
        try:    msg = e.response.json()["error"]["message"]
        except: msg = str(e)
        return jsonify({"success": False, "error": f"Vision API ({code}): {msg}"}), 502
    except requests.exceptions.Timeout:
        return jsonify({"success": False, "error": "Vision API timed out"}), 504
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# ════════════════════════════════════════════════════════════════
#  ROUTES — Text Chat
# ════════════════════════════════════════════════════════════════

@app.route("/api/chat", methods=["POST"])
def api_chat():
    msg = request.get_json(force=True).get("message", "")
    t   = msg.lower()

    # Club search
    if "club" in t or "activit" in t:
        lines = []
        for b in DB["buildings"].values():
            for c in b.get("clubs", []):
                lines.append(f"🎓 {c['name']} — {b['shortName']} ({c['schedule']})")
        return jsonify({"success": True, "result": {"type": "text",
            "content": "🎓 <strong>Student Clubs at RSU:</strong><br><br>" + "<br>".join(lines)}})

    # Dining search
    food_terms = ["eat", "food", "dining", "canteen", "cafeteria", "restaurant", "coffee", "drink", "lunch", "meal"]
    if any(term in t for term in food_terms):
        dining_buildings = []
        for b in DB["buildings"].values():
            haystack = " ".join([
                b.get("category", ""),
                b.get("description", ""),
                " ".join(b.get("keywords", [])),
                " ".join(b.get("services", [])),
                " ".join(b.get("facilities", [])),
            ]).lower()
            if "dining" in b.get("category", "").lower() or any(term in haystack for term in food_terms):
                dining_buildings.append(f"{b['emoji']} <strong>{b['name']}</strong> — {b['location']}")
        return jsonify({"success": True, "result": {"type": "text",
            "content": "🍽️ <strong>Places to eat at RSU:</strong><br><br>" + "<br>".join(dining_buildings)}})

    # All buildings list
    if any(phrase in t for phrase in ["show all rsu building", "show all rsu buildings", "list all buildings", "all buildings", "campus buildings"]):
        lines = [f"{b['emoji']} <strong>{b['name']}</strong> — {b['category']}"
                 for b in DB["buildings"].values()]
        return jsonify({"success": True, "result": {"type": "text",
            "content": "📍 <strong>RSU Campus Buildings:</strong><br><br>" + "<br>".join(lines)}})

    # Keyword match to a specific building
    b = keyword_text_search(msg)
    if b:
        return jsonify({"success": True, "result": {"type": "building", "building": strip_keywords(b)}})

    return jsonify({"success": True, "result": {"type": "text",
        "content": "👋 Ask me about any RSU building, service, or club — or upload a campus photo for AI recognition!"}})


# ════════════════════════════════════════════════════════════════
#  ROUTES — Navigation / Routing
# ════════════════════════════════════════════════════════════════

@app.route("/api/navigate", methods=["POST"])
def api_navigate():
    """
    Compute shortest path between two points.
    Body: {
      "from_node": "N_B6_1_CAN",    ← direct node ID, OR
      "from_building": "B6",         ← building entrance, OR
      "from_room": "B6-1-01",        ← specific room

      "to_node": "N_B11_5_TT",      ← direct node ID, OR
      "to_building": "B11",          ← building entrance, OR
      "to_room": "B11-5-01"          ← specific room (e.g. Table Tennis)
    }
    """
    try:
        body = request.get_json(force=True)

        # Resolve FROM node
        start = (body.get("from_node") or
                 find_node_for_room(body.get("from_room","")) or
                 find_entry_node(body.get("from_building","")))

        # Resolve TO node
        end   = (body.get("to_node") or
                 find_node_for_room(body.get("to_room","")) or
                 find_entry_node(body.get("to_building","")))

        if not start:
            return jsonify({"success": False, "error": "Could not find start location"}), 400
        if not end:
            return jsonify({"success": False, "error": "Could not find destination"}), 400
        if start == end:
            return jsonify({"success": True, "result": {"steps": [
                {"step":1,"instruction":"You are already at your destination! 🎯","type":"end"}
            ], "totalWeight": 0, "estimatedMinutes": 0, "path": [start]}})

        result = dijkstra(start, end)
        if result.get("error"):
            return jsonify({"success": False, "error": result["error"]}), 404

        return jsonify({"success": True, "result": result})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/navigate/nodes", methods=["GET"])
def api_nav_nodes():
    """Return all navigation nodes (for map rendering)."""
    return jsonify({"success": True, "nodes": DB["navigation"]["nodes"],
                    "edges": DB["navigation"]["edges"]})


# ════════════════════════════════════════════════════════════════
#  ROUTES — Admin
# ════════════════════════════════════════════════════════════════

@app.route("/api/admin/building", methods=["POST"])
def api_admin_building():
    """Add or update a building. Header: X-Admin-Secret: rsu-admin-2025"""
    if request.headers.get("X-Admin-Secret") != "rsu-admin-2025":
        return jsonify({"success": False, "error": "Unauthorised"}), 401
    body = request.get_json(force=True)
    bid  = body.get("buildingID","").upper()
    data = body.get("data")
    if not bid or not data:
        return jsonify({"success": False, "error": "buildingID and data required"}), 400
    DB["buildings"][bid] = data
    return jsonify({"success": True, "message": f"Building '{bid}' saved."})


@app.route("/api/admin/reload", methods=["POST"])
def api_admin_reload():
    """Reload database.json from disk without restarting."""
    global DB
    DB = load_db()
    return jsonify({"success": True, "message": "Database reloaded."})


# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    key_ok = bool(VISION_KEY)
    tm_ok  = DB.get("teachable_machine", {}).get("enabled", False)
    print("=" * 58)
    print("  RSU Campus Buddy  —  Flask Backend")
    print("=" * 58)
    print(f"  Google Vision API : {'SET ✅' if key_ok else 'NOT SET (use Teachable Machine or set VISION_API_KEY)'}")
    print(f"  Teachable Machine : {'ENABLED ✅' if tm_ok else 'DISABLED (edit database.json to enable)'}")
    print(f"  Buildings loaded  : {len(DB['buildings'])}")
    print(f"  Nav nodes         : {len(DB['navigation']['nodes'])}")
    print(f"  Frontend          : http://localhost:5000")
    print("=" * 58)
    app.run(debug=True, port=5000)
