# RSU Campus Buddy

## Course Information

Course Code: ICT111.

Course Name: Fundamental Technology Entrepreneurship.

Instructor: Dr. Herison Surbakti.

Project Type: 14-Labs Continuous IT Startup MVP Development.

## Team Name
RSUROOKIE

## Team Members and Roles

| Name | Role | Responsibility |
|---|---|---|
| Khin Zu Zu Oo | Product Lead + Technical Lead | Define project direction, manage repository, and oversee technical development |
| Min Khant Zaw | Documentation Lead + Validation Lead | Maintain documentation and collect user feedback |
| Phyo Min Khant| UX/UI Lead | Design wireframes, user flow, and interface screens |

## Initial Problem Area

Students, especially freshmen, international students, and campus visitors, oftens struggle to identify campus buildings and find information about services, facilities, student clubs, operating hours, and university regulations. Information is often scattered across multiple sources, making it difficult to access quickly and efficiently.

## Target Users

- New students
- Current RSU students
- International students
- Campus visitors
- University staff

## Initial IT Venture Direction

The team is interested in developing a technology solution that improves student life and campus experiences. We are exploring opportunities related to campus navigation, student services, accommodation, and student-to-student interactions. Potential solutions may include AI-assisted systems, web applications, and digital platforms that help students access information more efficiently and solve everyday campus challenges.

## Selected IT Venture Direction

Our team selected **RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)** as the semester project. The system aims to help students identify campus buildings and instantly access information about facilities, services, student clubs, operating hours, and campus regulations through image recognition and chatbot technology.


## Technology Possibility

- Web Application
- Mobile-Friendly Interface
- AI-Assisted Image Recognition
- Chatbot System
- Cloud Database
- Information Management System

## Repository Structure

- docs: Team profile, idea log, weekly logbook, and project documentation
- prototype: Source code and prototype files
- data: Survey responses and validation data
- finance: Financial planning and budgeting
- diagrams: Wireframes, flowcharts, and system diagrams
- screenshots: Evidence of project progress
- pitch: Presentation slides and pitch materials

## Weekly Progress Log

| Week | Main Activity | Output | Status |
|---|---|---|---|
| Lab 1 | Repository setup and idea generation | Repository, team profile, README, initial idea log, weekly logbook | Completed |
| Lab 2 | Opportunity scanning and project selection | Opportunity scan, NUF scoring, selected opportunity document | Completed |
| Lab 3 | Customer problem discovery and validation | Survey responses, interviews, problem notes, assumption-evidence table, customer discovery summary | Completed |


## Current Status

During Lab 03, the team conducted customer problem discovery by surveying and interviewing RSU students, especially freshmen and international students. The findings confirmed that students often experience difficulty identifying campus buildings and finding information about facilities, services, and operating hours. Students currently rely on asking friends, university staff, websites, and social media, which are often inconvenient and time-consuming. Based on the collected evidence, the team decided to continue developing RSU Campus Buddy and focus on the most important user problems.

## Next Step

In Lab 04, the team will define the MVP requirements and begin designing the solution prototype. The team will prioritize core features such as building image upload, building information display, and chatbot interaction, followed by creating wireframes and an initial user interface design.

# README Update Template After Lab 03

## Customer Problem Discovery Summary

In Lab 03, our team collected early problem evidence from target users to confirm whether our selected problem from Lab 02 is real and important. We conducted surveys and interviews with RSU students regarding their experiences finding campus buildings and information.

## Target Respondents

- Freshmen (1st-year students)
- International students
- Current RSU students

**Number of responses:** 14 surveys and 5 interviews.

## Main Evidence Found

- 12 out of 19 respondents reported difficulty finding campus buildings or services.
- 10 out of 19 respondents usually ask friends or senior students for help.
- 11 out of 19 respondents said current methods are time-consuming or inconvenient.
- Students use university websites, social media, and Google Maps, but information is often scattered across different sources.

