# Console Student Record Management System    

This system manages student records from the command line using JSON file storage, so the data remains available even after the program is closed.

---

## Project Description

This application is a simple student record management system designed for a beginner-level Python project. It allows users to add, view, search, update, and delete student records through a menu-driven console interface.

The project demonstrates the use of several core Python concepts in one complete working program:

- Data types and variables – strings, integers, lists, dictionaries, and sets
- Conditional statements and loops – `if`/`else` checks and `while` loops for menu navigation
- Functions – separate reusable functions for each task
- Exception handling – `try` and `except` to manage invalid input and file errors
- File I/O – reading and writing records to `records.json` using the `json` module
- Menu-driven design – user chooses actions from a numbered console menu until exiting

---

## Features

### Student Management

| #   | Feature              | Description                                                                |
| --- | -------------------- | -------------------------------------------------------------------------- |
| 1   | **Add Record**       | Adds a new student record with a unique roll number, name, age, and course |
| 2   | **View All Records** | Displays every saved record in the console                                 |
| 3   | **Search Records**   | Finds records by matching name or course text                              |
| 4   | **Update Record**    | Modifies an existing record using its roll number                          |
| 5   | **Delete Record**    | Removes a selected record after confirmation                               |

### System

| #   | Feature                         | Description                                                                      |
| --- | ------------------------------- | -------------------------------------------------------------------------------- |
| 6   | **Exit**                        | Closes the application                                                           |
| —   | **Persistent Storage**          | Records are stored in `records.json` so they remain after restarting the program |
| —   | **Input Validation**            | Empty names, invalid ages, and missing records are handled gracefully            |
| —   | **Auto Roll Number Generation** | Each new record receives the next available four-digit roll number               |

---

## 🛠️ Technologies & Concepts Used

- **Language:** Python 3
- **Standard Library Modules:**
  - `json` – reading and writing records to a JSON file
  - `os` – locating the data file in the project folder
- **Core Programming Concepts:**
  - Lists and dictionaries for storing records
  - Functions with return values and parameters
  - `while` loops for the main menu and repeated input handling
  - `try/except` blocks for file and value errors
  - String methods such as `.strip()`, `.lower()`, and `.isdigit()` for validation and formatting
  - List comprehensions for filtering matching records
  - f-strings for clean console output

---

## Project Structure

```text
PYDA - 1/
│
├── record_manager.py    # Main application code
├── records.json         # Stores all student records
├── README.md            # Project documentation
├── REPORT.md            # Assignment report
└── Executed Screeshot/ # Screenshots or outputs from the project
```

> `records.json` is created automatically when the program runs for the first time if it does not already exist.

---

## How to Run the Application

### Prerequisites

- Python 3 installed on your system

### Steps

1. Open a terminal in the project folder.
2. Run the program using:

```bash
python record_manager.py
```

3. Use the menu to add, view, search, update, or delete records.
4. The application will automatically save data in `records.json`.

---

## Sample Input / Output

### Main Menu

```text
===== CONSOLE RECORD MANAGER =====
1. Add record
2. View all records
3. Search records
4. Update record
5. Delete record
6. Exit
Enter your choice (1-6):
```

### Add Record

```text
--- Add Record ---
Enter name: Swapnil Gaur
Enter age: 21
Enter course: DSA
Record added successfully.
```

### View Records

```text
--- All Records ---
Roll No: 1000 | Name: Swapnil Gaur | Age: 21 | Course: DSA
```

### Search Records

```text
--- Search Records ---
Enter name or course to search: Swapnil Gaur
Roll No: 1000 | Name: Swapnil Gaur | Age: 21 | Course: DSA
```

---

## Error Handling Examples

The application handles invalid input without crashing:

```text
Enter name:
Name cannot be empty.
```

```text
Enter age: -5
Please enter a valid positive number for age.
```

```text
Enter roll number: abc
Please enter a valid numeric roll number.
```

```text
Search text cannot be empty.
```

If the data file is missing or corrupted, the application catches the error and returns an empty list instead of failing unexpectedly.

---

## GitHub Repository

Repository URL: (https://github.com/SwapnilGaur05/Console-Record-Management-Application)

---

## Author / Submission Details

| Field             | Detail                                                             |
| ----------------- | ------------------------------------------------------------------ |
| **Name**          | Swapnil Gaur                                                       |
| **Roll no**       | 57                                                                 |
| **Course**        | MCA - SEM 1                                                        |
| **Subject**       | Python Programming & Relational Database                           |
| **Assignment**    | Assignment 1 – Mini Project: Console Record-Management Application |
| **Date**          | 23rd September 2026                                                |

---

