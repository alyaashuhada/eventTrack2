"""
Database management for the University Information System.
Uses SQLite for data persistence.
"""

import sqlite3
from typing import List, Optional, Tuple
from models import Student, Course, Event, Faculty, Department


class DatabaseManager:
    """Manages all database operations for the university system."""
    
    def __init__(self, db_name: str = "university.db"):
        self.db_name = db_name
        self.initialize_database()
    
    def get_connection(self):
        """Get a database connection with row factory."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    def initialize_database(self):
        """Create all necessary tables if they don't exist."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
        
        # Students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                major TEXT NOT NULL,
                year INTEGER NOT NULL,
                enrollment_date TEXT NOT NULL
            )
        ''')
        
        # Courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                course_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                credits INTEGER NOT NULL,
                professor TEXT NOT NULL,
                semester TEXT NOT NULL
            )
        ''')
        
        # Events table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                event_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL,
                location TEXT NOT NULL,
                organizer TEXT NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        
        # Faculty table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS faculty (
                faculty_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                department TEXT NOT NULL,
                position TEXT NOT NULL,
                hire_date TEXT NOT NULL
            )
        ''')
        
        # Departments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS departments (
                dept_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                head TEXT NOT NULL,
                building TEXT NOT NULL,
                contact_email TEXT NOT NULL
            )
        ''')
        
        # Enrollment table (Many-to-Many relationship between students and courses)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS enrollments (
                student_id TEXT,
                course_id TEXT,
                enrollment_date TEXT NOT NULL,
                grade TEXT,
                PRIMARY KEY (student_id, course_id),
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id)
            )
        ''')
            
        conn.commit()
    
    # ==================== Student Operations ====================
    
    def add_student(self, student: Student) -> bool:
        """Add a new student to the database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO students (student_id, name, email, major, year, enrollment_date)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (student.student_id, student.name, student.email, 
                      student.major, student.year, student.enrollment_date))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
            row = cursor.fetchone()
            
            if row:
                return Student(row['student_id'], row['name'], row['email'],
                             row['major'], row['year'], row['enrollment_date'])
        return None
    
    def get_all_students(self) -> List[Student]:
        """Retrieve all students."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students ORDER BY name')
            rows = cursor.fetchall()
            
            return [Student(row['student_id'], row['name'], row['email'],
                           row['major'], row['year'], row['enrollment_date'])
                    for row in rows]
    
    def update_student(self, student: Student) -> bool:
        """Update an existing student."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE students 
                    SET name=?, email=?, major=?, year=?, enrollment_date=?
                    WHERE student_id=?
                ''', (student.name, student.email, student.major, 
                      student.year, student.enrollment_date, student.student_id))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return False
    
    def delete_student(self, student_id: str) -> bool:
        """Delete a student."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    # ==================== Course Operations ====================
    
    def add_course(self, course: Course) -> bool:
        """Add a new course to the database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO courses (course_id, name, department, credits, professor, semester)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (course.course_id, course.name, course.department,
                      course.credits, course.professor, course.semester))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_course(self, course_id: str) -> Optional[Course]:
        """Retrieve a course by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM courses WHERE course_id = ?', (course_id,))
            row = cursor.fetchone()
            
            if row:
                return Course(row['course_id'], row['name'], row['department'],
                            row['credits'], row['professor'], row['semester'])
        return None
    
    def get_all_courses(self) -> List[Course]:
        """Retrieve all courses."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM courses ORDER BY name')
            rows = cursor.fetchall()
            
            return [Course(row['course_id'], row['name'], row['department'],
                          row['credits'], row['professor'], row['semester'])
                    for row in rows]
    
    def delete_course(self, course_id: str) -> bool:
        """Delete a course."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM courses WHERE course_id = ?', (course_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    # ==================== Event Operations ====================
    
    def add_event(self, event: Event) -> bool:
        """Add a new event to the database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO events (event_id, name, description, date, location, organizer, category)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (event.event_id, event.name, event.description, event.date,
                      event.location, event.organizer, event.category))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_event(self, event_id: str) -> Optional[Event]:
        """Retrieve an event by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM events WHERE event_id = ?', (event_id,))
            row = cursor.fetchone()
            
            if row:
                return Event(row['event_id'], row['name'], row['description'],
                           row['date'], row['location'], row['organizer'], row['category'])
        return None
    
    def get_all_events(self) -> List[Event]:
        """Retrieve all events."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM events ORDER BY date DESC')
            rows = cursor.fetchall()
            
            return [Event(row['event_id'], row['name'], row['description'],
                         row['date'], row['location'], row['organizer'], row['category'])
                    for row in rows]
    
    def delete_event(self, event_id: str) -> bool:
        """Delete an event."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM events WHERE event_id = ?', (event_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    # ==================== Faculty Operations ====================
    
    def add_faculty(self, faculty: Faculty) -> bool:
        """Add a new faculty member to the database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO faculty (faculty_id, name, email, department, position, hire_date)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (faculty.faculty_id, faculty.name, faculty.email,
                      faculty.department, faculty.position, faculty.hire_date))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_faculty(self, faculty_id: str) -> Optional[Faculty]:
        """Retrieve a faculty member by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM faculty WHERE faculty_id = ?', (faculty_id,))
            row = cursor.fetchone()
            
            if row:
                return Faculty(row['faculty_id'], row['name'], row['email'],
                             row['department'], row['position'], row['hire_date'])
        return None
    
    def get_all_faculty(self) -> List[Faculty]:
        """Retrieve all faculty members."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM faculty ORDER BY name')
            rows = cursor.fetchall()
            
            return [Faculty(row['faculty_id'], row['name'], row['email'],
                           row['department'], row['position'], row['hire_date'])
                    for row in rows]
    
    def delete_faculty(self, faculty_id: str) -> bool:
        """Delete a faculty member."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM faculty WHERE faculty_id = ?', (faculty_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    # ==================== Department Operations ====================
    
    def add_department(self, department: Department) -> bool:
        """Add a new department to the database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO departments (dept_id, name, head, building, contact_email)
                    VALUES (?, ?, ?, ?, ?)
                ''', (department.dept_id, department.name, department.head,
                      department.building, department.contact_email))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_department(self, dept_id: str) -> Optional[Department]:
        """Retrieve a department by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM departments WHERE dept_id = ?', (dept_id,))
            row = cursor.fetchone()
            
            if row:
                return Department(row['dept_id'], row['name'], row['head'],
                                row['building'], row['contact_email'])
        return None
    
    def get_all_departments(self) -> List[Department]:
        """Retrieve all departments."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM departments ORDER BY name')
            rows = cursor.fetchall()
            
            return [Department(row['dept_id'], row['name'], row['head'],
                              row['building'], row['contact_email'])
                    for row in rows]
    
    def delete_department(self, dept_id: str) -> bool:
        """Delete a department."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM departments WHERE dept_id = ?', (dept_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    # ==================== Enrollment Operations ====================
    
    def enroll_student(self, student_id: str, course_id: str, enrollment_date: str) -> bool:
        """Enroll a student in a course."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO enrollments (student_id, course_id, enrollment_date)
                    VALUES (?, ?, ?)
                ''', (student_id, course_id, enrollment_date))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_student_courses(self, student_id: str) -> List[Course]:
        """Get all courses a student is enrolled in."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT c.* FROM courses c
                JOIN enrollments e ON c.course_id = e.course_id
                WHERE e.student_id = ?
            ''', (student_id,))
            rows = cursor.fetchall()
            
            return [Course(row['course_id'], row['name'], row['department'],
                          row['credits'], row['professor'], row['semester'])
                    for row in rows]
    
    def get_course_students(self, course_id: str) -> List[Student]:
        """Get all students enrolled in a course."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT s.* FROM students s
                JOIN enrollments e ON s.student_id = e.student_id
                WHERE e.course_id = ?
            ''', (course_id,))
            rows = cursor.fetchall()
            
            return [Student(row['student_id'], row['name'], row['email'],
                           row['major'], row['year'], row['enrollment_date'])
                    for row in rows]
