"""
Data models for the University Information System.
"""

from datetime import datetime
from typing import Optional


class Student:
    """Represents a student in the university."""
    
    def __init__(self, student_id: str, name: str, email: str, 
                 major: str, year: int, enrollment_date: str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.major = major
        self.year = year
        self.enrollment_date = enrollment_date
    
    def to_dict(self):
        """Convert student object to dictionary."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'email': self.email,
            'major': self.major,
            'year': self.year,
            'enrollment_date': self.enrollment_date
        }
    
    def __str__(self):
        return f"Student({self.student_id}, {self.name}, {self.major}, Year {self.year})"


class Course:
    """Represents a course offered by the university."""
    
    def __init__(self, course_id: str, name: str, department: str,
                 credits: int, professor: str, semester: str):
        self.course_id = course_id
        self.name = name
        self.department = department
        self.credits = credits
        self.professor = professor
        self.semester = semester
    
    def to_dict(self):
        """Convert course object to dictionary."""
        return {
            'course_id': self.course_id,
            'name': self.name,
            'department': self.department,
            'credits': self.credits,
            'professor': self.professor,
            'semester': self.semester
        }
    
    def __str__(self):
        return f"Course({self.course_id}, {self.name}, {self.credits} credits)"


class Event:
    """Represents a university event."""
    
    def __init__(self, event_id: str, name: str, description: str,
                 date: str, location: str, organizer: str, category: str):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.date = date
        self.location = location
        self.organizer = organizer
        self.category = category
    
    def to_dict(self):
        """Convert event object to dictionary."""
        return {
            'event_id': self.event_id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'location': self.location,
            'organizer': self.organizer,
            'category': self.category
        }
    
    def __str__(self):
        return f"Event({self.event_id}, {self.name}, {self.date})"


class Faculty:
    """Represents a faculty member."""
    
    def __init__(self, faculty_id: str, name: str, email: str,
                 department: str, position: str, hire_date: str):
        self.faculty_id = faculty_id
        self.name = name
        self.email = email
        self.department = department
        self.position = position
        self.hire_date = hire_date
    
    def to_dict(self):
        """Convert faculty object to dictionary."""
        return {
            'faculty_id': self.faculty_id,
            'name': self.name,
            'email': self.email,
            'department': self.department,
            'position': self.position,
            'hire_date': self.hire_date
        }
    
    def __str__(self):
        return f"Faculty({self.faculty_id}, {self.name}, {self.position})"


class Department:
    """Represents an academic department."""
    
    def __init__(self, dept_id: str, name: str, head: str, 
                 building: str, contact_email: str):
        self.dept_id = dept_id
        self.name = name
        self.head = head
        self.building = building
        self.contact_email = contact_email
    
    def to_dict(self):
        """Convert department object to dictionary."""
        return {
            'dept_id': self.dept_id,
            'name': self.name,
            'head': self.head,
            'building': self.building,
            'contact_email': self.contact_email
        }
    
    def __str__(self):
        return f"Department({self.dept_id}, {self.name}, Head: {self.head})"
