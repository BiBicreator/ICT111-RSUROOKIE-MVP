import json
import math
from pathlib import Path


DB_PATH = Path(__file__).with_name("database.json")


def room(room_id, name, floor, room_type, x=160, y=110):
    return {
        "id": room_id,
        "name": name,
        "floor": floor,
        "type": room_type,
        "x": x,
        "y": y,
    }


BUILDING_SPECS = [
    {
        "id": "B1",
        "number": "1",
        "name": "Arthit Ourairat Building (Building 1)",
        "shortName": "Building 1",
        "emoji": "\U0001F3DB\uFE0F",
        "category": "Administration",
        "description": "Building 1, located at the Main Entrance Zone of RSU, serves as the central administrative headquarters of the university. Named after the founder Dr. Arthit Ourairat, it houses executive offices including the President's Office and key administrative departments responsible for academic and student services.",
        "location": "Main Entrance Zone, RSU Campus",
        "lat": 13.9295,
        "lng": 100.6068,
        "floors": 10,
        "openHours": {"Mon-Fri": "08:00-17:00", "Sat": "08:00-12:00", "Sun": "Closed"},
        "rules": [
            "Smart dress code required",
            "RSU student ID must be presented for all services",
            "Take queue numbers before service",
            "No food or drinks in office areas",
        ],
        "keywords": ["administration", "president", "office", "registration", "headquarters", "student affairs"],
        "services": [
            "President's Office (Floor 10) - University executive operations (08:30-16:30)",
            "Office of Academic Affairs - Course registration and academic records (08:30-16:30)",
            "Student Affairs Division - Student welfare and activities (08:30-16:30)",
        ],
        "facilities": [
            "ATM (Bangkok Bank) at ground floor",
            "Elevators for all floors",
            "Campus-wide Wi-Fi",
            "Central service counters",
        ],
        "clubs": [
            {
                "name": "Student Government (อบม.)",
                "schedule": "Wed 15:00",
                "meetingLocation": "Floor 4",
                "memberCount": 24,
            }
        ],
        "famousFor": ["University headquarters", "President's Office", "Main administrative hub"],
        "rooms": [
            room("B1-1-01", "Room 101 - Academic Affairs Counter", 1, "service"),
            room("B1-10-01", "Room 1001 - President's Office", 10, "office"),
        ],
    },
    {
        "id": "B2",
        "number": "2",
        "name": "Prasittirat Building (Building 2)",
        "shortName": "Building 2",
        "emoji": "\U0001F4D6",
        "category": "Academic",
        "description": "Located in the Central Zone, Building 2 houses the RSU Central Library and academic support services. It provides extensive physical and digital learning resources for students and staff.",
        "location": "Central Zone, RSU Campus",
        "lat": 13.9290,
        "lng": 100.6060,
        "floors": 4,
        "openHours": {"Mon-Fri": "08:00-20:00", "Sat": "09:00-17:00", "Sun": "Closed"},
        "rules": [
            "No food or drinks",
            "Maintain silence",
            "ID required for borrowing",
            "Store bags in lockers",
            "Return books on time",
        ],
        "keywords": ["library", "study", "books", "research", "reading", "e-book"],
        "services": [
            "Book Lending (08:00-19:30)",
            "Research Assistance (09:00-17:00)",
            "Digital Resources (24/7 online access)",
            "Study Room Booking (08:00-19:00)",
        ],
        "facilities": [
            "Computer terminals",
            "Silent study zones",
            "Discussion rooms",
            "Printing and copying services",
        ],
        "clubs": [
            {
                "name": "Reading & Research Club",
                "schedule": "Thu 16:00",
                "meetingLocation": "Library Discussion Room",
                "memberCount": 32,
            }
        ],
        "famousFor": ["Central library", "Quiet study spaces", "Digital resources"],
        "rooms": [],
    },
    {
        "id": "B3",
        "number": "3",
        "name": "Urairat Building (Building 3)",
        "shortName": "Building 3",
        "emoji": "\U0001F393",
        "category": "Faculty",
        "description": "Building 3, located in the West Zone, is a hub for humanities and social sciences. It houses the College of Liberal Arts, Faculty of Law, Political Science, and the Institute of Diplomacy.",
        "location": "West Zone, RSU Campus",
        "lat": 13.9288,
        "lng": 100.6055,
        "floors": 5,
        "openHours": {"Mon-Fri": "07:30-19:00", "Sat": "08:00-14:00", "Sun": "Closed"},
        "rules": [
            "Smart dress code for offices",
            "Quiet in lecture halls",
            "RSU ID required",
        ],
        "keywords": ["law", "political science", "diplomacy", "humanities", "international studies", "liberal arts"],
        "services": [
            "Law Faculty Office (08:30-16:30)",
            "Political Science Office (08:30-16:30)",
            "Diplomacy Institute (09:00-16:00)",
        ],
        "facilities": [
            "Lecture rooms",
            "Seminar spaces",
            "Moot court room",
            "Faculty offices",
        ],
        "clubs": [
            {
                "name": "Law Society",
                "schedule": "Fri 16:00",
                "meetingLocation": "Moot Court Room",
                "memberCount": 28,
            },
            {
                "name": "Model UN Club",
                "schedule": "Tue 17:00",
                "meetingLocation": "Seminar Room",
                "memberCount": 36,
            },
        ],
        "famousFor": ["Moot court", "Liberal arts programs", "International studies"],
        "rooms": [],
    },
    {
        "id": "B4",
        "number": "4",
        "name": "Science Building (Building 4)",
        "shortName": "Building 4",
        "emoji": "\U0001F52C",
        "category": "Faculty",
        "description": "Located in the North Zone, Building 4 supports science and health-related education, including laboratories and research facilities for multiple faculties.",
        "location": "North Zone, RSU Campus",
        "lat": 13.9298,
        "lng": 100.6065,
        "floors": 6,
        "openHours": {"Mon-Fri": "07:00-20:00", "Sat": "08:00-14:00", "Sun": "Closed"},
        "rules": [
            "Lab coat and goggles required",
            "No unauthorized chemicals",
            "Report hazards",
            "Supervised access only",
        ],
        "keywords": ["science", "lab", "chemistry", "biology", "experiment", "medical tech"],
        "services": [
            "Science Labs (07:00-19:00)",
            "Medical Technology Labs (08:00-17:00)",
            "Faculty Office (08:30-16:30)",
        ],
        "facilities": [
            "Chemistry labs",
            "Biology labs",
            "Fume hoods",
            "Lecture theaters",
        ],
        "clubs": [
            {
                "name": "Science Society RSU",
                "schedule": "Thu 15:00",
                "meetingLocation": "Seminar Room",
                "memberCount": 40,
            },
            {
                "name": "Medical Technology Club",
                "schedule": "Wed 16:00",
                "meetingLocation": "Medical Technology Lab",
                "memberCount": 26,
            },
        ],
        "famousFor": ["Science labs", "Medical technology programs"],
        "rooms": [],
    },
    {
        "id": "B5",
        "number": "5",
        "name": "Wisanuratana Building (Building 5)",
        "shortName": "Building 5",
        "emoji": "\U0001F3E5",
        "category": "Health & Welfare",
        "description": "Located in the North Zone, this building houses medical-related faculties and the RSU Health Center, providing healthcare services to students.",
        "location": "North Zone, RSU Campus",
        "lat": 13.9302,
        "lng": 100.6072,
        "floors": 5,
        "openHours": {"Mon-Fri": "07:00-20:00", "Sat": "08:00-16:00", "Sun": "Emergency only"},
        "rules": [
            "Clinical attire required",
            "ID required",
            "Emergency cases prioritized",
        ],
        "keywords": ["medical", "clinic", "doctor", "pharmacy", "health", "nursing"],
        "services": [
            "Health Center (08:00-16:30)",
            "Pharmacy (08:00-16:00)",
            "Nursing Office (08:30-16:30)",
            "Emergency First Aid (24/7)",
        ],
        "facilities": [
            "Clinical labs",
            "Pharmacy lab",
            "Consultation rooms",
            "Wheelchair access",
        ],
        "clubs": [
            {
                "name": "Nursing Volunteer Club",
                "schedule": "Wed 15:00",
                "meetingLocation": "Nursing Lab",
                "memberCount": 30,
            },
            {
                "name": "Pharmacy Club",
                "schedule": "Fri 15:00",
                "meetingLocation": "Pharmacy Lab",
                "memberCount": 22,
            },
        ],
        "famousFor": ["Health center", "Medical and nursing programs"],
        "rooms": [],
    },
    {
        "id": "B6",
        "number": "6",
        "name": "Main Cafeteria (Building 6)",
        "shortName": "Building 6",
        "emoji": "\U0001F37D\uFE0F",
        "category": "Dining",
        "description": "Building 6, located in the Central Zone, is the main dining area of RSU, offering a variety of food options and serving as a social hub for students.",
        "location": "Central Zone, RSU Campus",
        "lat": 13.9284,
        "lng": 100.6062,
        "floors": 2,
        "openHours": {"Mon-Fri": "06:30-20:00", "Sat": "07:00-16:00", "Sun": "07:00-14:00"},
        "rules": [
            "Clean up after use",
            "No smoking",
            "No outside vendors",
            "Priority seating for disabled persons",
        ],
        "keywords": ["food", "cafeteria", "dining", "drink", "coffee", "canteen"],
        "services": [
            "Thai Food Stalls",
            "International Food",
            "Coffee & Beverages",
            "Meal Card Payment",
        ],
        "facilities": [
            "Indoor seating",
            "Outdoor seating",
            "Wi-Fi",
            "ATM",
        ],
        "clubs": [
            {
                "name": "Culinary & Food Culture Club",
                "schedule": "Sat 10:00",
                "meetingLocation": "Demo Kitchen",
                "memberCount": 18,
            }
        ],
        "famousFor": ["Main food hub", "Affordable meals"],
        "rooms": [],
    },
    {
        "id": "B7",
        "number": "7",
        "name": "Faculty of Engineering (Building 7)",
        "shortName": "Building 7",
        "emoji": "\u2699\uFE0F",
        "category": "Faculty",
        "description": "Located in the East Zone, Building 7 houses engineering and biomedical engineering programs, featuring advanced labs and workshops.",
        "location": "East Zone, RSU Campus",
        "lat": 13.9280,
        "lng": 100.6080,
        "floors": 6,
        "openHours": {"Mon-Fri": "07:30-20:00", "Sat": "08:00-14:00", "Sun": "Closed"},
        "rules": [
            "Safety equipment required",
            "ID required",
            "No food in labs",
            "Advance booking required",
        ],
        "keywords": ["engineering", "robotics", "lab", "fabrication", "coding", "biomedical"],
        "services": [
            "Lab Reservation (08:00-18:00)",
            "Equipment Loan (09:00-17:00)",
            "Academic Advising",
            "Fabrication Support",
        ],
        "facilities": [
            "Computer labs",
            "Electronics workshop",
            "3D printing lab",
            "Biomedical lab",
        ],
        "clubs": [
            {
                "name": "Robotics Club",
                "schedule": "Tue & Thu 17:00",
                "meetingLocation": "Robotics Lab",
                "memberCount": 42,
            },
            {
                "name": "IEEE Student Branch",
                "schedule": "1st Wed monthly 17:00",
                "meetingLocation": "Room 201",
                "memberCount": 24,
            },
            {
                "name": "Maker Space Club",
                "schedule": "Sat 10:00",
                "meetingLocation": "Fabrication Room",
                "memberCount": 20,
            },
        ],
        "famousFor": ["Engineering labs", "Robotics", "3D printing"],
        "rooms": [],
    },
    {
        "id": "B8",
        "number": "8",
        "name": "Faculty of Architecture & Design (Building 8)",
        "shortName": "Building 8",
        "emoji": "\U0001F3D7\uFE0F",
        "category": "Faculty",
        "description": "Building 8, located in the East Zone of the RSU campus, houses the Faculty of Architecture, College of Design, and Faculty of Digital Art. It is a creative hub featuring open studios, workshops, and digital labs where students work on design, architecture, and multimedia projects.",
        "location": "East Zone, RSU Campus",
        "lat": 13.9278,
        "lng": 100.6075,
        "floors": 5,
        "openHours": {"Mon-Fri": "07:30-21:00", "Sat": "08:00-18:00", "Sun": "By arrangement"},
        "rules": [
            "Design studio access requires RSU ID",
            "Studios must be kept clean",
            "All equipment must be returned after use",
            "Laser cutters and CNC machines require supervision",
        ],
        "keywords": ["architecture", "design", "art", "studio", "digital art", "3D modeling", "blueprint", "creative"],
        "services": [
            "Design Studios - Open workspace for drafting and projects (07:30-21:00)",
            "Model Workshop - Tools for physical model building (08:00-18:00)",
            "Digital Media Lab - Mac computers with Adobe and 3D software (08:00-20:00)",
        ],
        "facilities": [
            "Architecture studios",
            "Laser cutter (supervised)",
            "Digital art lab",
            "Exhibition and gallery space for student work",
        ],
        "clubs": [
            {
                "name": "Architecture Society RSU",
                "schedule": "Fri 17:00",
                "meetingLocation": "Main Studio",
                "memberCount": 26,
            },
            {
                "name": "Digital Art & Animation Club",
                "schedule": "Wed 17:00",
                "meetingLocation": "Digital Lab",
                "memberCount": 30,
            },
        ],
        "famousFor": ["Architecture programs", "Digital art labs", "Annual design exhibitions"],
        "rooms": [],
    },
    {
        "id": "B9",
        "number": "9",
        "name": "Music & Communication Arts (Building 9)",
        "shortName": "Building 9",
        "emoji": "\U0001F3B5",
        "category": "Faculty",
        "description": "Located in the Central-East Zone, Building 9 houses the Conservatory of Music and College of Communication Arts. It includes professional practice rooms, studios, and media production facilities.",
        "location": "Central-East Zone, RSU Campus",
        "lat": 13.9282,
        "lng": 100.6078,
        "floors": 4,
        "openHours": {"Mon-Fri": "08:00-20:00", "Sat": "08:00-17:00", "Sun": "Closed"},
        "rules": [
            "Practice rooms must be booked",
            "Maintain reasonable noise levels",
            "RSU ID required for access",
        ],
        "keywords": ["music", "recording", "film", "media", "broadcasting", "performance"],
        "services": [
            "Music Office - Advising and recital booking",
            "Communication Arts Office - Media programs",
            "Dormitory Office (9B, Floor 2) - Housing services",
        ],
        "facilities": [
            "Soundproof practice rooms",
            "Recording studio",
            "Media production labs",
            "Practice halls",
        ],
        "clubs": [
            {
                "name": "RSU Music Club",
                "schedule": "Mon & Wed 18:00",
                "meetingLocation": "Practice Hall",
                "memberCount": 34,
            },
            {
                "name": "Film & Media Club",
                "schedule": "Fri 16:00",
                "meetingLocation": "Media Lab",
                "memberCount": 28,
            },
        ],
        "famousFor": ["Music conservatory", "Recording studios", "Performance training"],
        "rooms": [],
    },
    {
        "id": "B10",
        "number": "10",
        "name": "Radiology & Parking (Building 10)",
        "shortName": "Building 10",
        "emoji": "\U0001F506",
        "category": "Faculty",
        "description": "Located in the North-East Zone, this building supports radiological technology education and campus parking.",
        "location": "North-East Zone, RSU Campus",
        "lat": 13.9300,
        "lng": 100.6080,
        "floors": 4,
        "openHours": {"Mon-Fri": "07:30-18:00", "Sat": "08:00-14:00", "Sun": "Closed"},
        "rules": [
            "Clinical attire required",
            "Strict radiation safety",
            "Parking requires RSU permit",
        ],
        "keywords": ["radiology", "imaging", "x-ray", "parking", "medical", "diagnostic"],
        "services": [
            "Radiology Office",
            "Campus Parking",
        ],
        "facilities": [
            "Diagnostic imaging lab",
            "Multi-level parking structure",
            "Radiology classrooms",
            "Student service desk",
        ],
        "clubs": [
            {
                "name": "Radiological Technology Society",
                "schedule": "Thu 15:00",
                "meetingLocation": "Seminar Room",
                "memberCount": 18,
            }
        ],
        "famousFor": ["Imaging labs", "Parking hub"],
        "rooms": [],
    },
    {
        "id": "B11",
        "number": "11",
        "name": "Business & Economics (Building 11)",
        "shortName": "Building 11",
        "emoji": "\U0001F4BC",
        "category": "Faculty",
        "description": "Located in the West Zone, this building hosts business, accounting, economics, and education faculties.",
        "location": "West Zone, RSU Campus",
        "lat": 13.9286,
        "lng": 100.6050,
        "floors": 5,
        "openHours": {"Mon-Fri": "07:30-19:00", "Sat": "08:00-14:00", "Sun": "Closed"},
        "rules": [
            "Business attire encouraged",
            "RSU ID required",
            "Quiet environment",
        ],
        "keywords": ["business", "finance", "accounting", "economics", "management", "education"],
        "services": [
            "Business Office",
            "Accounting Office",
            "Economics Advising",
        ],
        "facilities": [
            "Finance lab (Bloomberg)",
            "Seminar rooms",
            "Lecture halls",
            "Faculty offices",
        ],
        "clubs": [
            {
                "name": "Business Club",
                "schedule": "Wed 17:00",
                "meetingLocation": "Seminar Room",
                "memberCount": 35,
            },
            {
                "name": "Accounting & Finance Society",
                "schedule": "Thu 16:00",
                "meetingLocation": "Finance Lab",
                "memberCount": 26,
            },
        ],
        "famousFor": ["Business programs", "Bloomberg terminal"],
        "rooms": [],
    },
    {
        "id": "B12",
        "number": "12",
        "name": "Dormitory Complex (Building 12)",
        "shortName": "Building 12",
        "emoji": "\U0001F3E8",
        "category": "Residential & Services",
        "description": "Located in the South Zone, this is the main student housing complex with four 12-floor towers.",
        "location": "South Zone, RSU Campus",
        "lat": 13.9272,
        "lng": 100.6060,
        "floors": 12,
        "openHours": {"Dormitory": "24/7", "Office": "Mon-Fri 08:30-16:30"},
        "rules": [
            "ID required",
            "No opposite gender after 22:00",
            "No cooking",
            "Quiet hours enforced",
        ],
        "keywords": ["dorm", "housing", "residence", "accommodation", "student housing", "laundry"],
        "services": [
            "Student Housing",
            "Laundry",
            "Convenience Kiosk",
        ],
        "facilities": [
            "Dorm towers",
            "Laundry machines",
            "Lounges",
            "Security systems",
        ],
        "clubs": [],
        "famousFor": ["On-campus living", "12-floor towers"],
        "rooms": [],
    },
    {
        "id": "B13",
        "number": "13",
        "name": "Facilities Office (Building 13)",
        "shortName": "Building 13",
        "emoji": "\U0001F527",
        "category": "Facilities & Services",
        "description": "Located in the Service Zone, this building manages campus maintenance and environmental services.",
        "location": "Service Zone, RSU Campus",
        "lat": 13.9268,
        "lng": 100.6058,
        "floors": 2,
        "openHours": {"Mon-Fri": "07:00-17:00", "Sat": "07:00-12:00", "Sun": "Closed"},
        "rules": [
            "Restricted access",
            "Report issues via system",
        ],
        "keywords": ["maintenance", "repair", "facilities", "operations", "environment", "services"],
        "services": [
            "Maintenance",
            "Environmental Management",
        ],
        "facilities": [
            "Operations office",
            "Maintenance desk",
            "Service counter",
            "Storage area",
        ],
        "clubs": [],
        "famousFor": ["Campus operations"],
        "rooms": [],
    },
    {
        "id": "B14",
        "number": "14",
        "name": "Recreation Building (Building 14)",
        "shortName": "Building 14",
        "emoji": "\U0001F3CB\uFE0F",
        "category": "Sports & Recreation",
        "description": "Located in the South Zone, this is the main sports complex with gym, pool, and courts.",
        "location": "South Zone, RSU Campus",
        "lat": 13.9270,
        "lng": 100.6070,
        "floors": 3,
        "openHours": {"Mon-Fri": "06:00-21:00", "Sat": "07:00-19:00", "Sun": "08:00-17:00"},
        "rules": [
            "Sports attire required",
            "ID required",
            "Booking needed",
        ],
        "keywords": ["sports", "gym", "fitness", "swimming", "pool", "courts"],
        "services": [
            "Gym",
            "Pool",
            "Courts",
            "Therapy Clinic",
            "Fitness Classes",
        ],
        "facilities": [
            "Pool",
            "Courts",
            "Gym",
            "Lockers",
            "First aid",
        ],
        "clubs": [
            {
                "name": "Basketball Club",
                "schedule": "Tue & Thu 18:00",
                "meetingLocation": "Court A",
                "memberCount": 34,
            },
            {
                "name": "Swimming Club",
                "schedule": "Mon & Wed 06:30",
                "meetingLocation": "Pool Deck",
                "memberCount": 22,
            },
            {
                "name": "Muay Thai Club",
                "schedule": "Mon/Wed/Fri 17:00",
                "meetingLocation": "Training Hall",
                "memberCount": 20,
            },
            {
                "name": "Football Club",
                "schedule": "Tue/Thu/Sat 17:00",
                "meetingLocation": "Outdoor Field",
                "memberCount": 28,
            },
            {
                "name": "Yoga Club",
                "schedule": "Sat 09:00",
                "meetingLocation": "Studio",
                "memberCount": 16,
            },
        ],
        "famousFor": ["Sports complex", "Swimming pool"],
        "rooms": [],
    },
    {
        "id": "B15",
        "number": "15",
        "name": "Digital Multimedia Complex (Building 15)",
        "shortName": "Building 15",
        "emoji": "\U0001F4BB",
        "category": "Faculty",
        "description": "Located in the East Zone, this building is the center for IT and digital innovation.",
        "location": "East Zone, RSU Campus",
        "lat": 13.9276,
        "lng": 100.6082,
        "floors": 5,
        "openHours": {"Mon-Fri": "07:30-21:00", "Sat": "08:00-17:00", "Sun": "Closed"},
        "rules": [
            "No food near computers",
            "ID required",
        ],
        "keywords": ["IT", "coding", "AI", "cybersecurity", "digital", "innovation"],
        "services": [
            "IT Office",
            "Computer Labs",
            "Cybersecurity Labs",
        ],
        "facilities": [
            "Computer labs",
            "Server rooms",
            "Innovation studios",
            "Digital project spaces",
        ],
        "clubs": [
            {
                "name": "Coding Club",
                "schedule": "Mon 18:00",
                "meetingLocation": "Computer Lab",
                "memberCount": 38,
            },
            {
                "name": "Cybersecurity Club",
                "schedule": "Wed 17:00",
                "meetingLocation": "Cybersecurity Lab",
                "memberCount": 24,
            },
            {
                "name": "Game Dev Club",
                "schedule": "Fri 17:00",
                "meetingLocation": "Innovation Studio",
                "memberCount": 21,
            },
        ],
        "famousFor": ["DMC", "Tech innovation"],
        "rooms": [],
    },
    {
        "id": "B16",
        "number": "16",
        "name": "Prototype Factory (Building 16)",
        "shortName": "Building 16",
        "emoji": "\U0001F3ED",
        "category": "Facilities & Services",
        "description": "Located in the South-East Zone, this building supports engineering fabrication and prototyping.",
        "location": "South-East Zone, RSU Campus",
        "lat": 13.9265,
        "lng": 100.6077,
        "floors": 2,
        "openHours": {"Mon-Fri": "08:00-17:00", "Sat": "08:00-12:00", "Sun": "Closed"},
        "rules": [
            "Safety gear required",
            "Supervised access",
        ],
        "keywords": ["factory", "prototype", "workshop", "fabrication", "engineering", "machinery"],
        "services": [
            "Prototype Workshop",
            "Vehicle Services",
        ],
        "facilities": [
            "Machine workshop",
            "Welding stations",
            "Fabrication area",
            "Service bay",
        ],
        "clubs": [],
        "famousFor": ["Engineering fabrication"],
        "rooms": [],
    },
    {
        "id": "B17",
        "number": "17",
        "name": "Suriyathep Music Hall (Building 17)",
        "shortName": "Building 17",
        "emoji": "\U0001F3AD",
        "category": "Arts & Culture",
        "description": "Building 17, known as the Suriyathep Music Hall, is located in the Central Zone of RSU. It is the university's premier performance venue, hosting concerts, recitals, ceremonies, and cultural events. The hall serves as a landmark for arts and culture, frequently used for graduation rehearsals and major university functions.",
        "location": "Central Zone, RSU Campus",
        "lat": 13.9285,
        "lng": 100.6057,
        "floors": 3,
        "openHours": {"Events": "As scheduled", "Rehearsals": "By appointment"},
        "rules": [
            "Entry allowed only during scheduled events or rehearsals",
            "No food or drinks inside the hall",
            "Maintain silence during performances",
            "Smart dress required for formal events",
        ],
        "keywords": ["music hall", "performance", "concert", "theater", "stage", "ceremony", "auditorium", "recital", "event"],
        "services": [
            "Concert & Event Hosting - Venue for performances and ceremonies (event schedule)",
            "Rehearsal Space Booking - Available through student affairs (by appointment)",
        ],
        "facilities": [
            "Main auditorium with full audiovisual system",
            "Backstage area",
            "Green room",
            "Professional sound and lighting systems",
        ],
        "clubs": [
            {
                "name": "RSU Performing Arts Club",
                "schedule": "Rehearsals as scheduled",
                "meetingLocation": "Auditorium",
                "memberCount": 25,
            }
        ],
        "famousFor": ["RSU's main concert hall", "Graduation ceremonies", "Conservatory performances"],
        "rooms": [],
    },
    {
        "id": "B18",
        "number": "18",
        "name": "College of Tourism & Hospitality (Building 18)",
        "shortName": "Building 18",
        "emoji": "\u2708\uFE0F",
        "category": "Faculty",
        "description": "Building 18, located in the West-South Zone, houses the College of Tourism and Hospitality Industry and the Aviation Institute. It provides hands-on training environments including simulated hotel and airline facilities, preparing students for careers in tourism, hospitality, and aviation industries.",
        "location": "West-South Zone, RSU Campus",
        "lat": 13.9275,
        "lng": 100.6053,
        "floors": 4,
        "openHours": {"Mon-Fri": "07:30-18:00", "Sat": "08:00-14:00", "Sun": "Closed"},
        "rules": [
            "Professional appearance required on uniform days",
            "RSU ID required",
            "Handle training equipment carefully",
        ],
        "keywords": ["tourism", "hospitality", "hotel", "travel", "aviation", "airline", "cabin crew", "service", "restaurant"],
        "services": [
            "Tourism College Office - Program advising and academic services (08:30-16:30)",
            "Aviation Institute - Aviation-related programs including cabin crew and aviation management (08:30-16:30)",
        ],
        "facilities": [
            "Training restaurant",
            "Hotel front desk simulation area",
            "Aviation training room",
            "Hospitality practice labs",
        ],
        "clubs": [
            {
                "name": "RSU Tourism & Travel Club",
                "schedule": "Fri 16:00",
                "meetingLocation": "Seminar Room",
                "memberCount": 23,
            },
            {
                "name": "Aviation Club",
                "schedule": "Thu 17:00",
                "meetingLocation": "Aviation Room",
                "memberCount": 19,
            },
        ],
        "famousFor": ["Tourism and hospitality training", "Aviation institute", "Cabin crew preparation programs"],
        "rooms": [],
    },
    {
        "id": "B19",
        "number": "19",
        "name": "Agricultural Innovation & Biotechnology (Building 19)",
        "shortName": "Building 19",
        "emoji": "\U0001F33F",
        "category": "Faculty",
        "description": "Building 19, located in the North-West Zone, houses the College of Agricultural Innovation, Biotechnology, and Food Technology. It focuses on modern agriculture, food science, and biotechnology research, integrating laboratory work with real-world agricultural practices.",
        "location": "North-West Zone, RSU Campus",
        "lat": 13.9305,
        "lng": 100.6055,
        "floors": 4,
        "openHours": {"Mon-Fri": "07:30-18:00", "Sat": "08:00-14:00", "Sun": "Closed"},
        "rules": [
            "Lab coat required in laboratories",
            "No eating in lab areas",
            "Greenhouse users must ensure all vents and doors are properly closed after use",
        ],
        "keywords": ["agriculture", "biotechnology", "food science", "greenhouse", "farming", "sustainability", "food lab"],
        "services": [
            "AgriFood College Office - Academic advising and program support (08:30-16:30)",
            "Food Technology Lab - Food processing and quality testing (08:00-17:00)",
            "Biotechnology Research Lab - Research on plants and microorganisms (08:00-17:00)",
        ],
        "facilities": [
            "Greenhouse with climate control",
            "Food technology lab",
            "Biotechnology lab with PCR and lab equipment",
            "Experimental agricultural plots",
        ],
        "clubs": [
            {
                "name": "RSU Green & Sustainable Club",
                "schedule": "Sat 09:00",
                "meetingLocation": "Greenhouse",
                "memberCount": 22,
            },
            {
                "name": "Food Innovation Club",
                "schedule": "Wed 15:00",
                "meetingLocation": "Food Lab",
                "memberCount": 18,
            },
        ],
        "famousFor": ["Agricultural innovation", "Biotechnology research", "Food technology labs", "Sustainability programs"],
        "rooms": [],
    },
]


