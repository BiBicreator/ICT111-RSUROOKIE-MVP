# Lab 10 - Feature Implementation Status

## Purpose
Use this file to prove that your prototype implementation is connected to `system-requirements.md`.

| Req ID | Required Functionality | Prototype Screen/Module | Current Status | Evidence | Next Fix Needed |
|---|---|---|---|---|---|
| FR-01 | Homepage or landing screen | Homepage | Working Draft | `prototype/index.html`, Homepage screenshot | Improve UI layout and project introduction |
| FR-02 | Primary user pathway | Homepage → Chat → Recognition Result → Directory → Admin | Working Draft | Navigation menu and page links | Improve navigation flow and user experience |
| FR-03 | User input or data submission | Chat (Image Upload) | Working Draft | Upload form, `script.js` | Improve image upload validation |
| FR-04 | Data storage or simulated storage | JSON Database (`buildings.json`) | Working Draft | `prototype/data/buildings.json` | Expand building information and categories |
| FR-05 | View records or information list | Directory | Working Draft | Directory page | Add more campus buildings and information |
| FR-06 | Search, filter, or category function | Directory Search | In Progress | Search bar, JavaScript filter | Add category and facility filters |
| FR-07 | Detail view for each record | Building Detail | Working Draft | Building information page | Display additional facilities, floor maps, and clubs |
| FR-08 | Status or progress tracking | Recognition Result | Working Draft | Google Teachable Machine prediction result | Improve prediction confidence and recognition messages |
| FR-09 | Admin or manager function | Admin Panel | In Progress | `admin.html` | Complete add, edit, and delete functions |
| FR-10 | Validation and error prevention | Upload Form | In Progress | JavaScript validation | Validate image type and file size before upload |
| FR-11 | Confirmation or feedback message | Upload Confirmation | Working Draft | Success message after upload | Improve success and error notifications |
| FR-12 | Dashboard or summary view | Dashboard | In Progress | Dashboard page | Add statistics and summary cards |
| FR-13 | Basic UI consistency | Homepage, Chat, Uni Map, Directory, Dashboard, Admin | Working Draft | Shared CSS stylesheet | Improve color consistency, spacing, and icons |
| FR-14 | Mobile-friendly/responsive design | All pages | In Progress | Responsive CSS | Test on different screen sizes and devices |
| FR-15 | Privacy and responsible data handling | Chat & Admin | Working Draft | Privacy notice and sample JSON data | Add clearer privacy statement and data handling information |
| FR-16 | Final prototype traceability | Documentation | Working Draft | Lab 04–10 documents | Verify all features match requirements and user stories |

---

## Summary

### Features working today
- Homepage with navigation
- Chat interface
- Image upload
- Google Teachable Machine building recognition
- Building directory
- JSON database integration
- Building detail page

### Features partially working
- Search and filter
- Dashboard
- Admin panel
- Responsive layout
- Upload validation
- Recognition result display

### Features not yet started
- Indoor navigation
- Voice interaction
- Multi-language chatbot
- User login and authentication
- Analytics dashboard improvements

### Features requiring instructor feedback
- Google Teachable Machine integration approach
- JSON database structure
- Admin permission simulation
- Future backend integration using Flask
