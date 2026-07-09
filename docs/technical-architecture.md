# Technical Architecture

## Project Title

RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)

---

## 1. Selected Prototype Platform

**Other:** Flask (Python) + HTML/CSS/JavaScript + JSON + Google Teachable Machine

---

## 2. Architecture Decision

Our team selected Flask because it is lightweight, easy to develop, and integrates well with Python. HTML, CSS, and JavaScript provide a responsive and user-friendly interface. Google Teachable Machine is used to recognize campus buildings from uploaded images, while a custom JSON file stores building information such as facilities, services, operating hours, student clubs, and university regulations. This architecture is suitable for our team's skills and can be completed within one semester.

---

## 3. Main Components

| Component | Description | Tool / Technology | Related Requirement |
|---|---|---|---|
| User Interface | Displays the homepage, search function, chatbot, and building information. | HTML, CSS, JavaScript | FR-01, FR-03, FR-05 |
| Image Upload | Allows users to upload a building image for identification. | HTML Form, Flask | FR-01 |
| Image Recognition | Identifies the uploaded building image. | Google Teachable Machine | FR-02 |
| Data Storage | Stores campus building information in a JSON file. | JSON | FR-05, FR-06 |
| Building Information | Displays building details, facilities, services, operating hours, clubs, and regulations. | Flask + JSON | FR-05, FR-06, FR-07 |
| Chatbot | Answers campus-related questions using stored information. | Flask (Rule-based Chatbot) | FR-03, FR-04 |
| Admin Function | Allows administrators to add, edit, and delete building information. | Flask + JSON | FR-12 |

---

## 4. What Will Be Fully Implemented?

- Homepage
- Building image upload
- Google Teachable Machine image recognition
- Building search
- Building information page
- Campus chatbot
- Admin management page
- JSON-based data storage

---

## 5. What Will Be Simulated?

- Building directions will provide simple guidance instead of real-time GPS navigation.
- Floor plans will display sample images where available.
- Campus information will be stored in a custom JSON file instead of the official Rangsit University database.

---

## 6. Final Prototype Risk

The biggest technical risk is the accuracy of the Google Teachable Machine model. Incorrect image predictions may return the wrong building information. To reduce this risk, the team will train the model using multiple images of each building from different angles and lighting conditions. Another risk is maintaining accurate building information in the JSON file, which will be updated through the administrator interface.
