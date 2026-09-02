# NOTE: Do not do step 6.8
from database import Database


def main():
    db = Database("faculty.txt")
    while True:
        print()
        choice = select_menu_option()
        if choice == 1:
            db.delete_first_entry()
            print("First entry deleted.")
        elif choice == 2:
            total = db.sum_column("id")
            print(f"Sum of column 'id': {total}")
        elif choice == 3:
            largest_index = db.largest_column_value_index("birth_year")
            print(f"Index of largest value in column 'birth_year': {largest_index}")
            print(db.get_heading_string())
            print(db.get_record_string(largest_index))
        elif choice == 4:
            db.sort_entries_string_key("name_last")
            print("Entries sorted by last name (string key) in ascending order.")
        elif choice == 5:
            db.sort_entries_numeric_key("salary")
            print("Entries sorted by salary (numeric key) in descending order.")
        elif choice == 6:
            db.save_to_file("report.txt")
            print("Entries saved to 'report.txt'.")
        elif choice == 7:
            value = int(input("Enter the value for the key column (id): "))
            index = db.find_record_using_key("id", value)
            if index != -1:
                print(f"Record found at index {index}:")
                print(db.get_heading_string())
                print(db.get_record_string(index))
                print("Are you sure you want to delete this record? (y/n): ")
                confirm = input()
                if confirm == "y":
                    db.delete_using_key("id", value)
            else:
                print("Record not found.")
        elif choice == 8:
            print(db.get_heading_string())
            print(db.__str__())
        elif choice == 9:
            break

def select_menu_option():
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")
        if choice in [str(i) for i in range(1, 10)]:
            return int(choice)
        else:
            print("Invalid choice. Please try again.")
def print_menu():
    print("Menu:")
    print("1. Delete first entry")
    print("2. Sum column (id)")
    print("3. Largest column value (birth year)")
    print("4. Sort entries by string key (last name)")
    print("5. Sort entries by numeric key (salary)")
    print("6. Save to file")
    print("7. Delete using key (id)")
    print("8. Display all records")
    print("9. Exit")

if __name__ == "__main__":
    main()