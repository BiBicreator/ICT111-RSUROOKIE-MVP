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

Students, especially freshmen, international students, and campus visitors, often struggle to identify campus buildings and find information about services, facilities, student clubs, operating hours, and university regulations. Information is often scattered across multiple sources, making it difficult to access quickly and efficiently.

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
- `/data/validation-results.csv`
- `/docs/customer-validation-summary.md`
- `/docs/analytics-insights.md`
- `/docs/mvp-decision.md`
- `/docs/test-user-notes.md`
- `/screenshots/validation-test-screens.png`
- `/docs/weekly-logbook.md`
