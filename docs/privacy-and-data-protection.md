# Privacy and Data Protection

## Data Collection Summary

| Data Field | Why It Is Needed | Personal Data? | Sensitive Data? | Keep / Remove / Replace | Notes |
|---|---|---|---|---|---|
| Uploaded Building Image | Used for AI building recognition | No | No | Keep | Images are used only to identify campus buildings. |
| Building Name | Display recognized building information | No | No | Keep | Public campus information. |
| Building Location | Help students find the building | No | No | Keep | Public campus information. |
| Building Services | Show available services and facilities | No | No | Keep | Public information. |
| Student Clubs | Display clubs located in the building | No | No | Keep | Public campus information. |
| Opening Hours | Inform users of building operating hours | No | No | Keep | Public information. |
| Floor Map | Help users navigate inside buildings | No | No | Keep | Public campus information. |
| Search Keyword | Allow users to search campus information | No | No | Keep | Used only during the current session. |
| Chatbot Question | Process user requests and provide answers | No | No | Keep | Questions are not permanently stored in the prototype. |
| Admin Login Username | Authenticate administrators | Yes | No | Keep | Accessible only by authorized administrators. |
| Admin Passwords | Secure administrator access | Yes | Yes | Keep | Passwords should be protected and never displayed publicly. |
| Student ID | Not required for the prototype | Yes | No | Remove | The system does not require student identification. |
| Phone Numbers | Not required for the prototype | Yes | Yes | Remove | Avoid collecting unnecessary contact information. |
| Email Address | Not required for the prototype | Yes | No | Remove | Not needed for the MVP. |

---

## Privacy Rule for Prototype

The RSU Campus Buddy prototype only collects the minimum data necessary to provide campus building recognition and information services. Users upload a building image or enter a text question, and the system returns building information such as the building names, location, facilities, student clubs, opening hours, and floor maps.

The prototype does not collect unnecessary personal information such as student ID numbers, phone numbers, home addresses, or email addresses. Uploaded images are used only for building recognition and are not intended for long-term storage. Administrative functions are restricted to authorized users, and only administrators can modify campus information stored in the JSON database.

---

## Data Minimization Decision

After the privacy review, the team decided to remove all unnecessary personal information from the prototype.

### Removed Data Fields

- Student ID
- Phone Number
- Email Address
- Home Address
- Personal Profile Information

### Kept Data Fields

- Building images
- Building names
- Building locations
- Campus facilities
- Student clubs
- Opening hours
- Floor map
- Search keywords
- Chatbot questions
- Admin login credentials (administrator only)

By limiting data collection to only what is necessary, the prototype follows the principle of data minimization and helps protect user privacy while still meeting the project requirements.
