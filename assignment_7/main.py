from database import Database, Entry


def main():
    db = Database("faculty.txt")

    while True:
        print()
        choice = select_menu_option()

        if choice == 1:
            success = db.delete_first_entry()
            if success:
                print("First entry deleted.")
            else:
                print("Failed to delete first entry.")

        elif choice == 2:
            largest_index = db.largest_column_value_index("birth_year")
            if largest_index == -1:
                print("No records available.")
            else:
                print(db.get_heading_string())
                print(db.get_record_string(largest_index))

        elif choice == 3:
            db.save_to_file("report.txt")
            print("Entries saved to 'report.txt'.")

        elif choice == 4:
            value = get_integer("Enter the ID of the record to delete: ")
            index = db.find_record_using_id(value)

            if index != -1:
                print(db.get_heading_string())
                print(db.get_record_string(index))
                confirm = input("Are you sure you want to delete this record? (y/n): ").lower()
                if confirm == "y":
                    if db.delete_using_id(value):
                        print("Record deleted.")
                    else:
                        print("Failed to delete record.")
            else:
                print("Record not found.")

        elif choice == 5:
            entry = Entry(
                get_integer("Enter ID: "),
                input("Enter last name: "),
                input("Enter first name: "),
                input("Enter department: "),
                input("Enter role: "),
                get_integer("Enter birth year: "),
                input("Enter sex: "),
                get_integer("Enter salary: "),
                get_agrees(),
                get_float("Enter unknown float: ")
            )

            print("New record:")
            print(db.get_heading_string())
            print(format_entry(entry))

            confirm = input("Are you sure you want to add this record? (y/n): ").lower()
            if confirm == "y":
                if db.add_record_using_id(entry):
                    print("Record added.")
                else:
                    print("A record with that ID already exists.")

        elif choice == 6:
            value = get_integer("Enter the ID of the record to update: ")
            index = db.find_record_using_id(value)

            if index == -1:
                print("Record not found.")
                continue

            print("Current record:")
            print(db.get_heading_string())
            print(db.get_record_string(index))

            while True:
                column_name = select_update_option()
                if column_name is None:
                    break

                if column_name in ("birth_year", "salary"):
                    new_value = get_integer("Enter the new value: ")
                elif column_name == "unknown_float":
                    new_value = get_float("Enter the new value: ")
                elif column_name == "agrees":
                    new_value = get_agrees()
                else:
                    new_value = input("Enter the new value: ")

                confirm = input("Are you sure you want to update this field? (y/n): ").lower()
                if confirm == "y":
                    if db.update_record_using_id(value, column_name, new_value):
                        print("Record updated.")
                    else:
                        print("Failed to update record.")

                index = db.find_record_using_id(value)
                print(db.get_heading_string())
                print(db.get_record_string(index))

        elif choice == 7:
            print(db.get_heading_string())
            print(db.__str__())

        elif choice == 8:
            break


def format_entry(entry):
    return "%-20d%-20s%-20s%-20s%-20s%-20d%-20s%-20d%-20s%-20.2f\n" % (entry.id, entry.name_last, entry.name_first, entry.department, entry.role, entry.birth_year, entry.sex, entry.salary, entry.agrees, entry.unknown_float)


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_agrees():
    while True:
        value = input("Enter agrees (Yes/No): ").capitalize()
        if value in ("Yes", "No"):
            return value
        print("Please enter Yes or No.")


def select_menu_option():
    def print_menu():
        print("Menu:")
        print("1. Delete First Record")
        print("2. Display the Record with a given Largest Value")
        print("3. Print all Records in a Report File")
        print("4. Delete a Record Using Key")
        print("5. Add a New Record Using Key")
        print("6. Update a Record Using Key")
        print("7. Display all Records on the Screen")
        print("8. Quit")

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")
        if choice in [str(i) for i in range(1, 9)]:
            return int(choice)
        print("Invalid choice. Please try again.")

def select_update_option():
    options = {
        1: "name_last",
        2: "name_first",
        3: "department",
        4: "role",
        5: "birth_year",
        6: "sex",
        7: "salary",
        8: "agrees",
        9: "unknown_float",
        10: None
    }

    while True:
        print("Update Sub-Menu:")
        print("1. Last Name")
        print("2. First Name")
        print("3. Department")
        print("4. Role")
        print("5. Birth Year")
        print("6. Sex")
        print("7. Salary")
        print("8. Agrees")
        print("9. Unknown Float")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")
        if choice.isdigit() and int(choice) in options:
            return options[int(choice)]
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
