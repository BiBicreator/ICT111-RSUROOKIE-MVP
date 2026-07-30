# Feature Implementation Status

| Requirement ID | Requirement Summary | Prototype Screen/Module | Status | Evidence/Screenshot | Notes |
|---|---|---|---|---|---|
| FR-01 | Homepage or landing screen | Landing Page | **Completed** | `/screenshots/final-homepage.png` | Displays project title, target users, problem statement, solution, features, CTA, and acquisition metrics. |
| FR-02 | Primary user pathway | Landing Page → AI Chatbot → Results | **Completed** | `/screenshots/demo-flow.png` | Users can navigate from the landing page to the AI chatbot, upload an image, and receive building information. |
| FR-03 | User input or data submission | AI Chatbot Image Upload | **Completed** | `/screenshots/final-input-form.png` | Users upload campus building images for AI recognition using Google Teachable Machine. |
| FR-04 | Data storage or simulated storage | Flask Backend / JSON Data | **Completed** | `app.py`, `buildings.json` | Building information is stored in JSON files and processed by the Flask application. |
| FR-05 | View records/list | Building Directory | **Completed** | `/screenshots/final-record-list.png` | Users can browse the campus building directory and available facilities. |
| FR-06 | Search/filter/category | Directory Search | **Completed** | `/screenshots/final-record-list.png` | Users can search for buildings using keywords through the search function. |
| FR-07 | Detail view | Building Information Page | **Completed** | `/screenshots/final-detail-view.png` | Displays building description, facilities, clubs, opening hours, floor maps, and directions. |
| FR-08 | Status/progress tracking | AI Recognition Result | **Completed** | `/screenshots/final-detail-view.png` | Shows AI recognition result with confidence and matched building information. |
| FR-09 | Admin/manager function | Admin Panel | **Completed** | `/screenshots/final-admin-view.png` | Administrator can manage campus building information and update records. |
| FR-10 | Validation and feedback | Image Upload Form | **Completed** | `/screenshots/final-input-form.png` | Displays validation messages for invalid uploads and feedback after image recognition. |
| FR-11 | Dashboard/summary/metrics | Dashboard | **Completed** | `/screenshots/final-dashboard.png` | Dashboard displays prototype metrics including chatbot visits, image uploads, buildings mapped, and feedback statistics. |
| FR-12 | Final prototype traceability | Documentation & GitHub Repository | **Completed** | `README.md`, `/docs/` | All implemented features are traceable to system requirements, user stories, MVP features, and project documentation. |
