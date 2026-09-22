# Console Record-Management Application

## Project Description

Console Record Manager Application is a simple Python application for managing student records. Users can add, view, search, update, and delete records through a menu-driven console interface. Records are saved in a JSON file so they remain available after the application is closed.

## Features

- Add a new student record
- View all saved records
- Search records by name or course
- Update an existing record using its roll number
- Delete a record with confirmation
- Validate names, courses, ages, and roll numbers
- Save and load records using a JSON file
- Handle invalid input and file-related errors

## Technologies and Concepts Used

- Python 3
- Variables and data types: strings, integers, lists, dictionaries, and sets
- Conditional statements: `if`, `elif`, and `else`
- Loops: `while` and `for`
- Functions for separate application tasks
- Exception handling with `try` and `except`
- File I/O for reading and writing JSON data
- Menu-driven console application design
- Python `json` and `os` modules

## How to Run the Application

1. Install Python 3 on your computer.
2. Open a terminal in the project folder.
3. Run the following command:

   ```text
   python record_manager.py
   ```

4. Choose an option from the menu and follow the prompts.

The application automatically creates or updates `records.json` in the same folder. This file stores the records permanently.
