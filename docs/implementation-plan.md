# Lab 10 - Implementation Plan

## 1. Project Information

- **Group name:** RSUROOKIE
- **Project title:** RSU Campus Buddy – Smart Campus Chatbot for Student Services with Image Recognition
- **Repository link:**(https://github.com/BiBicreator/ICT111-RSUROOKIE-MVP)
- **Selected platform/tools:** HTML, CSS, JavaScript, Python Flask, Google Vision API, JSON Database, GitHub, VS Code
- **Backend status:** Simulated backend (Flask + JSON database)

---

## 2. Prototype Scope for Sprint 1

| Feature | Requirement ID | User Story ID | Screen/Module | Sprint 1 Status |
|---|---|---|---|---|
| Homepage / landing screen | FR-01 | US-01 | Homepage | In Progress |
| AI Chat & Image Upload | FR-03 | US-01 | Chat | In Progress |
| Building Directory | FR-05 | US-04 | Directory | In Progress |
| Search / Filter Buildings | FR-06 | US-04 | Directory | In Progress |
| Building Detail View | FR-07 | US-03 | Directory Detail | In Progress |
| AI Recognition Status | FR-08 | US-08 | Chat / Result | In Progress |
| Admin Management | FR-09 | US-07 | Admin | In Progress |
| Dashboard / Summary | FR-12 | US-10 | Dashboard | In Progress |

---

## 3. Implementation Approach

### Frontend
- Develop the user interface using HTML, CSS, and JavaScript.
- Build responsive pages for Chat, Uni Map, Directory, Dashboard, and Admin.

### Data Source / Storage
- Store campus building information in a JSON database.
- Retrieve and display building data dynamically using JavaScript.

### Admin / Status Handling
- Provide an admin page to update building information, facilities, clubs, and opening hours.
- Simulate administrator actions using the JSON database.

### Search / Filter Approach
- Implement keyword search by building name.
- Allow users to browse buildings through the interactive campus map.

### Validation Approach
- Validate uploaded images before sending them to Google Vision API.
- Display appropriate error messages for unsupported or invalid files.
- Show confirmation messages after successful image uploads.

### Screenshots / Evidence Approach
- Capture screenshots of each completed module:
  - Homepage
  - Chat
  - Uni Map
  - Directory
  - Dashboard
  - Admin
- Upload screenshots to the `/screenshots` folder as Sprint 1 evidence.

---

## 4. Member Responsibilities

| Member | Responsibility | Evidence of Contribution |
|---|---|---|
| Khin Zu Zu Oo | Frontend development, AI chatbot integration, Google Vision API, Directory, Dashboard, documentation | GitHub commits, Issues #45–#48 |
| Min Khant Zaw |  JSON database,testing support | GitHub commits, Issues #47 |

---

## 5. Risks or Blockers

| Risk | Planned Solution |
|---|---|
| Google Vision API quota or configuration issues | Provide setup instructions so users can create and use their own API key. |
| Incorrect AI building recognition | Improve training images and allow users to manually search the directory if recognition fails. |
| JSON data inconsistency | Validate JSON structure before loading data into the application. |
| Responsive layout issues on mobile devices | Test and adjust the interface using CSS media queries. |
| Git merge conflicts | Use feature branches and commit changes frequently to GitHub. |