POSITIONS = {
    "B1": (80, 70),
    "B2": (240, 70),
    "B3": (400, 70),
    "B4": (560, 70),
    "B5": (720, 70),
    "B6": (80, 180),
    "B7": (240, 180),
    "B8": (400, 180),
    "B9": (560, 180),
    "B10": (720, 180),
    "B11": (80, 300),
    "B12": (240, 300),
    "B13": (400, 300),
    "B14": (560, 300),
    "B15": (720, 300),
    "B16": (80, 410),
    "B17": (240, 410),
    "B18": (400, 410),
    "B19": (560, 410),
}


def convert(spec):
    return {
        "id": spec["id"],
        "number": spec["number"],
        "name": spec["name"],
        "shortName": spec["shortName"],
        "emoji": spec["emoji"],
        "category": spec["category"],
        "description": spec["description"],
        "location": spec["location"],
        "lat": spec["lat"],
        "lng": spec["lng"],
        "floors": spec["floors"],
        "openHours": spec["openHours"],
        "rules": spec["rules"],
        "keywords": spec["keywords"],
        "services": spec["services"],
        "facilities": spec["facilities"],
        "clubs": spec["clubs"],
        "famousFor": spec["famousFor"],
        "rooms": spec["rooms"],
    }


def build_navigation(buildings):
    nodes = [
        {
            "id": "N_CAMPUS_HUB",
            "label": "Campus Central Hub",
            "building": None,
            "floor": 0,
            "x": 410,
            "y": 240,
            "type": "outdoor_intersection",
        }
    ]
    edges = []
    edge_num = 1

    def add_edge(frm, to, weight, edge_type="outdoor", floor_change=False):
        nonlocal edge_num
        edge = {"id": f"E{edge_num:03d}", "from": frm, "to": to, "weight": int(weight), "type": edge_type}
        if floor_change:
            edge["floorChange"] = True
        edges.append(edge)
        edge_num += 1

    for bid, building in buildings.items():
        x, y = POSITIONS[bid]
        entry_id = f"N_{bid}_ENTRY"
        nodes.append(
            {
                "id": entry_id,
                "label": f"{building['shortName']} Entrance",
                "building": bid,
                "floor": 1,
                "x": x,
                "y": y,
                "type": "entrance",
            }
        )
        add_edge("N_CAMPUS_HUB", entry_id, max(25, round(math.hypot(x - 410, y - 240) / 2.8)))

        if not building["rooms"]:
            continue

        lift_id = f"N_{bid}_LIFT1"
        nodes.append(
            {
                "id": lift_id,
                "label": f"{building['shortName']} Lift",
                "building": bid,
                "floor": 1,
                "x": x,
                "y": y - 34,
                "type": "lift",
            }
        )
        add_edge(entry_id, lift_id, 12, "indoor_walk")

        for index, room_data in enumerate(building["rooms"], start=1):
            node_id = f"N_{bid}_ROOM_{index:02d}"
            nodes.append(
                {
                    "id": node_id,
                    "label": room_data["name"],
                    "building": bid,
                    "floor": room_data["floor"],
                    "x": room_data["x"],
                    "y": room_data["y"],
                    "type": "room",
                    "roomID": room_data["id"],
                }
            )
            if room_data["floor"] > 1:
                add_edge(lift_id, node_id, 10 + room_data["floor"], "lift", True)
            else:
                add_edge(entry_id, node_id, 14 + index, "indoor_walk")

    rows = [
        ["B1", "B2", "B3", "B4", "B5"],
        ["B6", "B7", "B8", "B9", "B10"],
        ["B11", "B12", "B13", "B14", "B15"],
        ["B16", "B17", "B18", "B19"],
    ]
    cols = [
        ["B1", "B6", "B11", "B16"],
        ["B2", "B7", "B12", "B17"],
        ["B3", "B8", "B13", "B18"],
        ["B4", "B9", "B14", "B19"],
        ["B5", "B10", "B15"],
    ]

    for group in rows + cols:
        for left, right in zip(group, group[1:]):
            lx, ly = POSITIONS[left]
            rx, ry = POSITIONS[right]
            add_edge(f"N_{left}_ENTRY", f"N_{right}_ENTRY", max(28, round(math.hypot(lx - rx, ly - ry) / 2.8)))

    return {
        "_comment": "Navigation graph for the RSU campus dataset. Building entrance routing works for all buildings; room routing works where room data exists.",
        "nodes": nodes,
        "edges": edges,
    }


def main():
    db = json.loads(DB_PATH.read_text(encoding="utf-8"))
    buildings = {spec["id"]: convert(spec) for spec in BUILDING_SPECS}
    db["buildings"] = buildings
    db["navigation"] = build_navigation(buildings)
    db["teachable_machine"]["labels"] = {
        "_comment": "Map your Teachable Machine class names to building IDs",
        "Building 1": "B1",
        "Arthit Ourairat Building": "B1",
        "Library": "B2",
        "Prasittirat Building": "B2",
        "Urairat Building": "B3",
        "Science Building": "B4",
        "Wisanuratana Building": "B5",
        "Main Cafeteria": "B6",
        "Engineering": "B7",
        "Architecture": "B8",
        "Music & Communication Arts": "B9",
        "Radiology": "B10",
        "Business & Economics": "B11",
        "Dormitory": "B12",
        "Facilities Office": "B13",
        "Recreation Building": "B14",
        "Digital Multimedia Complex": "B15",
        "Prototype Factory": "B16",
        "Suriyathep Music Hall": "B17",
        "Tourism & Hospitality": "B18",
        "Agricultural Innovation & Biotechnology": "B19",
    }
    DB_PATH.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