## Updated Problem Statement

Freshmen and international students at Rangsit University frequently experience difficulty identifying campus buildings and finding accurate information about services, facilities, and operating hours. They currently rely on asking others or searching through multiple sources, which is often time-consuming and inconvenient.

## Decision for Next Step

The team decided to continue with the same project direction and focus the MVP on solving the most significant problems identified during customer discovery.

The initial MVP will prioritize:
- Building identification through image upload
- Building and facility information
- Operating hours and regulations
- A chatbot for campus-related questions

# README Update - Lab 05

## Lab 05: Product Concept and UI/UX Wireframe

### Product Concept

RSU Campus Buddy is a web-based smart campus assistant designed to help freshmen, international students, and campus visitors quickly access campus information. Users can upload a photo of a campus building or search by building name to receive information about facilities, services, operating hours, student clubs, and university regulations. The system uses a Google Teachable Machine image recognition model and a custom database maintained by the project team to provide campus information through an easy-to-use interface and chatbot.

### Requirement-Driven Screens

| Screen | Related Requirement IDs | Wireframe File |
|---|---|---|
| Homepage / Landing | FR-01, FR-02 | /wireframes/homepage.png |
| Image Upload & Recognition | FR-03, FR-04 | /wireframes/input-form.png |
| Building Search / List | FR-05, FR-06 | /wireframes/record-list.png |
| Building Detail View | FR-07, FR-08 | /wireframes/detail-view.png |
| Chatbot | FR-09, FR-10 | /wireframes/chatbot.png |
| Admin View | FR-11, FR-12 | /wireframes/admin-view.png |

### User Flow

The user starts on the homepage and chooses either to upload a building image or search for a building by name. If an image is uploaded, the Google Teachable Machine model identifies the building and retrieves information from the project's custom database. Users can then view detailed building information or ask additional questions through the chatbot. Administrators can manage the building information by adding, editing, or deleting records through the admin interface.

**User Flow Diagram:** `/diagrams/user-flow.mmd`

### Team Contribution

All team members contributed to the same GitHub repository throughout Lab 05.

- **Product Lead:** Defined the product concept, requirements, and MVP scope.
- **Technical Lead:** Developed the system architecture, integrated Google Teachable Machine, and managed the project repository.
- **UX/UI Lead:** Designed the wireframes, user flow, and interface layout.
- **Documentation Lead:** Updated the README, documentation, and weekly logbook.
- **Validation Lead:** Ensured the wireframes and features aligned with the validated user requirements collected during customer discovery.

# Lab 06 Update - Business Model Canvas and Technical Architecture

## Lab 06 Summary

In Lab 06, our group developed the business model and technical design for **RSU Campus Buddy**. We completed the Business Model Canvas, Feature-Value Mapping, Technical Architecture, Data Structure, System Architecture Diagram, and User Flow Diagram. These documents define the product's value, technical implementation, and data organization, providing a clear foundation for developing the final prototype.

## Files Added or Updated

- [Business Model Canvas](docs/business-model-canvas.md)
- [Feature-Value Mapping](docs/feature-value-mapping.md)
- [Technical Architecture](docs/technical-architecture.md)
- [Data Structure](docs/data-structure.md)
- [System Architecture Diagram](diagrams/system-architecture.png)
- [Data Flow Diagram](diagrams/data-flow.mmd)
- [Weekly Logbook](docs/weekly-logbook.md)

## Technical Direction

The prototype uses a **backend-based architecture** with **Flask (Python)** as the backend, **HTML/CSS/JavaScript** for the frontend, **JSON** as the data storage, and **Google Teachable Machine** for AI image recognition. This architecture is suitable for our team's skills and supports the planned MVP features without requiring a complex database or official university system integration.

## Final Prototype Connection

