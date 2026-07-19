# Lab 08 - Analytics Insights

## 1. Analytics Question

What did users do, say, and prove when testing the MVP direction?

The validation tested whether users could successfully use the main features of RSU Campus Buddy, including AI building recognition, building searchs, chatbot assistance, viewing campus information, and admin management. The collected data shows how effectively users completed these tasks and identifies areas that require improvement.

---

## 2. Metrics Calculated

| Metric | Formula / Method | Result |
|---|---|---:|
| Total test users | Count testers | **12** |
| Completed tasks | Count `Task_Completed = Yes` | **11** |
| Task success rate | Completed tasks ÷ Total testers | **91.7%** |
| Average feedback score | Average of feedback scores (1–5) | **4.3 / 5** |
| Average interest level | Average of interest scores (1–5) | **4.6 / 5** |
| Confusion points | Count repeated confusion categories | **AI image recognition, search function, chatbot responses** |

---

## 3. Findings

1. **Most users successfully completed their assigned tasks.** Eleven out of twelve participants completed the required tasks, resulting in a **91.7% task success rate**, indicating that the prototype supports the primary user workflow.

2. **Users valued the AI building recognition and campus information features.** Most participants rated these features highly and considered them useful for locating campus buildings and services.

3. **Users identified several areas for improvement.** The most common feedback involved improving AI recognition accuracy for unclear images, expanding chatbot responses, and making the search function support abbreviations and partial keywords.

---

## 4. Interpretation

The validation results indicate that the current MVP is effective in helping students access campus information through AI image recognition and the chatbot. Overall user satisfaction and interest were high, showing that the project addresses a genuine user need. However, improvements to AI accuracy, search functionality, and chatbot knowledge are necessary to enhance usability before the final prototype is completed.

---

## 5. Requirements Affected

| Requirement ID | Evidence | Action Needed |
|---|---|---|
| FR-02 | Some uploaded images were not recognized successfully. | Retrain Google Teachable Machine using additional building images. |
| FR-03 | Chatbot could not answer some campus-related questions. | Expand chatbot keywords and response database. |
| FR-06 | Users wanted more flexible search options. | Support abbreviations and partial keyword matching. |
| FR-08 | Recognition errors occurred with low-quality images. | Improve error handling and user feedbacks messages. |
| FR-09 | Admin users requested a more organized management interface. | Improve the admin page layout and editing workflow. |

---

## 6. Next Prototype Improvement

- Improve AI building recognition accuracy by adding more training images.
- Expand chatbot knowledge to answer more campus-related questions.
- Improve the building search feature with abbreviation and partial keyword support.
- Enhance the admin interface for easier data management.
- Improve feedback messages when AI recognition fails or user input is invalid.
- Continue usability testing after implementing these improvements.
