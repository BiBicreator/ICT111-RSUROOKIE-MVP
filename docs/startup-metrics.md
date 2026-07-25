# Startup / Product Metrics

> Define metrics that show useful product activity. Metrics should help the team understand system usage, AI performance, user engagement, and prototype effectiveness.

## 1. Metrics Summary

| Metric ID | Metric Name | Metric Type | Why This Metric Matters | Formula / How to Calculate | Data Source | Prototype Screen |
|---|---|---|---|---|---|---|
| M-01 | Total Building Records | Usage | Shows the number of campus buildings available in the system | Count all building records | `buildings.json` | Dashboard |
| M-02 | Total AI Recognitions | Usage | Measures how often users use the image recognition feature | Count successful image recognition requests | Recognition logs / simulated data | Dashboard |
| M-03 | Recognition Accuracy | Performance | Measures the accuracy of Google Teachable Machine predictions | Correct recognitions ÷ Total recognitions × 100 | Prototype testing results | Dashboard |
| M-04 | Most Viewed Building | User Activity | Identifies the campus building viewed most frequently | Count detail page visits for each building | Directory usage data | Dashboard |
| M-05 | Directory Search Success Rate | Validation | Measures whether users can successfully find a building | Successful searches ÷ Total searches × 100 | Search history / testing results | Dashboard |
| M-06 | Average User Feedback Score | Validation | Measures user satisfaction with the prototype | Average of feedback scores (1–5) | Validation results | Dashboard |

---

## 2. Metrics Interpretation

The startup metrics help evaluate both the usability and performance of the RSU Campus Buddy prototype. Tracking the total number of building records ensures that the campus directory provides sufficient information for users. Monitoring AI recognitions and recognition accuracy helps determine how well the Google Teachable Machine model identifies campus buildings and highlights areas where additional training images may be needed. The most viewed building metric indicates which locations students access most frequently, allowing the team to prioritize improvements for those pages. Measuring the directory search success rate shows whether students can quickly find the information they need. Finally, the average user feedback score reflects overall user satisfaction and provides evidence for future prototype improvements.

---

## 3. Link to Final Prototype

These metrics will be displayed on the **Dashboard** page of the final prototype. The dashboard will summarize:
- Total campus buildings available
- Total AI image recognitions
- AI recognition accuracy
- Most viewed building
- Directory search success rate
- Average user feedback score

These metrics will help administrators monitor system usage, evaluate AI performance, and identify opportunities to improve the campus navigation experience.
