#  RSU Campus Buddy ( Smart Campus Chatbot With Image) 


> 4 tabs: **Chat** · **Uni Map** · **Directory**,**Admin**  
> Image recognition via **Google Cloud Vision API**,**Teachable Machine**

---

##  Folder Structure

```
smart_campus_chatbot/
│   └── index.html          ← Complete multi-tab app (no build tools)
│   ├── app.py              ← Flask REST API + campus database
│   ├── admin.py            ← Admin Management
│   └── requirements.txt    ← Python dependencies
└── README.md
```

---

##  App Tabs

| Tab | Description |
|-----|-------------|
|  **Chat** | AI chatbot — text questions OR upload a photo → Google Vision identifies the building |
|  **Uni Map** | Interactive SVG campus map with all buildings. Click any building → opens in Directory |
| **Directory** | Full building directory with search, filters, expandable info, and Get Direction buttons |
| **Admin** | Secure admin panel for maintaining campus data. Add, edit, or delete building information, update facilities and maps, and manage the chatbot's building database. |

---


##  Step 1 — Create Your Own Google Cloud Vision API Key

> **Note:** For security reasons, our project does **not** include or share our Google Cloud Vision API key. Please create your **own free API key** by following the steps below.

1. Go to **https://console.cloud.google.com**
2. Create a new project (or select an existing one).
3. Enable **Cloud Vision API**:
   - Go to **APIs & Services → Library**
   - Search for **Cloud Vision API**
   - Click **Enable**
4. Go to **APIs & Services → Credentials**.
5. Click **Create Credentials → API Key**.
6. Copy your API key and replace the placeholder in the project configuration:

```javascript
const API_KEY = "YOUR_API_KEY_HERE";
```

---

##  Step 2 — Run the Backend

```bash
cd backend

# Install
pip install -r requirements.txt

# Set API key
export GOOGLE_VISION_API_KEY=your_key_here   # Mac/Linux
set GOOGLE_VISION_API_KEY=your_key_here      # Windows

# Start server
python app.py
```
Server: **http://localhost:5000**

---

##  Step 3 — Open Frontend

Open `frontend/index.html` in any browser. No build step needed.

>  Note: If the backend is offline, the app still works using its built-in fallback campus data. Only image recognition and live text chat require the backend.

---

##  Troubleshooting

| Problem | Solution |
|---------|----------|
| API Key NOT SET | `export GOOGLE_VISION_API_KEY=your_key` |
| CORS error | Make sure Flask is running on port 5000 |
| Vision API 403 | Check key is valid & Vision API is enabled |
| Image not recognized | Use clear, well-lit photo of a single building |
| Directory shows fallback | Backend offline — still works with local data |

