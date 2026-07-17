# MVP Experiment Plan

## 1. Group and Project Information

- **Group name:** RSUROOKIE
- **Project title:** RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)
- **Repository link:** (https://github.com/BiBicreator/ICT111-RSUROOKIE-MVP.git)
- **Main target user:** RSU students, especially freshmen and international students
- **Prototype platform:** Flask (Python), HTML/CSS/JavaScript, JSON, Google Teachable Machine

---

## 2. Experiment Objective

We want to test whether RSU students can successfully recognize campus buildings, search for campus information, and use the chatbot to find campus services without assistance.

---

## 3. Requirement Scope for the Experiment

| Requirement ID | Requirement Summary | Related Screen/Feature | Tested in This Experiment? |
|---|---|---|---|
| FR-01 | Homepage displays project information and navigation | Homepage | Yes |
| FR-02 | Upload a building image for recognition | Upload Image | Yes |
| FR-03 | AI recognizes the uploaded building image | AI Recognition | Yes |
| FR-04 | Search for a building by name | Search Building | Yes |
| FR-05 | Chatbot answers campus-related questions | Chatbot | Yes |
| FR-06 | Display building information, facilities, services, clubs, and operating hours | Building Information Page | Yes |
| FR-07 | Admin manages campus information stored in the JSON dataset | Admin Panel | No |

---

## 4. MVP Experiment Type

### Selected experiment type

- Backend/database prototype
- Simple web prototype

### Reason for selection

Our prototype includes a working Flask backend, HTML/CSS/JavaScript frontend, a JSON dataset for campus information, and Google Teachable Machine for image recognition. These technologies allow users to interact with the main features and provide realistic feedback during validation.

---

## 5. Test Users

| Test User Group | Number of Testers | Why They Are Relevant |
|---|---:|---|
| RSU Freshmen | 3 | They are unfamiliar with the campus and are the primary target users. |
| International Students | 2 | They often need assistance locating campus buildings and services. |

---

## 6. Experiment Procedure Summary

1. Ask participants to open the RSU Campus Buddy prototype.
2. Upload a campus building image and verify whether the building is correctly recognized.
3. Search for a building using the search feature.
4. Ask the chatbot a campus-related question.
5. Review the displayed building information, facilities, services, and operating hours.
6. Record task completion, time taken, confusion points, and user feedback.
7. Collect suggestions for improving the prototype.

---

## 7. Expected Learning

After the experiment, the team will determine whether users can complete the main tasks without assistance, identify usability issues, evaluate the accuracy of the AI image recognition and chatbot responses, and decide which features should be improved before the final prototype.
