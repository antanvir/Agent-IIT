global days, teachers, teacher_Id
global semester, course


greetings = {
    "hi": "Hello", "hello": "Hi", "bye": "Bye!", "okay": "Hm",
    "thanks": "Welcome!", "thank": "Welcome", "ok": "Hm",
}

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

dayName = {
    "sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4,
}

teachers = ["", "Md. Shariful Islam", "Zerina Begum", "Mohd. Zulfiquar Hafiz", "Md. Mahbubul Alam Joarder", 
    "Kazi Muheymin-Us-Sakib", "Mohommad Shoyaib", "Md. Shafiul Alam Khan", "B M Mainul Hossain", "Naushin Nower",
    "Ahmedul Kabir", "Nurul Ahad Tawhid", "Md. Saeed Siddik", "Nadia Nahar", "Abdus Sattar", "Kishan Kumar Ganguly",
    "Chandranath Poddar", "Md. Iftekharul Amin", "Kazi Mahbubur Rahman", "Muhammad Shariat Ullah", "Shahdad Hossain"]


teacher_Id = {
    "shariful": 1,  "islam": 1, "zerina": 2,    "begum": 2, "zulfiquar": 3, "hafiz": 3,
    "mahbubul": 4,  "joarder": 4,   "kazi": 5,  "sakib": 5, "muheymin": 5,  "muheymin-us-sakib": 5,
    "mohommad": 6,  "shoyaib": 6,   "shafiul": 7,   "khan": 7,  "mainul": 8,    "hossain": 8,
    "naushin": 9,   "nower": 9,	 "ahmedul": 10,  "kabir": 10,    "nurul": 11,    "ahad": 11, "tawhid": 11,
    "saeed": 12,    "siddik": 12,   "nadia": 13,    "nahar": 13,    "abdus": 14,    "sattar": 14,	"rifat": 14,
    "kishan": 15,   "kumar": 15,    "ganguly": 15,  "poddar": 16,   "iftekharul": 17,   "mahbubur": 18,
    "shariat": 19,  "shahdad": 20,
}

semester = {
    "9th": 6, '9': 6, "6": 6, "6th": 6,     "10th": 4, '10': 4, "4": 4, "4th": 4,
    "8th": 8, '8': 8, "8th": 6,             "11th": 2, '11': 2, "2": 2, "2nd": 2,
}

bloodGrouping = {
    "a+": "A+", "a-": "A-", "b+": "B+", "b-": "B-", 
    "o+": "O+", "o-": "O-", "ab+": "AB+", "ab-": "AB-",
}

course = {
    "distributed": "6|Distributed Systems", "mis": "6|Management Information Systems",
    "management": "6|Management Information Systems", "ethics": "6|Information Systems Ethics",
    "artificial": "6|Artificial Intelligence", "intelligence": "6|Artificial Intelligence",
    "ai": "6|Artificial Intelligence", "testing": "6|Software Testing And Quality Assurance",
    "assurance": "6|Software Testing And Quality Assurance", "design": "6|Software Design And Analysis",
    "analysis": "6|Software Design And Analysis",


    'metrics': "8|Software Metrics", "ml": "8|Machine Learning", "machine": "8|Machine Learning",
    'project': "8|Software Project Management", "network": "8|Computer, Data And Network Security",


    "security": "4|Information Security", "specification": "4|Software Requirements Specification And Analysis",
    "requirements": "4|Software Requirements Specification And Analysis", "srs": "4|Software Requirements Specification And Analysis",
    "bus": "4|Business Studies for Engineers", "business": "4|Business Studies for Engineers",
    "dbms": "4|Database Management System-I", "database": "4|Database Management System-I",
    "db": "4|Database Management System-I", "psychology": "4|Business Psychology",
    "operating": "4|Operating Systems And System Programming", "os": "4|Operating Systems And System Programming",
}

def initialize():
    ""


def main():
    initialize()
    print(days[1], " ", teachers[19])
    print(teacher_Id['kabir'])


if __name__ == "__main__":
    main()