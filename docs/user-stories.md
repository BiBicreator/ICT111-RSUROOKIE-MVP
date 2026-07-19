# Lab 04 - User Stories and Acceptance Criteria

## User Story Format

As a [user role], I want to [goal/action], so that [benefit/value].

## User Stories

| Story ID | Role | User Story | Related Requirement | Priority | Acceptance Criteria | Demo Evidence |
|---|---|---|---|---|---|---|
| US-01 | Student | As a student, I want to upload a campus building photo so that I can instantly identify the building. | FR-03 | Must | Given the user uploads a valid building image, when the image is submitted, then the system recognizes the building and displays its name. | Screenshot of AI recognition |
| US-02 | Student | As a student, I want to ask questions about campus locations so that I can quickly find information. | FR-02 | Must | Given the user enters a question, when it is submitted, then the chatbot returns relevant campus information. | Screenshot of chatbot response |
| US-03 | Student | As a student, I want to view building details so that I know the available facilities, opening hours, and student clubs. | FR-07 | Must | Given a recognized building, when the user opens its details, then the system displays building information, facilities, clubs, opening hours, and floor map. | Building detail screen |
| US-04 | Student | As a student, I want to search campus buildings by name so that I can quickly find the information I need. | FR-06 | Should | Given the user enters a building name, when the search is performed, then matching buildings are displayed. | Search page screenshot |
| US-05 | Student | As a student, I want to view directions between buildings so that I can easily navigate around campus. | FR-02 | Should | Given the user selects a destination, when the navigation feature is used, then the system shows the route or directions. | Navigation screen |
| US-06 | Student | As a student, I want to browse the campus map so that I can explore buildings before visiting them. | FR-05 | Could | Given the campus map page is opened, when a building is selected, then its information is displayed. | Campus map screen |
| US-07 | Administrator | As an administrator, I want to update building information so that students always receive accurate campus information. | FR-09 | Must | Given the administrator logs in, when building information is edited and saved, then the JSON database is updated successfully. | Admin dashboard |
| US-08 | Student | As a student, I want to receive a confirmation message after uploading an image so that I know my request has been processed. | FR-11 | Must | Given an image is successfully uploaded, when processing finishes, then the system displays a confirmation message. | Confirmation message |
| US-09 | Student | As a student, I want the system to reject invalid image uploads so that only supported images are processed. | FR-10 | Must | Given an invalid or unsupported file is uploaded, when validation occurs, then an error message is displayed. | Validation message |
| US-10 | Administrator | As an administrator, I want to view summary statistics so that I can monitor campus information and system usage. | FR-12 | Should | Given the admin dashboard is opened, when summary data is loaded, then charts and statistics are displayed. | Dashboard screenshot |

---

## Acceptance Criteria Checklist

A good acceptance criterion should be:

- ✅ Testable
- ✅ Observable in the final prototype
- ✅ Connected to a functional requirement
- ✅ Connected to user evidence
- ✅ Specific and measurable

---

## Rejected / Future User Stories

| Story ID | Reason for Postponing | Future Condition |
|---|---|---|
| US-11 | Voice search for campus navigation | Add after the web prototype is completed. |
| US-12 | Real-time indoor navigation | Implement if indoor positioning or GPS support becomes available. |
| US-13 | Student login with university account | Add when authentication and backend services are implemented. |
| US-14 | Push notifications for campus events | Consider for a future mobile application version. |
