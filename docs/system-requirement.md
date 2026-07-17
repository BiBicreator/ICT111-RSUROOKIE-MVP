# System Requirements

## Project Title

**RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)**

## Functional Requirements

| Req ID | Requirement | Description |
| --- | --- | --- |
| **FR-01** | Homepage / Landing Page | The system shall display the project title, target users, project purpose, and navigation to the main features. |
| **FR-02** | Building Image Recognition | The system shall allow users to upload a campus building image for AI recognition using Google Teachable Machine. |
| **FR-03** | Chatbot Question Input | The system shall allow users to enter campus-related questions through the chatbot interface. |
| **FR-04** | Campus Data Management | The system shall retrieve and manage campus information stored in a JSON dataset. |
| **FR-05** | Building Information Display | The system shall display building information including the building name, description, services, facilities, operating hours, and student clubs. |
| **FR-06** | Search Function | The system shall allow users to search for buildings or campus services using keywords. |
| **FR-07** | Building Detail View | The system shall display detailed information for a selected building, including floor plans and available facilities. |
| **FR-08** | Recognition Result / Information Status | The system shall display the AI recognition result or an appropriate message if the building cannot be identified. |
| **FR-09** | Admin Management | The administrator shall be able to add, edit, update, or delete campus information stored in the JSON dataset. |
| **FR-10** | Input Validation | The system shall validate uploaded images and required user inputs before processing. |
| **FR-11** | User Feedback Message | The system shall display confirmation or error messages, such as successful recognition or invalid image upload. |
| **FR-12** | Campus Information Summary | The system shall provide a summary page listing available campus buildings and services. |
| **FR-13** | Consistent User Interface | All pages shall use a consistent layout, navigation menu, buttons, fonts, and color scheme. |
| **FR-14** | Responsive Design | The system shall provide a responsive interface suitable for desktop and mobile devices. |
| **FR-15** | Privacy Protection | The prototype shall avoid collecting unnecessary personal information and only process uploaded building images for recognition purposes. |
| **FR-16** | Requirement Traceability | Every feature and screen in the prototype shall map to the project's user stories, MVP features, and system requirements. |

---

# Technical Requirements

## Prototype Platform

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **AI Model:** Google Teachable Machine
- **Data Storage:** JSON
- **Development Tool:** Visual Studio Code
- **Version Control:** GitHub

---

## Main User Workflow

1. Open the RSU Campus Buddy homepage.
2. Upload a campus building image **or** search for a building.
3. The system recognizes the building using Google Teachable Machine.
4. The system retrieves building information from the JSON dataset.
5. The chatbot displays the building name, facilities, services, operating hours, student clubs, and floor plan.
6. Users may continue searching for another building or ask another campus-related question.

---

## Admin Workflow

1. Login to the Admin Panel.
2. Add new building information.
3. Edit existing building information.
4. Delete incorrect building records.
5. Save updates to the JSON dataset.

---

## Data Storage

The prototype uses a **JSON dataset** to store:

- Campus building information
- Building descriptions
- Facilities
- Services
- Student clubs
- Operating hours
- Floor plans
- Navigation information

---

## Technology Stack

| Component | Technology |
| --- | --- |
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask (Python) |
| AI Recognition | Google Teachable Machine |
| Database | JSON |
| Version Control | GitHub |

---

## Notes

This prototype is developed for educational purposes as part of the ICT105 course. The system uses a custom JSON dataset instead of the official Rangsit University database. Real-time navigation is outside the MVP scope and is simulated using static campus directions.
