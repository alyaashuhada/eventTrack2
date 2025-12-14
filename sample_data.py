#!/usr/bin/env python3
"""
Sample data generator for the University Information System.
This script populates the database with sample data for testing.
"""

from datetime import datetime, timedelta
from database import DatabaseManager
from models import Student, Course, Event, Faculty, Department


def generate_sample_data():
    """Generate and insert sample data into the database."""
    db = DatabaseManager()
    
    print("Generating sample data for University Information System...")
    
    # Add Departments
    print("\n1. Adding departments...")
    departments = [
        Department("CS", "Computer Science", "Dr. Alan Turing", "Tech Building A", "cs@university.edu"),
        Department("MATH", "Mathematics", "Dr. Emmy Noether", "Science Building B", "math@university.edu"),
        Department("ENG", "Engineering", "Dr. Nikola Tesla", "Engineering Complex", "eng@university.edu"),
        Department("BIO", "Biology", "Dr. Jane Goodall", "Life Sciences Building", "bio@university.edu"),
        Department("ARTS", "Arts & Humanities", "Dr. Maya Angelou", "Arts Center", "arts@university.edu")
    ]
    
    for dept in departments:
        if db.add_department(dept):
            print(f"  ✓ Added department: {dept.name}")
        else:
            print(f"  ✗ Department {dept.name} already exists")
    
    # Add Faculty
    print("\n2. Adding faculty members...")
    faculty = [
        Faculty("F001", "Dr. Alice Johnson", "alice.johnson@university.edu", "Computer Science", "Professor", "2015-08-15"),
        Faculty("F002", "Dr. Bob Smith", "bob.smith@university.edu", "Computer Science", "Associate Professor", "2018-01-10"),
        Faculty("F003", "Dr. Carol Williams", "carol.williams@university.edu", "Mathematics", "Professor", "2012-09-01"),
        Faculty("F004", "Dr. David Brown", "david.brown@university.edu", "Engineering", "Assistant Professor", "2020-08-20"),
        Faculty("F005", "Dr. Emma Davis", "emma.davis@university.edu", "Biology", "Professor", "2014-02-15"),
        Faculty("F006", "Dr. Frank Miller", "frank.miller@university.edu", "Arts & Humanities", "Associate Professor", "2017-06-01")
    ]
    
    for member in faculty:
        if db.add_faculty(member):
            print(f"  ✓ Added faculty: {member.name}")
        else:
            print(f"  ✗ Faculty {member.name} already exists")
    
    # Add Courses
    print("\n3. Adding courses...")
    courses = [
        Course("CS101", "Introduction to Programming", "Computer Science", 3, "Dr. Alice Johnson", "Fall 2024"),
        Course("CS201", "Data Structures", "Computer Science", 4, "Dr. Bob Smith", "Fall 2024"),
        Course("CS301", "Algorithms", "Computer Science", 4, "Dr. Alice Johnson", "Spring 2025"),
        Course("MATH101", "Calculus I", "Mathematics", 4, "Dr. Carol Williams", "Fall 2024"),
        Course("MATH201", "Linear Algebra", "Mathematics", 3, "Dr. Carol Williams", "Spring 2025"),
        Course("ENG101", "Engineering Fundamentals", "Engineering", 3, "Dr. David Brown", "Fall 2024"),
        Course("ENG202", "Circuit Design", "Engineering", 4, "Dr. David Brown", "Spring 2025"),
        Course("BIO101", "General Biology", "Biology", 4, "Dr. Emma Davis", "Fall 2024"),
        Course("ART101", "Art History", "Arts & Humanities", 3, "Dr. Frank Miller", "Fall 2024"),
    ]
    
    for course in courses:
        if db.add_course(course):
            print(f"  ✓ Added course: {course.name}")
        else:
            print(f"  ✗ Course {course.name} already exists")
    
    # Add Students
    print("\n4. Adding students...")
    students = [
        Student("S001", "John Doe", "john.doe@student.edu", "Computer Science", 2, "2023-09-01"),
        Student("S002", "Jane Smith", "jane.smith@student.edu", "Computer Science", 3, "2022-09-01"),
        Student("S003", "Michael Johnson", "michael.j@student.edu", "Mathematics", 1, "2024-09-01"),
        Student("S004", "Emily Williams", "emily.w@student.edu", "Engineering", 2, "2023-09-01"),
        Student("S005", "David Brown", "david.b@student.edu", "Biology", 4, "2021-09-01"),
        Student("S006", "Sarah Davis", "sarah.d@student.edu", "Computer Science", 1, "2024-09-01"),
        Student("S007", "Robert Taylor", "robert.t@student.edu", "Mathematics", 3, "2022-09-01"),
        Student("S008", "Lisa Anderson", "lisa.a@student.edu", "Arts & Humanities", 2, "2023-09-01"),
        Student("S009", "James Wilson", "james.w@student.edu", "Engineering", 3, "2022-09-01"),
        Student("S010", "Maria Garcia", "maria.g@student.edu", "Biology", 1, "2024-09-01")
    ]
    
    for student in students:
        if db.add_student(student):
            print(f"  ✓ Added student: {student.name}")
        else:
            print(f"  ✗ Student {student.name} already exists")
    
    # Add Events
    print("\n5. Adding events...")
    base_date = datetime.now()
    events = [
        Event("EVT001", "Fall Semester Orientation", "Welcome event for new students", 
              (base_date - timedelta(days=30)).strftime("%Y-%m-%d"), "Main Auditorium", 
              "Student Affairs", "Academic"),
        Event("EVT002", "Computer Science Hackathon", "24-hour coding competition",
              (base_date + timedelta(days=15)).strftime("%Y-%m-%d"), "CS Building Lab",
              "CS Department", "Academic"),
        Event("EVT003", "University Career Fair", "Meet potential employers",
              (base_date + timedelta(days=30)).strftime("%Y-%m-%d"), "Sports Complex",
              "Career Services", "Career"),
        Event("EVT004", "Annual Science Symposium", "Student research presentations",
              (base_date + timedelta(days=45)).strftime("%Y-%m-%d"), "Science Building",
              "Research Department", "Academic"),
        Event("EVT005", "Basketball Tournament", "Inter-department sports competition",
              (base_date + timedelta(days=20)).strftime("%Y-%m-%d"), "Sports Arena",
              "Athletics Department", "Sports"),
        Event("EVT006", "Cultural Night", "Celebration of diversity and culture",
              (base_date + timedelta(days=60)).strftime("%Y-%m-%d"), "Student Center",
              "Student Union", "Cultural"),
        Event("EVT007", "Guest Lecture: AI in Healthcare", "Industry expert presentation",
              (base_date + timedelta(days=10)).strftime("%Y-%m-%d"), "Tech Auditorium",
              "CS Department", "Academic")
    ]
    
    for event in events:
        if db.add_event(event):
            print(f"  ✓ Added event: {event.name}")
        else:
            print(f"  ✗ Event {event.name} already exists")
    
    # Enroll students in courses
    print("\n6. Enrolling students in courses...")
    enrollments = [
        ("S001", "CS101"),
        ("S001", "MATH101"),
        ("S002", "CS201"),
        ("S002", "CS301"),
        ("S003", "MATH101"),
        ("S003", "CS101"),
        ("S004", "ENG101"),
        ("S004", "MATH101"),
        ("S005", "BIO101"),
        ("S006", "CS101"),
        ("S007", "MATH201"),
        ("S008", "ART101"),
        ("S009", "ENG202"),
        ("S010", "BIO101")
    ]
    
    enrollment_date = datetime.now().strftime("%Y-%m-%d")
    for student_id, course_id in enrollments:
        if db.enroll_student(student_id, course_id, enrollment_date):
            print(f"  ✓ Enrolled {student_id} in {course_id}")
        else:
            print(f"  ✗ Failed to enroll {student_id} in {course_id}")
    
    print("\n✓ Sample data generation complete!")
    print("\nDatabase now contains:")
    print(f"  - {len(departments)} departments")
    print(f"  - {len(faculty)} faculty members")
    print(f"  - {len(courses)} courses")
    print(f"  - {len(students)} students")
    print(f"  - {len(events)} events")
    print(f"  - {len(enrollments)} course enrollments")


if __name__ == "__main__":
    generate_sample_data()
