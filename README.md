# University Information-Based System

A comprehensive command-line application for managing university information including students, courses, events, faculty, and departments.

## Features

### 1. Student Management
- Add, view, update, and delete student records
- Track student enrollment information (ID, name, email, major, year)
- Enroll students in courses
- View courses for each student

### 2. Course Management
- Add, view, and delete course records
- Track course details (ID, name, department, credits, professor, semester)
- View student enrollment for each course

### 3. Event Tracking
- Add, view, and delete university events
- Track event information (ID, name, description, date, location, organizer, category)
- Categorize events (Academic, Sports, Cultural, Career, etc.)

### 4. Faculty Management
- Add, view, and delete faculty member records
- Track faculty information (ID, name, email, department, position, hire date)

### 5. Department Management
- Add, view, and delete department records
- Track department details (ID, name, head, building, contact email)

### 6. Reports & Statistics
- View system-wide summary statistics
- Group students by major
- Group courses by department
- View all events chronologically

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses Python standard library)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/alyaashuhada/eventTrack2.git
   cd eventTrack2
   ```

2. The system uses SQLite for data persistence, which is included in Python's standard library.

## Usage

### Running the Application

Start the main application:
```bash
python3 university_system.py
```

### Populating Sample Data

To populate the database with sample data for testing:
```bash
python3 sample_data.py
```

This will create:
- 5 departments
- 6 faculty members
- 9 courses
- 10 students
- 7 events
- Multiple course enrollments

### Main Menu Navigation

The application provides an interactive menu system:

```
============================================================
  UNIVERSITY INFORMATION SYSTEM
============================================================

  1. Student Management
  2. Course Management
  3. Event Tracking
  4. Faculty Management
  5. Department Management
  6. Reports & Statistics
  0. Back/Exit
```

Navigate by entering the number of your choice and pressing Enter.

## Database Schema

The system uses SQLite with the following tables:

### Students
- `student_id` (Primary Key)
- `name`
- `email` (Unique)
- `major`
- `year`
- `enrollment_date`

### Courses
- `course_id` (Primary Key)
- `name`
- `department`
- `credits`
- `professor`
- `semester`

### Events
- `event_id` (Primary Key)
- `name`
- `description`
- `date`
- `location`
- `organizer`
- `category`

### Faculty
- `faculty_id` (Primary Key)
- `name`
- `email` (Unique)
- `department`
- `position`
- `hire_date`

### Departments
- `dept_id` (Primary Key)
- `name`
- `head`
- `building`
- `contact_email`

### Enrollments (Many-to-Many)
- `student_id` (Foreign Key)
- `course_id` (Foreign Key)
- `enrollment_date`
- `grade`

## Project Structure

```
eventTrack2/
├── README.md                 # This file
├── requirements.txt          # Python dependencies (none required)
├── models.py                 # Data model classes
├── database.py               # Database management and operations
├── university_system.py      # Main CLI application
├── sample_data.py            # Sample data generator
└── university.db             # SQLite database (created automatically)
```

## Examples

### Adding a Student
1. Select "1. Student Management" from main menu
2. Select "1. Add New Student"
3. Enter student details:
   - Student ID: S011
   - Full Name: Alice Cooper
   - Email: alice.cooper@student.edu
   - Major: Computer Science
   - Year: 1

### Enrolling a Student in a Course
1. Select "1. Student Management" from main menu
2. Select "6. Enroll Student in Course"
3. Enter student ID: S011
4. Enter course ID: CS101

### Adding an Event
1. Select "3. Event Tracking" from main menu
2. Select "1. Add New Event"
3. Enter event details:
   - Event ID: EVT008
   - Event Name: Tech Conference 2024
   - Description: Annual technology conference
   - Date: 2024-12-15
   - Location: Convention Center
   - Organizer: CS Department
   - Category: Academic

### Viewing Reports
1. Select "6. Reports & Statistics" from main menu
2. Choose from available reports:
   - Total counts summary
   - Students grouped by major
   - Courses grouped by department
   - All events chronologically

## Data Persistence

All data is stored in a SQLite database file (`university.db`) which is created automatically when you first run the application. The database persists between sessions, so all your data is saved.

To start fresh:
1. Delete the `university.db` file
2. Run the application again to create a new empty database
3. Optionally run `sample_data.py` to populate with sample data

## Features Summary

✓ Complete CRUD operations for all entities
✓ Relationship management (student-course enrollments)
✓ Interactive command-line interface
✓ Data validation and error handling
✓ SQLite database for persistence
✓ Sample data generator for testing
✓ Reporting and statistics
✓ User-friendly menu navigation

## License

This project is part of the eventTrack2 repository.

## Author

Developed as a University Information-Based System for managing academic records, events, and personnel.