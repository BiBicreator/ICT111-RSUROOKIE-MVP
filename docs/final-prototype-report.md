# Final Prototype Report

## 1. Project Title

**RSU Campus Buddy (Smart Campus Chatbot with AI Image Recognition)**

---
## Team Members and Roles

| Name | Role | Responsibility |
|------|------|----------------|
| **Khin Zu Zu Oo** | Product Lead + Technical Lead | Defined the project direction, managed the GitHub repository, developed the AI image recognition system, Flask backend, landing page, dashboard, and integrated the overall prototype. |
| **Min Khant Zaw** | Documentation Lead + Validation Lead | Maintained project documentation, prepared reports and GitHub documentation, conducted user testing, collected feedback, and validated prototype requirements. |
| **Phyo Min Khant** | UX/UI Lead | Designed the user interface, wireframes, user flow, landing page layout, and improved the overall user experience and visual consistency of the prototype. |
---

## 3. Problem Background

New students and visitors at Rangsit University often experience difficulty identifying campus buildings and locating important services. Campus information is scattered across university websites, social media pages, and printed maps, making it difficult to quickly find classrooms, offices, laboratories, clubs, and student services. This results in confusion, wasted time, and repeated requests for directions from university staff. Based on early validation and user feedback, students wanted a faster and easier way to identify campus buildings and access campus information.

---

## 4. Target Users

**Primary Users**
- New students at Rangsit University
- Current students unfamiliar with certain buildings
- Visitors and parents visiting the campus

**Secondary Users**
- University staff
- Campus administrators

These users need a simple way to recognize campus buildings and quickly access information such as available facilities, offices, clubs, opening hours, floor maps, and directions.

---

## 5. Evidence Summary

The project was developed using evidence collected throughout previous labs.

- User interviews indicated that students often struggled to identify unfamiliar campus buildings.
- Validation testing showed that users preferred uploading a photo rather than manually searching through directories.
- User testing demonstrated that the AI image recognition feature significantly reduced the time required to locate building information.
- Feedback also suggested improving recognition accuracy by training the AI model with additional building images.

---

## 6. Final Prototype Overview

RSU Campus Buddy is a web-based smart campus assistant that uses AI image recognition to identify university buildings from uploaded photographs. The prototype is built using HTML, CSS, JavaScript, Python Flask, and Google Teachable Machine.

Main functions include:

- AI building recognition from uploaded images
- Interactive campus building directory
- Building information pages
- Search functionality
- Dashboard showing prototype metrics
- Administrator panel for managing campus information
- Responsive desktop and laptop interface

The prototype allows users to quickly identify buildings and access useful campus information without searching through multiple websites.

---

## 7. Requirement Traceability Summary

| Requirement ID | Implemented Feature/Screen | User Story ID | Evidence Source | Status |
|---|---|---|---|---|
| FR-01 | Landing Page | US-01 | Homepage Screenshot | Completed |
| FR-02 | User Navigation Flow | US-02 | Demo Flow | Completed |
| FR-03 | AI Image Upload | US-03 | Chatbot Screenshot | Completed |
| FR-04 | JSON Data Storage | US-04 | Flask Backend | Completed |
| FR-05 | Building Directory | US-05 | Directory Screenshot | Completed |
| FR-06 | Search Buildings | US-06 | Search Function | Completed |
| FR-07 | Building Detail Page | US-07 | Detail Screenshot | Completed |
| FR-08 | Recognition Result | US-08 | AI Prediction Screen | Completed |
| FR-09 | Admin Panel | US-09 | Admin Screenshot | Completed |
| FR-10 | Input Validation & Feedback | US-10 | Upload Validation | Completed |
| FR-11 | Dashboard Metrics | US-11 | Dashboard Screenshot | Completed |
| FR-12 | Requirement Traceability | US-12 | GitHub Documentation | Completed |

---

## 8. Data Handling

The prototype processes several types of data:

**Collected Data**
- Uploaded campus building images
- Search keywords entered by users

**Stored Data**
- Campus building information stored in JSON files
- Chat history stored using localStorage
- Prototype metrics stored locally

**Displayed Data**
- Building names
- Facilities
- Student clubs
- Opening hours
- Building descriptions
- Floor maps
- Recognition confidence

**Search and Filter**
- Search buildings by keyword
- Browse the building directory

**Updated Data**
- Administrators can update building information.

The prototype does not collect unnecessary personal information from users.

---

## 9. Validation and User Testing Results

Five users tested the prototype during Lab 13.

The testing showed that:

- Users successfully uploaded building images.
- Most users easily understood the AI recognition workflow.
- Users appreciated the building directory and search functionality.
- The dashboard was considered useful for demonstrating prototype metrics.
- Some users suggested improving AI recognition accuracy by adding more training images.

Overall, the prototype met its main objectives and required only minor improvements before the final release.

---

## 10. Startup/Product Metrics

The prototype includes several acquisition and product metrics:

- Landing page visits
- Chatbot demo visits
- Image uploads
- Buildings mapped
- Feedback responses
- User testing completion rate

These metrics help evaluate user engagement, prototype usage, and future improvements.

---

## 11. Business Value and Venture Direction

RSU Campus Buddy provides value by making campus navigation faster and easier for students and visitors.

The system:

- Reduces confusion on campus
- Saves time locating buildings
- Decreases repetitive direction requests to university staff
- Improves the overall campus experience

The product could be expanded to other universities, hospitals, shopping malls, airports, and large public facilities that require indoor navigation and building identification.

---

## 12. Limitations and Future Improvements

Current limitations include:

- Google Teachable Machine model currently supports only a limited number of campus buildings.
- Recognition accuracy decreases when images are taken from unusual angles.
- Indoor navigation is still under development.
- The prototype currently supports desktop and laptop devices only.

Future improvements include:

- Train additional building images to improve AI accuracy.
- Expand the campus building database.
- Add real-time indoor navigation.
- Improve dashboard analytics.
- Develop a mobile version.
- Integrate Google Maps and GPS navigation.
- Connect the system with the official university information system.
