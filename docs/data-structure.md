# Data Structure

## Project Title

RSU Campus Buddy (Smart Campus Chatbot for Student Services with Image Recognition)

---

## 1. Main Data Entities / Tables

| Entity / Table | Purpose | Example Records |
|---|---|---|
| Campus | Store general information about Rangsit University. | RSU |
| Buildings | Store detailed information about each campus building, including services, facilities, clubs, rooms, and operating hours. | Building 1, Building 2 |
| Navigation | Store predefined navigation routes between campus buildings. | Building 1 → Building 2 |
| Teachable Machine | Store the Google Teachable Machine model information used for image recognition. | Model URL, Labels |

---

## 2. Field Definition

| Entity | Field Name | Data Type | Required? | Example Value | Validation Rule | Used For Search/Filter? |
|---|---|---|---|---|---|---|
| Campus | id | String | Yes | RSU | Must be unique | No |
| Campus | name | String | Yes | Rangsit University | Cannot be empty | No |
| Campus | description | String | Yes | Private research university | No |
| Campus | lat | Number | Yes | 13.9653 | Valid latitude | No |
| Campus | lng | Number | Yes | 100.5873 | Valid longitude | No |
| Building | id | String | Yes | B1 | Must be unique | Yes |
| Building | number | String | Yes | 1 | Cannot be empty | Yes |
| Building | name | String | Yes | Arthit Ourairat Building | Cannot be empty | Yes |
| Building | shortName | String | Yes | Building 1 | Cannot be empty | Yes |
| Building | category | String | Yes | Academic | Predefined category | Yes |
| Building | description | String | Yes | Academic building | Cannot be empty | No |
| Building | location | String | Yes | North Campus | Cannot be empty | Yes |
| Building | floors | Integer | Yes | 7 | Positive number | No |
| Building | openHours | String | Yes | 08:00–17:00 | Valid time format | No |
| Building | services | Array | Yes | Student Service Center | Optional multiple values | Yes |
| Building | facilities | Array | Yes | Library, Computer Lab | Optional multiple values | Yes |
| Building | clubs | Array | No | ICT Club | Optional | Yes |
| Building | famousFor | String | No | Engineering Faculty | Optional | Yes |
| Building | rooms | Array | No | Room 101 | Optional | Yes |
| Navigation | from | String | Yes | B1 | Existing building ID | Yes |
| Navigation | to | String | Yes | B2 | Existing building ID | Yes |
| Navigation | route | Array | Yes | Walkway A | Valid route | No |
| Teachable Machine | model_url | String | Yes | https://... | Valid URL | No |
| Teachable Machine | labels | Array | Yes | Building 1, Building 2 | At least one label | Yes |

---

## 3. Status Values

The current prototype does not use record status values (such as Pending or Completed). Building information is managed directly by the administrator.

| Status | Meaning | Who Can Update? |
|---|---|---|
| Active | Building information is available to users. | Admin |
| Updated | Building information has been modified. | Admin |
| Archived | Building information is hidden but retained in the system. | Admin |

---

## 4. Sample Records

The prototype uses JSON files as the sample dataset.

Dataset location:
- `/data/campus_data.json`

The dataset contains:
- Campus information
- Building information
- Facilities and services
- Student clubs
- Operating hours
- Navigation data
- Google Teachable Machine configuration

This JSON dataset is the equivalent sample dataset used by the prototype.

---

## 5. Data Privacy Note

The prototype does not collect personal information such as student names, student IDs, email addresses, phone numbers, or passwords. The system stores only campus-related information created by the project team. All sample data is used solely for educational purposes.
