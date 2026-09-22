import json
import os


DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "records.json")


def load_records():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)
            return records if isinstance(records, list) else []
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load records: {error}")
        return []


def save_records(records):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
    except OSError as error:
        print(f"Could not save records: {error}")


def get_next_id(records):
    if not records:
        return 1
    return max(record["id"] for record in records) + 1


def get_next_roll_no(records):
    used_roll_numbers = {record.get("roll_no") for record in records}
    for roll_no in range(1000, 10000):
        if roll_no not in used_roll_numbers:
            return roll_no
    raise ValueError("All four-digit roll numbers are already in use.")


def display_record(record):
    print(
        f"Roll No: {record['roll_no']:04d} | Name: {record['name']} | "
        f"Age: {record['age']} | Course: {record['course']}"
    )


def add_record(records):
    print("\n--- Add Record ---")
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter age: "))
        if age <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive number for age.")
        return

    course = input("Enter course: ").strip()
    if not course:
        print("Course cannot be empty.")
        return

    try:
        record = {
            "roll_no": get_next_roll_no(records),
            "name": name,
            "age": age,
            "course": course,
        }
    except ValueError as error:
        print(error)
        return
    records.append(record)
    save_records(records)
    print("Record added successfully.")


def view_records(records):
    print("\n--- All Records ---")
    if not records:
        print("No records found.")
        return

    for record in records:
        display_record(record)


def search_records(records):
    print("\n--- Search Records ---")
    keyword = input("Enter name or course to search: ").strip().lower()
    if not keyword:
        print("Search text cannot be empty.")
        return

    matches = [
        record
        for record in records
        if keyword in record["name"].lower()
        or keyword in record["course"].lower()
    ]

    if not matches:
        print("No matching records found.")
        return

    for record in matches:
        display_record(record)


def find_record(records):
    try:
        roll_no = int(input("Enter roll number: "))
    except ValueError:
        print("Please enter a valid numeric roll number.")
        return None

    for record in records:
        if record.get("roll_no") == roll_no:
            return record

    print("Record not found.")
    return None


def update_record(records):
    print("\n--- Update Record ---")
    record = find_record(records)
    if record is None:
        return

    print("Press Enter to keep the current value.")
    name = input(f"Name [{record['name']}]: ").strip()
    course = input(f"Course [{record['course']}]: ").strip()
    age_text = input(f"Age [{record['age']}]: ").strip()

    if name:
        record["name"] = name
    if course:
        record["course"] = course
    if age_text:
        try:
            age = int(age_text)
            if age <= 0:
                raise ValueError
            record["age"] = age
        except ValueError:
            print("Invalid age. The old age was kept.")

    save_records(records)
    print("Record updated successfully.")


def delete_record(records):
    print("\n--- Delete Record ---")
    record = find_record(records)
    if record is None:
        return

    confirmation = input(f"Delete {record['name']}? (y/n): ").strip().lower()
    if confirmation == "y":
        records.remove(record)
        save_records(records)
        print("Record deleted successfully.")
    else:
        print("Delete cancelled.")


def display_menu():
    print("\n===== CONSOLE RECORD MANAGER =====")
    print("1. Add record")
    print("2. View all records")
    print("3. Search records")
    print("4. Update record")
    print("5. Delete record")
    print("6. Exit")


def main():
    records = load_records()
    print("Welcome to the Console Record Manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            search_records(records)
        elif choice == "4":
            update_record(records)
        elif choice == "5":
            delete_record(records)
        elif choice == "6":
            print("Thank you for using the application.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