The outputs from Lab 06 provide the technical foundation for the final prototype. The Business Model Canvas defines the product strategy, the Feature-Value Mapping ensures every feature delivers value to users, the Technical Architecture guides system development, the Data Structure organizes the prototype data, and the System Architecture and User Flow Diagrams define how users interact with the system. These documents will guide the implementation, testing, and refinement of the final RSU Campus Buddy prototype.

# README Update - Lab 08

## Lab 08: Customer Validation and Analytics Sheet

### Validation Objective

The objective of this validation was to evaluate whether users could successfully use the main features of **RSU Campus Buddy**. The team tested AI building recognition, campus building search, chatbot interaction, building information pages, and the admin management functions to identify usability issues and collect feedback for improving the MVP.

---

### Prototype Version Tested

- **Version:** v1.0 (MVP)
- **Link:** `/prototype/`
- **Screenshots:** `/screenshots/validation-test-screens.png`

---

### Analytics Summary

| Metric | Result |
|---|---:|
| Total test users | **12** |
| Task success rate | **91.7% (11/12)** |
| Average feedback score | **4.3 / 5** |
| Average interest level | **4.6 / 5** |
| Main confusion point | AI image recognition with unclear images, chatbot responses, and search keywords |

---

### MVP Decision

The team decided to **continue with minor revisions**. Validation results showed that most users successfully completed the main tasks and found the prototype useful. Improvements will focus on increasing AI recognition accuracy, expanding chatbot responses, improving the search function, and enhancing the admin interface before the final prototype.

---

### Files Added

- `/data/validation-results.xlsx`
- `/data/Analytics-Dashboard.xlsx`
- `/data/validation-results.csv`
- `/docs/customer-validation-summary.md`
- `/docs/analytics-insights.md`
- `/docs/mvp-decision.md`
- `/docs/test-user-notes.md`
- `/screenshots/validation-test-screens.png`
- `/docs/weekly-logbook.md`

## Lab 09 - Responsible IT Check

### Responsible Design Summary

During Lab 09, our team reviewed the RSU Campus Buddy prototype from the perspectives of privacy, ethics, intellectual property (IP), security, and responsible data handling.

The main findings were:

- **Privacy:** The prototype only collects the minimum data required for AI building recognition and avoids collecting unnecessary personal information such as student IDs, phone numbers, or email addresses.
- **Ethics:** The AI building recognition model may occasionally produce incorrect results, so users are informed that recognition accuracy depends on image quality.
- **Intellectual Property (IP):** All third-party resources, including Google Teachable Machine, Bootstrap, Font Awesome, Google Fonts, and ChatGPT, were documented and properly acknowledged.
- **Security:** Administrator functions are separated from student functions, input validation is implemented, and image uploads are restricted to supported formats. Additional administrator authentication will be implemented before the final prototype.
- **Risk Management:** A project risk register was created to identify privacy, ethical, legal, security, IP, and data quality risks, together with mitigation strategies.

### Files Added

- `docs/legal-ethical-checklist.md`
- `docs/privacy-and-data-protection.md`
- `docs/ip-and-third-party-assets.md`
- `docs/security-risk-check.md`
- `docs/risk-register.md`
- `docs/updated-requirements-note.md`
- `docs/weekly-logbook.md`
- `docs/user-consent-statement.md`
- `docs/data-handling-policy.md`
- `data/data-inventory.csv`
- `data/ip-and-third-party-assets.csv`
- `data/risk-register.csv`

### Requirement Update

After reviewing the prototype during Lab 09, the team confirmed that **no functional changes were required** to `system-requirements.md`. The responsible design review resulted in implementation improvements related to privacy, security, ethics, and data handling, while the original functional requirements remain valid.

### Team Contributions

| Member | Contribution |
|---|---|
| Min Khant Zaw | Prepared the Data Inventory, Privacy and Data Protection Review, Legal & Ethical Checklist, Security Risk Check, Risk Register, Data Handling Policy. |
| Khin Zu Zu Oo | Created GitHub Issues for Lab 09, organized repository files and folders, IP and Third-Party Assets Register,User Consent Statement, Updated Requirements Note, and supporting CSV documentation. updated the README, maintained project documentation, and assisted with repository management. |
## Lab 10 - MVP Implementation Sprint 1

