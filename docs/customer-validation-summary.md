# Lab 08 - Customer Validation Summary

## 1. Project Title

**RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)**

---

## 2. Prototype Tested

The team tested the first MVP version of **RSU Campus Buddy**, a web-based campus assistant that uses Google Teachable Machine to recognize campus buildings and provides building information through a chatbot interface.

- **Prototype version:** v0.1
- **Prototype link or screenshot location:** `/prototype/` and `/screenshots/validation-test-screens.png`
- **Main tasks tested:**
  - Upload a building image for AI recognition
  - Search for a campus building
  - Ask the chatbot about campus services
  - View building information
  - Admin updates campus information
- **Related requirements from `system-requirements.md`:**
  - FR-01
  - FR-02
  - FR-03
  - FR-04
  - FR-05
  - FR-06
  - FR-07
  - FR-08
  - FR-09
  - FR-10
  - FR-11
  - FR-12

---

## 3. Test Users

| Test User ID | User Role | Why this user is relevant |
|---|---|---|
| TU-01 | Student | Primary target user who needs campus information |
| TU-02 | Student | Represents new students searching for buildings |
| TU-03 | Student | Tested chatbot functionality |
| TU-04 | Student | Tested building information features |
| TU-05 | Student | Tested AI image recognition |
| TU-06 | International Student | Represents international students unfamiliar with campus |
| TU-07 | Student | Tested floor plan and facilities |
| TU-08 | Student | Tested chatbot navigation |
| TU-09 | Admin | Tested campus information management |
| TU-10 | Admin | Tested adding and updating building records |
| TU-11 | Student | Tested validation and error messages |
| TU-12 | Student | Tested browsing campus information |

---

## 4. Validation Method

**Testing method:**
- Individual usability testing using the working prototype.

**Date/time:**
- (15.07.2026)

**Location or online platform:**
- Rangsit University / Inperson demonstration

**Number of testers:**
- 12

**Data collected:**
- Task completion
- Completion time
- Feedback score
- Interest level
- Confusion points
- User comments

---

## 5. Summary of Results

| Metric | Result | Interpretation |
|---|---:|---|
| Total test users | 12 | Validation involved both students and administrators. |
| Task success rate | 91.7% (11/12) | Most users completed their assigned tasks successfully. |
| Average feedback score | 4.3 / 5 | Users were generally satisfied with the prototype. |
| Average interest level | 4.5 / 5 | Users showed strong interest in using the system. |
| Most common confusion point | AI image recognition and search keywords | Some users experienced recognition errors with unclear images and expected more flexible search terms. |

---

## 6. Key User Comments

### Positive Feedback

- AI building recognition makes campus navigation easier.
- Building information is clear and helpful.
- The chatbot provides useful campus information.
- The interface is easy to understand.

### Suggested Improvements

- Improve AI recognition accuracy using more training images.
- Expand chatbot responses to answer more campus-related questions.
- Support abbreviations and partial building names in search.
- Improve the admin interface layout.

---

## 7. Affected Requirements

| Requirement ID | Evidence Found | Required Prototype Improvement |
|---|---|---|
| FR-02 | Some uploaded images were not recognized correctly. | Retrain the AI model using more building images. |
| FR-03 | Chatbot could not answer some questions. | Expand chatbot knowledge and keywords. |
| FR-06 | Users expected more flexible search options. | Support abbreviations and partial keyword search. |
| FR-08 | Recognition failed for low-quality images. | Improve error handling and provide clearer feedback messages. |
| FR-09 | Admin interface could be more user-friendly. | Improve the admin page layout and editing workflow. |

---

## 8. Conclusion

The current MVP is **validated**. Most participants successfully completed the main tasks and gave positive feedback about the AI building recognition, chatbot, and campus information features. User testing also identified several improvements, particularly in AI recognition accuracy, chatbot responses, search functionality, and the admin interface. These findings will guide the next iteration of the prototype before the final project submission.
