# Weekly Venture Logbook

## Lab 1: Lab Setup and IT Venture Repository

### What We Completed

1. Created the GitHub repository and organized the required folder structure.
2. Assigned team roles and responsibilities for the semester project.
3. Prepared the README file, team profile, idea log, and selected RSU Campus Buddy as the primary project idea.

### What We Learned

1. How to create and manage a GitHub repository for project collaboration.
2. The importance of documentation, version control, and project planning.
3. How to identify real user problems and develop potential IT venture solutions.

### Problems or Difficulties

1. Choosing the most feasible project idea among several possible concepts.
2. Understanding GitHub Issues, repository management, and commit workflows.

### Evidence of Work

- GitHub repository link: [https://github.com/BiBicreator/ICT111-RSUROOKIE-MVP.git]
- Screenshot: Repository folder structure and GitHub Issues
- File created:
  - README.md
  - docs/team-profile.md
  - docs/idea-log.md
  - docs/weekly-logbook.md
- Commit link: [Insert Commit Link]

### Decision Made This Week

The team decided to develop RSU Campus Buddy, a Smart Campus Chatbot for Student Services with Image Recognition. The system will help students identify campus buildings and instantly access information about services, facilities, student clubs, operating hours, and campus regulations through an AI-powered chatbot.

### Plan for Next Week

1. Conduct opportunity scanning related to campus navigation and student service accessibility.
2. Gather feedback from students through surveys and interviews.
3. Identify the most important user problems and define the core features of the Minimum Viable Product (MVP).
4. Begin creating initial user flow and wireframe designs for the system.

## Lab 02: IT Opportunity Scanning
### What We Completed
1. Reviewed and analyzed three project ideas from Lab 1.
2. Conducted opportunity scanning and evaluated potential IT venture opportunities using NUF scoring.
3. Selected RSU Campus Buddy as the semester project and updated project documentation.
### Selected Opportunity
RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)
### Why We Selected It
The team evaluated several opportunities using the NUF (New, Useful, Feasible) framework. RSU Campus Buddy received the highest score because it solves a real problem experienced by students, provides a useful campus information service, and can be developed as a web-based MVP using available technologies within the semester timeframe.

### What We Rejected
Student Roommate Matching & Housing Platform was not selected because it requires more complex matching logic, larger amounts of user data, and additional validation compared to the selected project.
### What We Learned
1. How to identify opportunities based on real user problems rather than technology trends.
2. How to compare ideas objectively using NUF scoring.
3. The importance of selecting a project that is both useful and feasible to develop within the semester.
### Evidence of Work
- Opportunity scan file: docs/opportunity-scan.md
- NUF scoring file: data/opportunity-scoring.xlsx
- Selected opportunity file: docs/selected-opportunity.md
- GitHub issue screenshot: [Insert Screenshot]
- Commit link: [Insert Commit Link]
### Plan for Lab 03
The team will prepare interview and survey questions for RSU students, especially freshmen and international students. We will collect evidence about difficulties in campus navigation and information accessibility to validate the problem and identify the most valuable MVP features.

# Weekly Venture Logbook

## Lab 03: Customer Problem Discovery

### What We Completed
1. Prepared customer discovery questions and identified target respondents.
2. Conducted surveys and interviews with RSU students to validate the problem.
3. Created problem notes, assumption-evidence table, and customer discovery summary.

### What We Learned About the Problem
1. Many freshmen and international students have difficulty finding campus buildings and information.
2. Students currently rely on friends, university staff, websites, and social media to find information.
3. Information is scattered across multiple sources, making it inconvenient and time-consuming to access.

### What Evidence We Collected
- Number of respondents/interviews: 14 survey responses and 5 interviews.
- Evidence file: `data/raw-responses.xlsx`
- Key repeated pattern: Students often ask friends or senior students for directions and spend extra time searching for campus information.

### What We Changed Based on Evidence
The team decided to focus the MVP on the most important user needs, including building identification with image recognition, facility information, operating hours, and chatbot assistance. Advanced features will be considered in future versions.

### Problems or Difficulties
1. Finding enough target respondents, especially international students.
2. Some responses were incomplete or provided limited details about their experiences.

### Evidence of Work
- GitHub repository link: `https://github.com/BiBicreator/ICT111-RSUROOKIE-MVP`
- Customer questions file: `docs/customer-questions.md`
- Raw responses file: `data/raw-responses.xlsx`
- Assumption-evidence table: `docs/assumption-evidence-table.md`
- Commit link: `https://github.com/BiBicreator/ICT111-RSUROOKIE-MVP/commit/7ea3d0c2ea1422ac5fe85a4b3ab660f79e8830b6`

