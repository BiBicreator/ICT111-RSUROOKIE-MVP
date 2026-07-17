# Lab 08 - MVP Decision

## 1. Decision

- [x] Continue with the current MVP direction
- [x] Continue with minor revisions
- [x] Revise major workflow or feature
- [x] Collect more evidence before implementation
- [ ] Pivot or change the solution direction

---

## 2. Evidence Supporting the Decision

The MVP was tested by **12 participants**, including students, international students, and administrators.

The validation results showed:

- **11 out of 12 users (91.7%)** successfully completed their assigned tasks.
- The average feedback score was **4.3/5**.
- The average interest level was **4.6/5**.
- Users found the AI building recognition, campus information, and chatbot features useful.
- Most improvement suggestions focused on AI recognition accuracy, chatbot responses, and search functionality rather than changing the overall project direction.

These results indicate that the MVP solves a real user problem and only requires minor improvements before final implementation.

---

## 3. Requirements to Keep

| Requirement ID | Reason |
|---|---|
| FR-01 | Homepage clearly introduces the project and guides users to the main features. |
| FR-04 | JSON data storage successfully provides campus information. |
| FR-05 | Building information is useful and easy to understand. |
| FR-07 | Building detail pages provide relevant information for users. |
| FR-10 | Input validation prevents invalid image uploads and incomplete inputs. |
| FR-11 | Confirmation and error messages help users understand system responses. |
| FR-12 | Campus information summary provides a useful overview of available buildings and services. |

---

## 4. Requirements to Improve

| Requirement ID | Problem Found | Improvement Needed |
|---|---|---|
| FR-02 | AI recognition failed for some unclear building images. | Collect more training images and retrain the Google Teachable Machine model. |
| FR-03 | Chatbot could not answer some campus-related questions. | Expand chatbot keywords and response database. |
| FR-06 | Search function does not support abbreviations or partial building names. | Improve search functionality with keyword matching and abbreviations. |
| FR-08 | Recognition failure messages could be clearer. | Improve error handling and provide more helpful feedback. |
| FR-09 | Admin interface can be more user-friendly. | Improve page layout and simplify data management. |

---

## 5. Prototype Changes Before Next Lab

- Improve AI building recognition by training the model with additional campus images.
- Expand chatbot responses to cover more campus-related questions.
- Improve the search function by supporting abbreviations and partial keywords.
- Improve the admin interface for easier building information management.
- Refine feedback and error messages to improve the user experience.
- Conduct another round of usability testing after implementing the improvements.

---

## 6. GitHub Issues Created

| Issue Title | Assigned Member | Requirement ID |
|---|---|---|
| Collect or Clean Validation Data for RSU Campus Buddy | Min Khant Zaw| FR-01–FR-12 |
| Complete validation-results.xlsx | Khin Zu Zu Oo | FR-01–FR-12 |
| Write Customer Validation Summary | Khin Zu Zu Oo | FR-01–FR-12 |
| Write Analytics Insights | Khin Zu Zu Oo | FR-01–FR-12 |
| Write MVP Decision | Khin Zu Zu Oo | FR-01–FR-12 |
| Improve Prototype Based on Validation Evidence |Khin Zu Zu Oo | FR-02, FR-03, FR-06, FR-08, FR-09 |
| Update README and Weekly Logbook for Lab 08 | Khin Zu Zu Oo | Documentation |