### Sprint Goal
Our goal in Lab 10 is to develop the first working version of the **RSU Campus Buddy** prototype based on the approved requirements, user stories, system architecture, wireframes, and responsible IT design. The prototype demonstrates the core workflow of recognizing campus buildings using **Google Teachable Machine**, displaying building information from a **JSON database**, and providing administrative management functions.

---

### Implementation Approach

- **Platform/tools:** HTML, CSS, JavaScript, Google Teachable Machine (TensorFlow.js), JSON Database, GitHub, VS Code
- **Backend status:** Simulated backend (JSON database)
- **Data storage/simulation:** Campus building information stored in `prototype/data/buildings.json`
- **Prototype folder:** `/prototype`

---

### Features Implemented in Sprint 1

| Feature | Requirement ID | Status | Evidence |
|---|---|---|---|
| Homepage | FR-01 | ✅ Working Draft | `frontend.html` |
| AI Chat & Image Upload | FR-03 | ✅ Working Draft | `frontend.html`, `app.py` |
| Campus Building Database | FR-04 | ✅ Working Draft | `database.json` |
| Campus Directory | FR-05 | ✅ Working Draft | `frontend.html`, `database.json` |
| Search & Filter | FR-06 | 🟡 In Progress | Search function in `frontend.html` |
| Building Detail View | FR-07 | ✅ Working Draft | Building information displayed after AI recognition in `frontend.html` |
| AI Recognition Result | FR-08 | 🟡 In Progress | Google Teachable Machine integration in `app.py` |
| Admin Panel | FR-09 | 🟡 In Progress | `admin.html` |
| Input Validation | FR-10 | 🟡 In Progress | `app.py` |
| Dashboard / Analytics | FR-12 | 🟡 In Progress | Dashboard section in `frontend.html` |

---

### Screenshots

- **Homepage:** `/screenshots/homepage.png`
- **AI Chat & Image Upload:** `/screenshots/AI-image-chatbotpage.png`
- **Campus Directory:** `/screenshots/Campus Directory.png`
- **Uni Map:** `/screenshots/UniMap.png`
- **Chatbot Response:** `/screenshots/chatbot-respond.png`
- **Chatbot Direction Response:** `/screenshots/chatbot-respond-direction.png`
- **Floor Map:** `/screenshots/floor-map.png`
- **Admin Dashboard:** `/screenshots/admin-page.png`
- **Admin Building Management:** `/screenshots/admin-building management-page.png`
- **Admin Teachable Machine Training:** `/screenshots/admin-teachable-machine-training-page.png`

---

### Team Contribution

- **Khin Zu ZU Oo**
  - Developed the Homepage, Chat interface, Directory, Dashboard,Managed the GitHub repository, JSON database, and integrated Google Teachable Machine.
  - Created and updated project documentation.

- **Min Khant Zaw**
  -  Admin panel, and testing support.

  ## Lab 11: MVP Implementation Sprint 2 and Startup Metrics

### Prototype Progress

During Lab 11, our team enhanced the MVP developed in Lab 10 by improving the AI-powered campus navigation workflow, expanding the campus building database, and refining the overall user experience. We integrated Google Teachable Machine with our Flask backend (`app.py`) to improve building recognition, updated the Campus Directory with additional building information, enhanced the search functionality, and improved the Admin Panel for managing campus data. We also documented startup/product metrics and completed prototype testing to evaluate the system's usability and performance.

---

### Implemented / Improved Features

