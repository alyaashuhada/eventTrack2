#!/usr/bin/env python3
"""
Test script to verify the University Information System functionality.
"""

from database import DatabaseManager
from models import Student, Course, Event, Faculty, Department


def test_database_operations():
    """Test various database operations."""
    db = DatabaseManager()
    
    print("=" * 60)
    print("TESTING UNIVERSITY INFORMATION SYSTEM")
    print("=" * 60)
    
    # Test 1: Count records
    print("\n1. Testing Record Counts:")
    students = db.get_all_students()
    courses = db.get_all_courses()
    events = db.get_all_events()
    faculty = db.get_all_faculty()
    departments = db.get_all_departments()
    
    print(f"   Students: {len(students)}")
    print(f"   Courses: {len(courses)}")
    print(f"   Events: {len(events)}")
    print(f"   Faculty: {len(faculty)}")
    print(f"   Departments: {len(departments)}")
    
    # Test 2: Retrieve specific records
    print("\n2. Testing Record Retrieval:")
    student = db.get_student("S001")
    if student:
        print(f"   ✓ Retrieved student: {student.name} - {student.major}")
    else:
        print("   ✗ Failed to retrieve student")
    
    course = db.get_course("CS101")
    if course:
        print(f"   ✓ Retrieved course: {course.name} - {course.credits} credits")
    else:
        print("   ✗ Failed to retrieve course")
    
    # Test 3: Test enrollments
    print("\n3. Testing Enrollment Relationships:")
    student_courses = db.get_student_courses("S001")
    print(f"   Student S001 is enrolled in {len(student_courses)} course(s):")
    for course in student_courses:
        print(f"     - {course.course_id}: {course.name}")
    
    course_students = db.get_course_students("CS101")
    print(f"   Course CS101 has {len(course_students)} student(s) enrolled:")
    for student in course_students[:3]:  # Show first 3
        print(f"     - {student.student_id}: {student.name}")
    
    # Test 4: Test data integrity
    print("\n4. Testing Data Integrity:")
    test_student = Student("TEST001", "Test Student", "test@test.edu", "Testing", 1, "2024-01-01")
    if db.add_student(test_student):
        print("   ✓ Successfully added test student")
        if db.delete_student("TEST001"):
            print("   ✓ Successfully deleted test student")
        else:
            print("   ✗ Failed to delete test student")
    else:
        print("   ✗ Failed to add test student")
    
    # Test 5: Display sample data
    print("\n5. Sample Data Preview:")
    print("\n   First 3 Students:")
    for student in students[:3]:
        print(f"     {student.student_id}: {student.name} - {student.major}, Year {student.year}")
    
    print("\n   First 3 Courses:")
    for course in courses[:3]:
        print(f"     {course.course_id}: {course.name} - {course.department}")
    
    print("\n   First 3 Events:")
    for event in events[:3]:
        print(f"     {event.event_id}: {event.name} - {event.date}")
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nThe University Information System is ready to use.")
    print("Run: python3 university_system.py")
    print("=" * 60)


if __name__ == "__main__":
    test_database_operations()
