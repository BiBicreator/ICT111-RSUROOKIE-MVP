# Startup / Product Metrics

> Define metrics that measure how users interact with the RSU Campus Buddy prototype and evaluate the effectiveness of the AI-powered campus navigation system.

## 1. Metrics Summary

| Metric ID | Metric Name | Metric Type | Why This Metric Matters | Formula / How to Calculate | Data Source | Prototype Screen |
|---|---|---|---|---|---|---|
| M-01 | Total Campus Buildings | Usage | Shows how many campus buildings are available for users to explore. | Count all building records | `database.json` | Directory / Dashboard |
| M-02 | AI Image Recognition Requests | Usage | Measures how frequently users use the AI image recognition feature. | Count uploaded images processed by the system | `app.py` | AI Chat |
| M-03 | Building Recognition Accuracy | Performance | Evaluates how accurately Google Teachable Machine identifies campus buildings. | Correct recognitions ÷ Total recognitions × 100 | Prototype testing results | AI Chat |
| M-04 | Directory Search Success Rate | Validation | Measures whether users can successfully find campus buildings using the search feature. | Successful searches ÷ Total searches × 100 | `frontend.html` search results | Directory |
| M-05 | Admin Building Updates | Operational | Tracks how often administrators update campus building information. | Count successful admin updates | `admin.html` / `database.json` | Admin Panel |
| M-06 | Average User Feedback Score | Validation | Measures overall user satisfaction with the prototype. | Average feedback score (1–5) | User validation results | Dashboard |

---

## 2. Metrics Interpretation

These metrics help evaluate both the usability and technical performance of the RSU Campus Buddy prototype. The total number of campus buildings indicates whether the directory provides comprehensive campus information. Tracking AI image recognition requests shows how actively users use the chatbot's image recognition feature. Building recognition accuracy helps the team evaluate the effectiveness of the Google Teachable Machine model and identify when additional training images are needed. The directory search success rate measures whether students can quickly locate campus buildings and related information. Monitoring admin building updates ensures that campus information remains accurate and up to date. Finally, the average user feedback score provides evidence of user satisfaction and highlights areas for future improvements before the final prototype.

---

## 3. Link to Final Prototype

These metrics will be presented on the **Dashboard** page of the final prototype. The dashboard will display:

- Total campus buildings in the database.
- Total AI image recognition requests.
- Building recognition accuracy.
- Directory search success rate.
- Number of administrator updates.
- Average user feedback score.

These metrics will help administrators monitor system performance while providing the development team with meaningful insights for improving the AI recognition model, campus directory, and overall user experience.
