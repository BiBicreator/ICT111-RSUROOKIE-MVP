# Data Handling Policy

## Data Collection

The RSU Campus Buddy prototype collects only the minimum data required to provide its services.

Collected data includes:

- Uploaded building images for AI recognition
- Building search keywords
- Chatbot questions
- Campus building information (building name, location, facilities, student clubs, opening hours, floor maps)
- Administrator login credentials (administrator only)

The prototype does **not** collect personal information such as student ID numbers, phone numbers, home addresses, or financial information.

---

## Data Storage

The prototype stores and simulates data using:

- **JSON database** for campus building information
- **HTML/CSS/JavaScript frontend** for the user interface
- **Flask (Python)** backend to process requests
- **Google Teachable Machine** for AI image recognition
- Sample datasets for testing and validation

No personal user data is permanently stored during prototype testing.

---

## Data Access

| User Role | Access Permission |
|------------|-------------------|
| Student | Upload building images, search campus information, interact with the chatbot, and view building details. |
| Administrator | Add, edit, update, and manage campus building information stored in the JSON database. |

Only authorized administrators can modify campus information.

---

## Data Minimization

The team reviewed the prototype and removed unnecessary personal data.

### Removed Fields

- Student ID
- Phone number
- Email address
- Home address
- Personal profile information
- Financial information

### Kept Fields

- Building image
- Building name
- Building location
- Facilities
- Student clubs
- Opening hours
- Floor map
- Search keywords
- Chatbot questions
- Administrator login credentials

---

## Responsible Data Rule

The RSU Campus Buddy prototype follows responsible data handling practices by collecting only the information necessary to provide campus navigation and information services.

The system:

- Collects only the minimum data required for the prototype.
- Does not request unnecessary personal or sensitive information.
- Uses sample or anonymized data for testing and demonstrations.
- Restricts editing functions to authorized administrators.
- Uses uploaded images only for AI building recognition within the prototype.
- Follows basic privacy, security, and ethical principles throughout development.