### Plan for Lab 04
The team will define the customer segments and create user personas based on the collected evidence. We will then develop user stories and identify the core features that should be included in the MVP design and prototype.

# Weekly Logbook - Lab 05

## Group Name

RSUROOKIE

## Project Title

RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)

## Lab 05 Focus

Product Concept and UI/UX Wireframe

## What We Completed Today

- [x] Reviewed Lab 04 requirements
- [x] Defined product concept
- [x] Mapped features to requirements
- [x] Created required wireframe screens
- [x] Created user flow diagram
- [x] Built clickable prototype draft or screen navigation plan
- [x] Updated GitHub repository

## Member Contributions

| Member Name | Contribution | Evidence / Commit Link |
|---|---|---|
| Member 1 | Defined the product concept, MVP scope, and system requirements. | GitHub Commit |
| Member 2 | Designed wireframes and user flow diagram. | GitHub Commit |
| Member 3 | Updated GitHub documentation, README, and feature mapping. | GitHub Commit |

## Decisions Made

| Decision | Reason | Related Requirement |
|---|---|---|
| Use Google Teachable Machine for image recognition. | Easy to integrate and suitable for a semester MVP. | FR-03, FR-04 |
| Store campus information in a custom database instead of the official RSU database. | Official university databases are not accessible for this project. | FR-07, FR-08 |
| Exclude real-time GPS navigation from the MVP. | Beyond the project scope and not required for the first prototype. | FR-12 |
| Include an admin page to manage campus information. | Allows manual updating of building information in the custom database. | FR-11 |

## Problems Found

- Some wireframes required several revisions to better match the functional requirements.
- It was challenging to organize all required screens while keeping the interface simple and user-friendly.
- The team needed to ensure every screen could be traced back to the corresponding functional requirements.

## Next Steps Before Lab 06

- Finalize all wireframes based on team feedback.
- Develop the HTML/CSS interface from the approved wireframes.
- Integrate the Google Teachable Machine image recognition model.
- Connect the frontend with the Flask backend (`app.py`) and the custom database.
- Begin implementing the core MVP features.

# Weekly Logbook - Lab 06

## Group Name

RSUROOKIE

## Project Title

RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)

## Date

(Write your lab date)

## Members Present

| Member Name | Contribution Today | GitHub Evidence / Commit / File Updated |
|---|---|---|
|Khin Zu Zu Oo | Completed the Business Model Canvas, Feature-Value Mapping, Technical Architecture, Data Structure, System Architecture Diagram, User Flow Diagram, updated project documentation, and uploaded the JSON dataset. | Multiple commits, `/docs/`, `/data/`, `/diagrams/` |
|Min Khant Zaw | Created GitHub issues, created project files and folders, and organized the repository structure. | GitHub Issues, repository setup commits |

---

## Decisions Made Today

### 1. Business model decision

The team agreed to focus on RSU students, especially freshmen and international students. The MVP will provide campus building recognition, campus information, and a chatbot to improve access to university services.

### 2. Technical architecture decision

The team selected **Flask (Python)** for the backend, **HTML/CSS/JavaScript** for the frontend, **Google Teachable Machine** for image recognition, and **JSON** as the data storage method because these technologies match our team's skills and are feasible within one semester.

### 3. Data structure decision

The team decided to use a JSON-based dataset containing campus information, building details, navigation data, and Teachable Machine configuration instead of an official university database.

### 4. Diagram decision

The team completed the System Architecture Diagram and User Flow Diagram. Both diagrams were updated to match the actual prototype and technologies used in the project.

---

## Problems or Risks Found

- Google Teachable Machine recognition accuracy depends on the quality and variety of training images.
- Campus information must be manually maintained because the prototype does not connect to the official Rangsit University database.
- Real-time navigation is outside the MVP scope and will be simulated using static directions.

---

## Next Actions Before Lab 07

- Finalize the System Architecture and User Flow diagrams.
- Improve the UI design and screen navigation.
- Continue implementing the Flask backend and frontend integration.
- Test Google Teachable Machine image recognition with additional building images.
- Verify that the JSON dataset matches the prototype requirements.

---

## Lecturer / TA Notes

(To be completed during or after the lab.)