| Requirement ID | Feature | Status | Evidence |
|---|---|---|---|
| FR-03 | AI Chatbot and Image Upload | ✅ Improved | `frontend.html`, `app.py` |
| FR-04 | Campus Building Database | ✅ Improved | `database.json` |
| FR-05 | Campus Directory | ✅ Improved | `frontend.html` |
| FR-06 | Building Search | 🟡 Improved | Search function in `frontend.html` |
| FR-08 | AI Building Recognition | 🟡 Improved | Google Teachable Machine + `app.py` |
| FR-09 | Admin Panel | 🟡 Improved | `admin.html` |
| FR-12 | Startup Metrics Documentation | ✅ Completed | `docs/startup-metrics.md` |

---

### Startup/Product Metrics

The following startup metrics were documented:

- Total Campus Buildings
- AI Image Recognition Requests
- Building Recognition Accuracy
- Directory Search Success Rate
- Admin Building Updates
- Average User Feedback Score

These metrics help evaluate user activity, AI performance, and prototype effectiveness.

---

### Prototype Screenshots

- Homepage (`frontend.html`)
- AI Chat and Image Recognition
- Campus Directory
- Building Information Display
- Admin Panel (`admin.html`)
- Dashboard / Startup Metrics
- Mobile Responsive Interface

---

### Member Contributions

**Khin Zu Zu Oo**
- Improved Homepage and user interface.
- Enhanced AI Chatbot and Google Teachable Machine integration.
- Improved Campus Directory and Search functionality.
- Updated responsive design.
- Updated Flask backend (`app.py`) and `database.json`.
- Improved Admin Panel functionality.
- Prepared Lab 11 documentation.
- Updated README and project reports.

---

### Remaining Work

- Improve Google Teachable Machine recognition accuracy with additional training images.
- Complete Admin CRUD (Create, Read, Update, Delete) functionality.
- Add advanced search filters (faculty, building category, facilities).
- Expand dashboard analytics and startup metrics.
- Improve responsive design for different screen sizes.
- Perform final usability testing and fix remaining issues before the final presentation.

# Lab 12 - Landing Page and Digital Go-to-Market

## Landing Page

- **Landing page folder/link:** `landing-page/index.html`
- **Main CTA:** **Try the Chatbot**
- **Prototype/demo link:** `frontend.html`

---

## Go-to-Market Plan

- **Target early users:**
  - New and current RSU students
  - International students
  - University staff
  - Campus visitors

- **Selected channels:**
  - RSU class LINE groups
  - Campus QR code posters
  - Facebook and Instagram
  - University orientation events
  - GitHub project repository

- **Main marketing message:**

  *Navigate RSU Campus Smarter with AI. Upload a building photo to instantly identify campus buildings, explore facilities, and find directions using RSU Campus Buddy.*

---

## Acquisition Metrics

- **Landing Page Views** – Number of users who open the landing page.
- **Chatbot CTA Clicks** – Number of users who click **Try the Chatbot**.
- **Chatbot Visits** – Number of users who open and test the chatbot prototype.
- **Image Uploads** – Number of building images submitted for AI recognition.
- **Feedback Responses** – Number of users who submit prototype feedback.
- **Interest Conversion Rate** – Percentage of landing page visitors who continue to the chatbot.

---

## Screenshots

- Landing page screenshot: `/screenshots/landing-page.png`
- CTA screenshot: `/screenshots/call-to-action.png`

---

## Requirement Alignment

The landing page communicates the purpose and value of **RSU Campus Buddy (Smart Campus Chatbot with AI Image Recognition)** while encouraging users to test the prototype through the **Try the Chatbot** call-to-action. The landing page introduces the AI building recognition feature, interactive campus map, building directory, and campus navigation functions that correspond to the functional requirements defined in `system-requirements.md`. The acquisition metrics support prototype evaluation by measuring user engagement, chatbot usage, image uploads, and feedback collection.

---

## Member Contributions

| Member | Contribution | Commit/Issue Evidence |
| --- | --- | --- |
| KHIN ZUZU OO | Designed the landing page, created acquisition metrics, prepared the digital go-to-market plan, wrote marketing messages, and updated Lab 12 documentation. | GitHub commits and Lab 12 documentation |

