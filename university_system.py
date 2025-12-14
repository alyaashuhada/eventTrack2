#!/usr/bin/env python3
"""
University Information-Based System
Main command-line interface for managing university data.
"""

import sys
from datetime import datetime
from database import DatabaseManager
from models import Student, Course, Event, Faculty, Department


class UniversitySystem:
    """Main application class for the University Information System."""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.running = True
    
    def clear_screen(self):
        """Clear the console screen."""
        print("\n" * 2)
    
    def print_header(self, title):
        """Print a formatted header."""
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)
    
    def print_menu(self, options):
        """Print a menu with numbered options."""
        print()
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        print("  0. Back/Exit")
        print()
    
    def get_input(self, prompt, required=True):
        """Get user input with optional validation."""
        while True:
            value = input(f"  {prompt}: ").strip()
            if value or not required:
                return value
            print("  This field is required. Please try again.")
    
    def get_int_input(self, prompt, min_val=None, max_val=None):
        """Get integer input with optional range validation."""
        while True:
            try:
                value = int(input(f"  {prompt}: "))
                if min_val is not None and value < min_val:
                    print(f"  Value must be at least {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"  Value must be at most {max_val}")
                    continue
                return value
            except ValueError:
                print("  Please enter a valid number.")
    
    def confirm_action(self, message):
        """Ask for confirmation."""
        response = input(f"  {message} (y/n): ").strip().lower()
        return response == 'y'
    
    # ==================== Main Menu ====================
    
    def main_menu(self):
        """Display and handle the main menu."""
        while self.running:
            self.print_header("UNIVERSITY INFORMATION SYSTEM")
            options = [
                "Student Management",
                "Course Management",
                "Event Tracking",
                "Faculty Management",
                "Department Management",
                "Reports & Statistics"
            ]
            self.print_menu(options)
            
            choice = self.get_input("Select an option")
            
            if choice == "1":
                self.student_menu()
            elif choice == "2":
                self.course_menu()
            elif choice == "3":
                self.event_menu()
            elif choice == "4":
                self.faculty_menu()
            elif choice == "5":
                self.department_menu()
            elif choice == "6":
                self.reports_menu()
            elif choice == "0":
                if self.confirm_action("Are you sure you want to exit?"):
                    print("\n  Thank you for using the University Information System!")
                    self.running = False
            else:
                print("\n  Invalid option. Please try again.")
                input("\n  Press Enter to continue...")
    
    # ==================== Student Management ====================
    
    def student_menu(self):
        """Handle student management menu."""
        while True:
            self.print_header("STUDENT MANAGEMENT")
            options = [
                "Add New Student",
                "View All Students",
                "Search Student",
                "Update Student",
                "Delete Student",
                "Enroll Student in Course",
                "View Student's Courses"
            ]
            self.print_menu(options)
            
            choice = self.get_input("Select an option")
            
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_all_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                self.enroll_student()
            elif choice == "7":
                self.view_student_courses()
            elif choice == "0":
                break
            else:
                print("\n  Invalid option. Please try again.")
            
            input("\n  Press Enter to continue...")
    
    def add_student(self):
        """Add a new student."""
        print("\n  === Add New Student ===\n")
        
        student_id = self.get_input("Student ID (e.g., S001)")
        name = self.get_input("Full Name")
        email = self.get_input("Email")
        major = self.get_input("Major")
        year = self.get_int_input("Year (1-4)", 1, 4)
        enrollment_date = datetime.now().strftime("%Y-%m-%d")
        
        student = Student(student_id, name, email, major, year, enrollment_date)
        
        if self.db.add_student(student):
            print(f"\n  ✓ Student {name} added successfully!")
        else:
            print(f"\n  ✗ Failed to add student. ID or email may already exist.")
    
    def view_all_students(self):
        """Display all students."""
        print("\n  === All Students ===\n")
        students = self.db.get_all_students()
        
        if not students:
            print("  No students found.")
            return
        
        print(f"  {'ID':<10} {'Name':<25} {'Major':<20} {'Year':<5} {'Email':<30}")
        print("  " + "-" * 90)
        for student in students:
            print(f"  {student.student_id:<10} {student.name:<25} {student.major:<20} "
                  f"{student.year:<5} {student.email:<30}")
    
    def search_student(self):
        """Search for a student by ID."""
        print("\n  === Search Student ===\n")
        student_id = self.get_input("Enter Student ID")
        
        student = self.db.get_student(student_id)
        if student:
            print(f"\n  Student Found:")
            print(f"  ID: {student.student_id}")
            print(f"  Name: {student.name}")
            print(f"  Email: {student.email}")
            print(f"  Major: {student.major}")
            print(f"  Year: {student.year}")
            print(f"  Enrollment Date: {student.enrollment_date}")
        else:
            print(f"\n  ✗ Student with ID {student_id} not found.")
    
    def update_student(self):
        """Update student information."""
        print("\n  === Update Student ===\n")
        student_id = self.get_input("Enter Student ID")
        
        student = self.db.get_student(student_id)
        if not student:
            print(f"\n  ✗ Student with ID {student_id} not found.")
            return
        
        print(f"\n  Current Information for {student.name}:")
        print(f"  1. Name: {student.name}")
        print(f"  2. Email: {student.email}")
        print(f"  3. Major: {student.major}")
        print(f"  4. Year: {student.year}")
        
        print("\n  Enter new values (press Enter to keep current value):\n")
        
        name = self.get_input(f"Name [{student.name}]", required=False) or student.name
        email = self.get_input(f"Email [{student.email}]", required=False) or student.email
        major = self.get_input(f"Major [{student.major}]", required=False) or student.major
        year_input = self.get_input(f"Year [{student.year}]", required=False)
        year = int(year_input) if year_input else student.year
        
        updated_student = Student(student_id, name, email, major, year, student.enrollment_date)
        
        if self.db.update_student(updated_student):
            print(f"\n  ✓ Student information updated successfully!")
        else:
            print(f"\n  ✗ Failed to update student information.")
    
    def delete_student(self):
        """Delete a student."""
        print("\n  === Delete Student ===\n")
        student_id = self.get_input("Enter Student ID")
        
        student = self.db.get_student(student_id)
        if not student:
            print(f"\n  ✗ Student with ID {student_id} not found.")
            return
        
        print(f"\n  Student: {student.name} ({student.student_id})")
        if self.confirm_action("Are you sure you want to delete this student?"):
            if self.db.delete_student(student_id):
                print(f"\n  ✓ Student deleted successfully!")
            else:
                print(f"\n  ✗ Failed to delete student.")
    
    def enroll_student(self):
        """Enroll a student in a course."""
        print("\n  === Enroll Student in Course ===\n")
        student_id = self.get_input("Student ID")
        course_id = self.get_input("Course ID")
        
        if not self.db.get_student(student_id):
            print(f"\n  ✗ Student with ID {student_id} not found.")
            return
        
        if not self.db.get_course(course_id):
            print(f"\n  ✗ Course with ID {course_id} not found.")
            return
        
        enrollment_date = datetime.now().strftime("%Y-%m-%d")
        
        if self.db.enroll_student(student_id, course_id, enrollment_date):
            print(f"\n  ✓ Student enrolled successfully!")
        else:
            print(f"\n  ✗ Enrollment failed. Student may already be enrolled in this course.")
    
    def view_student_courses(self):
        """View courses for a specific student."""
        print("\n  === Student's Courses ===\n")
        student_id = self.get_input("Enter Student ID")
        
        student = self.db.get_student(student_id)
        if not student:
            print(f"\n  ✗ Student with ID {student_id} not found.")
            return
        
        courses = self.db.get_student_courses(student_id)
        
        print(f"\n  Courses for {student.name}:\n")
        if not courses:
            print("  No courses found.")
            return
        
        print(f"  {'Course ID':<12} {'Name':<30} {'Credits':<8} {'Professor':<20}")
        print("  " + "-" * 70)
        for course in courses:
            print(f"  {course.course_id:<12} {course.name:<30} {course.credits:<8} {course.professor:<20}")
    
    # ==================== Course Management ====================
    
    def course_menu(self):
        """Handle course management menu."""
        while True:
            self.print_header("COURSE MANAGEMENT")
            options = [
                "Add New Course",
                "View All Courses",
                "Search Course",
                "Delete Course",
                "View Course Enrollment"
            ]
            self.print_menu(options)
            
            choice = self.get_input("Select an option")
            
            if choice == "1":
                self.add_course()
            elif choice == "2":
                self.view_all_courses()
            elif choice == "3":
                self.search_course()
            elif choice == "4":
                self.delete_course()
            elif choice == "5":
                self.view_course_students()
            elif choice == "0":
                break
            else:
                print("\n  Invalid option. Please try again.")
            
            input("\n  Press Enter to continue...")
    
    def add_course(self):
        """Add a new course."""
        print("\n  === Add New Course ===\n")
        
        course_id = self.get_input("Course ID (e.g., CS101)")
        name = self.get_input("Course Name")
        department = self.get_input("Department")
        credits = self.get_int_input("Credits", 1, 6)
        professor = self.get_input("Professor")
        semester = self.get_input("Semester (e.g., Fall 2024)")
        
        course = Course(course_id, name, department, credits, professor, semester)
        
        if self.db.add_course(course):
            print(f"\n  ✓ Course {name} added successfully!")
        else:
            print(f"\n  ✗ Failed to add course. ID may already exist.")
    
    def view_all_courses(self):
        """Display all courses."""
        print("\n  === All Courses ===\n")
        courses = self.db.get_all_courses()
        
        if not courses:
            print("  No courses found.")
            return
        
        print(f"  {'ID':<12} {'Name':<30} {'Department':<15} {'Credits':<8} {'Professor':<20}")
        print("  " + "-" * 85)
        for course in courses:
            print(f"  {course.course_id:<12} {course.name:<30} {course.department:<15} "
                  f"{course.credits:<8} {course.professor:<20}")
    
    def search_course(self):
        """Search for a course by ID."""
        print("\n  === Search Course ===\n")
        course_id = self.get_input("Enter Course ID")
        
        course = self.db.get_course(course_id)
        if course:
            print(f"\n  Course Found:")
            print(f"  ID: {course.course_id}")
            print(f"  Name: {course.name}")
            print(f"  Department: {course.department}")
            print(f"  Credits: {course.credits}")
            print(f"  Professor: {course.professor}")
            print(f"  Semester: {course.semester}")
        else:
            print(f"\n  ✗ Course with ID {course_id} not found.")
    
    def delete_course(self):
        """Delete a course."""
        print("\n  === Delete Course ===\n")
        course_id = self.get_input("Enter Course ID")
        
        course = self.db.get_course(course_id)
        if not course:
            print(f"\n  ✗ Course with ID {course_id} not found.")
            return
        
        print(f"\n  Course: {course.name} ({course.course_id})")
        if self.confirm_action("Are you sure you want to delete this course?"):
            if self.db.delete_course(course_id):
                print(f"\n  ✓ Course deleted successfully!")
            else:
                print(f"\n  ✗ Failed to delete course.")
    
    def view_course_students(self):
        """View students enrolled in a specific course."""
        print("\n  === Course Enrollment ===\n")
        course_id = self.get_input("Enter Course ID")
        
        course = self.db.get_course(course_id)
        if not course:
            print(f"\n  ✗ Course with ID {course_id} not found.")
            return
        
        students = self.db.get_course_students(course_id)
        
        print(f"\n  Students enrolled in {course.name}:\n")
        if not students:
            print("  No students enrolled.")
            return
        
        print(f"  {'Student ID':<12} {'Name':<30} {'Major':<20} {'Year':<5}")
        print("  " + "-" * 67)
        for student in students:
            print(f"  {student.student_id:<12} {student.name:<30} {student.major:<20} {student.year:<5}")
    
    # ==================== Event Management ====================
    
    def event_menu(self):
        """Handle event tracking menu."""
        while True:
            self.print_header("EVENT TRACKING")
            options = [
                "Add New Event",
                "View All Events",
                "Search Event",
                "Delete Event"
            ]
            self.print_menu(options)
            
            choice = self.get_input("Select an option")
            
            if choice == "1":
                self.add_event()
            elif choice == "2":
                self.view_all_events()
            elif choice == "3":
                self.search_event()
            elif choice == "4":
                self.delete_event()
            elif choice == "0":
                break
            else:
                print("\n  Invalid option. Please try again.")
            
            input("\n  Press Enter to continue...")
    
    def add_event(self):
        """Add a new event."""
        print("\n  === Add New Event ===\n")
        
        event_id = self.get_input("Event ID (e.g., EVT001)")
        name = self.get_input("Event Name")
        description = self.get_input("Description")
        date = self.get_input("Date (YYYY-MM-DD)")
        location = self.get_input("Location")
        organizer = self.get_input("Organizer")
        category = self.get_input("Category (e.g., Academic, Sports, Cultural)")
        
        event = Event(event_id, name, description, date, location, organizer, category)
        
        if self.db.add_event(event):
            print(f"\n  ✓ Event {name} added successfully!")
        else:
            print(f"\n  ✗ Failed to add event. ID may already exist.")
    
    def view_all_events(self):
        """Display all events."""
        print("\n  === All Events ===\n")
        events = self.db.get_all_events()
        
        if not events:
            print("  No events found.")
            return
        
        print(f"  {'ID':<10} {'Name':<25} {'Date':<12} {'Location':<20} {'Category':<15}")
        print("  " + "-" * 82)
        for event in events:
            print(f"  {event.event_id:<10} {event.name:<25} {event.date:<12} "
                  f"{event.location:<20} {event.category:<15}")
    
    def search_event(self):
        """Search for an event by ID."""
        print("\n  === Search Event ===\n")
        event_id = self.get_input("Enter Event ID")
        
        event = self.db.get_event(event_id)
        if event:
            print(f"\n  Event Found:")
            print(f"  ID: {event.event_id}")
            print(f"  Name: {event.name}")
            print(f"  Description: {event.description}")
            print(f"  Date: {event.date}")
            print(f"  Location: {event.location}")
            print(f"  Organizer: {event.organizer}")
            print(f"  Category: {event.category}")
        else:
            print(f"\n  ✗ Event with ID {event_id} not found.")
    
    def delete_event(self):
        """Delete an event."""
        print("\n  === Delete Event ===\n")
        event_id = self.get_input("Enter Event ID")
        
        event = self.db.get_event(event_id)
        if not event:
            print(f"\n  ✗ Event with ID {event_id} not found.")
            return
        
        print(f"\n  Event: {event.name} ({event.event_id})")
        if self.confirm_action("Are you sure you want to delete this event?"):
            if self.db.delete_event(event_id):
                print(f"\n  ✓ Event deleted successfully!")
            else:
                print(f"\n  ✗ Failed to delete event.")
    
    # ==================== Faculty Management ====================
    
    def faculty_menu(self):
        """Handle faculty management menu."""
        while True:
            self.print_header("FACULTY MANAGEMENT")
            options = [
                "Add New Faculty Member",
                "View All Faculty",
                "Search Faculty Member",
                "Delete Faculty Member"
            ]
            self.print_menu(options)
            
            choice = self.get_input("Select an option")
            
            if choice == "1":
                self.add_faculty()
            elif choice == "2":
                self.view_all_faculty()
            elif choice == "3":
                self.search_faculty()
            elif choice == "4":
                self.delete_faculty()
            elif choice == "0":
                break
            else:
                print("\n  Invalid option. Please try again.")
            
            input("\n  Press Enter to continue...")
    
    def add_faculty(self):
        """Add a new faculty member."""
        print("\n  === Add New Faculty Member ===\n")
        
        faculty_id = self.get_input("Faculty ID (e.g., F001)")
        name = self.get_input("Full Name")
        email = self.get_input("Email")
        department = self.get_input("Department")
        position = self.get_input("Position (e.g., Professor, Associate Professor)")
        hire_date = self.get_input("Hire Date (YYYY-MM-DD)")
        
        faculty = Faculty(faculty_id, name, email, department, position, hire_date)
        
        if self.db.add_faculty(faculty):
            print(f"\n  ✓ Faculty member {name} added successfully!")
        else:
            print(f"\n  ✗ Failed to add faculty member. ID or email may already exist.")
    
    def view_all_faculty(self):
        """Display all faculty members."""
        print("\n  === All Faculty Members ===\n")
        faculty = self.db.get_all_faculty()
        
        if not faculty:
            print("  No faculty members found.")
            return
        
        print(f"  {'ID':<10} {'Name':<25} {'Department':<20} {'Position':<25}")
        print("  " + "-" * 80)
        for member in faculty:
            print(f"  {member.faculty_id:<10} {member.name:<25} {member.department:<20} {member.position:<25}")
    
    def search_faculty(self):
        """Search for a faculty member by ID."""
        print("\n  === Search Faculty Member ===\n")
        faculty_id = self.get_input("Enter Faculty ID")
        
        faculty = self.db.get_faculty(faculty_id)
        if faculty:
            print(f"\n  Faculty Member Found:")
            print(f"  ID: {faculty.faculty_id}")
            print(f"  Name: {faculty.name}")
            print(f"  Email: {faculty.email}")
            print(f"  Department: {faculty.department}")
            print(f"  Position: {faculty.position}")
            print(f"  Hire Date: {faculty.hire_date}")
        else:
            print(f"\n  ✗ Faculty member with ID {faculty_id} not found.")
    
    def delete_faculty(self):
        """Delete a faculty member."""
        print("\n  === Delete Faculty Member ===\n")
        faculty_id = self.get_input("Enter Faculty ID")
        
        faculty = self.db.get_faculty(faculty_id)
        if not faculty:
            print(f"\n  ✗ Faculty member with ID {faculty_id} not found.")
            return
        
        print(f"\n  Faculty Member: {faculty.name} ({faculty.faculty_id})")
        if self.confirm_action("Are you sure you want to delete this faculty member?"):
            if self.db.delete_faculty(faculty_id):
                print(f"\n  ✓ Faculty member deleted successfully!")
            else:
                print(f"\n  ✗ Failed to delete faculty member.")
    
    # ==================== Department Management ====================
    
    def department_menu(self):
        """Handle department management menu."""
        while True:
            self.print_header("DEPARTMENT MANAGEMENT")
            options = [
                "Add New Department",
                "View All Departments",
                "Search Department",
                "Delete Department"
            ]
            self.print_menu(options)
            
            choice = self.get_input("Select an option")
            
            if choice == "1":
                self.add_department()
            elif choice == "2":
                self.view_all_departments()
            elif choice == "3":
                self.search_department()
            elif choice == "4":
                self.delete_department()
            elif choice == "0":
                break
            else:
                print("\n  Invalid option. Please try again.")
            
            input("\n  Press Enter to continue...")
    
    def add_department(self):
        """Add a new department."""
        print("\n  === Add New Department ===\n")
        
        dept_id = self.get_input("Department ID (e.g., DEPT001)")
        name = self.get_input("Department Name")
        head = self.get_input("Department Head")
        building = self.get_input("Building")
        contact_email = self.get_input("Contact Email")
        
        department = Department(dept_id, name, head, building, contact_email)
        
        if self.db.add_department(department):
            print(f"\n  ✓ Department {name} added successfully!")
        else:
            print(f"\n  ✗ Failed to add department. ID may already exist.")
    
    def view_all_departments(self):
        """Display all departments."""
        print("\n  === All Departments ===\n")
        departments = self.db.get_all_departments()
        
        if not departments:
            print("  No departments found.")
            return
        
        print(f"  {'ID':<12} {'Name':<30} {'Head':<25} {'Building':<15}")
        print("  " + "-" * 82)
        for dept in departments:
            print(f"  {dept.dept_id:<12} {dept.name:<30} {dept.head:<25} {dept.building:<15}")
    
    def search_department(self):
        """Search for a department by ID."""
        print("\n  === Search Department ===\n")
        dept_id = self.get_input("Enter Department ID")
        
        dept = self.db.get_department(dept_id)
        if dept:
            print(f"\n  Department Found:")
            print(f"  ID: {dept.dept_id}")
            print(f"  Name: {dept.name}")
            print(f"  Head: {dept.head}")
            print(f"  Building: {dept.building}")
            print(f"  Contact Email: {dept.contact_email}")
        else:
            print(f"\n  ✗ Department with ID {dept_id} not found.")
    
    def delete_department(self):
        """Delete a department."""
        print("\n  === Delete Department ===\n")
        dept_id = self.get_input("Enter Department ID")
        
        dept = self.db.get_department(dept_id)
        if not dept:
            print(f"\n  ✗ Department with ID {dept_id} not found.")
            return
        
        print(f"\n  Department: {dept.name} ({dept.dept_id})")
        if self.confirm_action("Are you sure you want to delete this department?"):
            if self.db.delete_department(dept_id):
                print(f"\n  ✓ Department deleted successfully!")
            else:
                print(f"\n  ✗ Failed to delete department.")
    
    # ==================== Reports & Statistics ====================
    
    def reports_menu(self):
        """Handle reports and statistics menu."""
        while True:
            self.print_header("REPORTS & STATISTICS")
            options = [
                "Total Counts Summary",
                "Students by Major",
                "Courses by Department",
                "Upcoming Events"
            ]
            self.print_menu(options)
            
            choice = self.get_input("Select an option")
            
            if choice == "1":
                self.show_summary()
            elif choice == "2":
                self.students_by_major()
            elif choice == "3":
                self.courses_by_department()
            elif choice == "4":
                self.upcoming_events()
            elif choice == "0":
                break
            else:
                print("\n  Invalid option. Please try again.")
            
            input("\n  Press Enter to continue...")
    
    def show_summary(self):
        """Display summary statistics."""
        print("\n  === University System Summary ===\n")
        
        students = self.db.get_all_students()
        courses = self.db.get_all_courses()
        events = self.db.get_all_events()
        faculty = self.db.get_all_faculty()
        departments = self.db.get_all_departments()
        
        print(f"  Total Students: {len(students)}")
        print(f"  Total Courses: {len(courses)}")
        print(f"  Total Events: {len(events)}")
        print(f"  Total Faculty: {len(faculty)}")
        print(f"  Total Departments: {len(departments)}")
    
    def students_by_major(self):
        """Display students grouped by major."""
        print("\n  === Students by Major ===\n")
        
        students = self.db.get_all_students()
        majors = {}
        
        for student in students:
            if student.major not in majors:
                majors[student.major] = []
            majors[student.major].append(student)
        
        if not majors:
            print("  No students found.")
            return
        
        for major, major_students in sorted(majors.items()):
            print(f"\n  {major}: {len(major_students)} student(s)")
            for student in major_students:
                print(f"    - {student.name} ({student.student_id})")
    
    def courses_by_department(self):
        """Display courses grouped by department."""
        print("\n  === Courses by Department ===\n")
        
        courses = self.db.get_all_courses()
        departments = {}
        
        for course in courses:
            if course.department not in departments:
                departments[course.department] = []
            departments[course.department].append(course)
        
        if not departments:
            print("  No courses found.")
            return
        
        for dept, dept_courses in sorted(departments.items()):
            print(f"\n  {dept}: {len(dept_courses)} course(s)")
            for course in dept_courses:
                print(f"    - {course.name} ({course.course_id}) - {course.credits} credits")
    
    def upcoming_events(self):
        """Display upcoming events."""
        print("\n  === All Events (by Date) ===\n")
        
        events = self.db.get_all_events()
        
        if not events:
            print("  No events found.")
            return
        
        for event in events:
            print(f"\n  {event.name}")
            print(f"    Date: {event.date}")
            print(f"    Location: {event.location}")
            print(f"    Category: {event.category}")
            print(f"    Organizer: {event.organizer}")


def main():
    """Main entry point for the application."""
    try:
        app = UniversitySystem()
        app.main_menu()
    except KeyboardInterrupt:
        print("\n\n  Program interrupted by user.")
    except Exception as e:
        print(f"\n  Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
