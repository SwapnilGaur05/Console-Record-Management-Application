# Assignment 1: Mini Project – Console Record-Management Application

## Assignment Report

**Student Name:** Swapnil Gaur  
**Date:** September 2026  
**Subject:** Python for Data Analytics (PYDA)  
**Project Title:** Student Record Management System

---

## 1. Introduction

This report documents the development of a console-based record-management application created as part of Assignment 1 for the PYDA course. The project is a simple yet effective student record system that allows users to add, view, search, update, and delete student records through a menu-driven interface.

The application demonstrates the practical use of Python fundamentals such as data structures, functions, loops, conditional logic, exception handling, and file handling. It also shows how a small real-world program can be structured into modular parts for readability and maintainability.

---

## 2. Objective

The main objective of the project was to build a functional console application that:

- Provides a clear menu-based user interface
- Supports CRUD operations (Create, Read, Update, Delete)
- Stores records persistently in a JSON file
- Validates user input to avoid invalid data entries
- Uses modular functions to organize the code
- Demonstrates efficient Python programming concepts

---

## 3. System Design

### 3.1 Architecture

The application follows a simple single-file architecture with clearly separated responsibilities.

```text
record_manager.py
├── Configuration & File Path Setup
├── File I/O Functions            (load_records, save_records)
├── Validation Helpers            (get_next_roll_no)
├── Display Functions             (display_record, display_menu)
├── CRUD Functions                (add_record, view_records, search_records,
│                                 update_record, delete_record)
├── Search and Lookup             (find_record)
├── Main Program Loop            (main)
└── Entry Point                  (__name__ == "__main__")
```

### 3.2 Data Structure

Each student record is stored as a Python dictionary. The application keeps all records in a list of dictionaries.

| Field     | Data Type | Description                |
| --------- | --------- | -------------------------- |
| `roll_no` | `int`     | Unique student roll number |
| `name`    | `str`     | Student name               |
| `age`     | `int`     | Student age                |
| `course`  | `str`     | Student course name        |

Example record format:

```python
{
    "roll_no": 1000,
    "name": "Swapnil Gaur",
    "age": 21,
    "course": "DSA"
}
```

### 3.3 Data Flow

```text
User Input → Validation → List of Records → records.json
                                  ↑
                              Program Start
                                  ↑
                         JSON File Loaded into Memory
```

---

## 4. Python Concepts Demonstrated

### 4.1 Data Types and Variables

The project uses several Python data types, including:

- `str` for names and course titles
- `int` for roll numbers and ages
- `list` to store all records
- `dict` for each individual record
- `bool` for confirmation logic

The data is managed using variables and dictionaries to represent student information in a structured form.

### 4.2 Conditional Statements and Loops

The application uses `if`, `elif`, and `else` statements to process user menu choices and validate inputs.

```python
if choice == "1":
    add_record(records)
elif choice == "2":
    view_records(records)
```

The `while True` loop keeps the menu active until the user chooses to exit. This ensures the program stays interactive and continues accepting commands.

### 4.3 Functions

The project is organized into multiple reusable functions, which makes the code easier to understand and maintain.

| Category         | Functions                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------ |
| File I/O         | `load_records()`, `save_records()`                                                         |
| Record Utilities | `get_next_id()`, `get_next_roll_no()`                                                      |
| Display          | `display_record()`, `display_menu()`                                                       |
| CRUD Operations  | `add_record()`, `view_records()`, `search_records()`, `update_record()`, `delete_record()` |
| Search           | `find_record()`                                                                            |
| Main Entry       | `main()`                                                                                   |

Each function is responsible for a single task, which improves code readability and modularity.

### 4.4 Exception Handling

The application handles errors gracefully using `try` and `except` blocks. This prevents the program from crashing when the user enters invalid data or the file is missing or corrupted.

Examples include:

- Invalid age input
- Empty name or course fields
- Missing JSON file
- Corrupted JSON data
- General file system errors

```python
try:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        records = json.load(file)
except FileNotFoundError:
    return []
except (json.JSONDecodeError, OSError) as error:
    print(f"Could not load records: {error}")
    return []
```

### 4.5 File I/O

The program uses Python’s built-in `json` module to store and retrieve data.

- Records are saved to `records.json`
- Data is loaded when the program starts
- Data is written back to the file after add, update, and delete operations
- The file uses UTF-8 encoding for safe text storage

```python
with open(DATA_FILE, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=4)
```

### 4.6 Menu-Driven Console Design

The application presents a numbered menu to the user:

1. Add record
2. View all records
3. Search records
4. Update record
5. Delete record
6. Exit

This design allows users to interact with the system easily and is a common pattern in console-based applications.

---

## 5. Features Summary

1. Add Record: Allows a user to enter a student name, age, and course and assigns a unique roll number.
2. View All Records: Displays all stored records in the console.
3. Search Records: Finds records by matching names or course information.
4. Update Record: Allows editing a record after it is found by roll number.
5. Delete Record: Removes a selected record after confirmation.
6. Persistent Storage: Saves records in a JSON file so that the data remains available after the program closes.

---

## 6. Testing

The application was tested for the following scenarios:

| Test Case            | Input / Scenario                    | Expected Result             | Status |
| -------------------- | ----------------------------------- | --------------------------- | ------ |
| Add valid record     | Name, age, course entered correctly | Record saved successfully   | ✓ Pass |
| Add empty name       | Blank name input                    | Error message displayed     | ✓ Pass |
| Add invalid age      | Negative or non-numeric age         | Validation error shown      | ✓ Pass |
| View records         | Empty or filled list                | Correct output displayed    | ✓ Pass |
| Search records       | Match by name or course             | Matching records shown      | ✓ Pass |
| Search with no match | Unavailable keyword                 | “No matching records found” | ✓ Pass |
| Update record        | Valid roll number and new values    | Record updated              | ✓ Pass |
| Delete record        | Valid record and confirmation       | Record removed              | ✓ Pass |
| Cancel deletion      | User enters `n`                     | Record kept                 | ✓ Pass |
| Invalid menu input   | Number outside 1–6                  | Error message displayed     | ✓ Pass |
| Missing data file    | `records.json` absent               | Empty list created          | ✓ Pass |
| Corrupted JSON file  | Invalid JSON content                | Error handled gracefully    | ✓ Pass |

---

## 7. Limitations and Future Enhancements

### Current Limitations

- Only one file stores the data, so the application is simple and lightweight
- No sorting or filtering features are available
- There is no login or authentication system
- Data validation is basic and limited to required fields

### Potential Enhancements

- Add student ID field for more structured records
- Include additional fields such as phone number and email
- Add sorting by name, age, or roll number
- Add a search by roll number with precise matching
- Convert the project into a graphical user interface version
- Use SQLite or a database for better data management

---

## 8. Conclusion

This project successfully demonstrates how Python can be used to build a functional and practical console-based record management system. It covers core programming concepts such as variables, loops, conditions, functions, file handling, and user validation in a simple and organized way.

The application is user-friendly, modular, and easy to extend. It serves as a strong beginner-level project for learning Python in the context of data analytics and software development.

---

## 9. References

- Python Official Documentation: https://docs.python.org/3/
- Python `json` Module: https://docs.python.org/3/library/json.html
- Python Input/Output Guide: https://docs.python.org/3/tutorial/inputoutput.html

---

## 10. Project Files

- `record_manager.py` – Main application logic
- `records.json` – Persistent data storage file
