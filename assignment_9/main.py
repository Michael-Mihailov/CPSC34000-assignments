from record import Record
from hashtable import HashTable



def main():
    hashTable = HashTable(500) # This is a load factor of 1.0 since the input file is also 500 lines

    with open("electric_car.txt", "r") as file:
        for line in file:
            data = line.strip().split("\t")
            hashTable.addRecord(Record(*data))

    while True:
        print("\nMain Menu")
        print("A. Add a new record")
        print("B. Find a record")
        print("C. Quit")
        choice = input("Option: ").upper()

        if choice == "A":
            vinNum = input("VIN: ")
            city = input("City: ")
            state = input("State: ")
            postalCode = input("Postal Code: ")
            modelYear = input("Model Year: ")
            make = input("Make: ")
            model = input("Model: ")

            record = Record(vinNum, city, state, postalCode, modelYear, make, model)
            if hashTable.addRecord(record):
                print("Record added")
            else:
                print("FAILED: That VIN already exists")


        elif choice == "B":
            key = input("Enter VIN: ")
            record = hashTable.findRecord(key)

            if record is None:
                print("Record not found")
            else:
                print("Record:", record)
                print("D. Delete record")
                print("E. Update record")
                print("F. Return to main menu")
                choice = input("Option: ").upper()

                if choice == "D":
                    confirm = input("Delete this record? (y/n): ").lower()
                    if confirm == "y":
                        hashTable.deleteRecord(key)
                        print("Record deleted")

                elif choice == "E":
                    print("G. City")
                    print("H. State")
                    print("I. Postal Code")
                    print("J. Model Year")
                    print("K. Make")
                    print("L. Model")
                    print("M. Return to main menu")
                    field = input("Field to update: ").upper()

                    updateFields = {
                        "G": ("City", "city"),
                        "H": ("State", "state"),
                        "I": ("Postal Code", "postalCode"),
                        "J": ("Model Year", "modelYear"),
                        "K": ("Make", "make"),
                        "L": ("Model", "model"),
                    }
                    if field in updateFields:
                        name, attribute = updateFields[field]
                        setattr(record, attribute, input("New " + name + ": "))
                        print("Record updated")

        elif choice == "C":
            break



if __name__ == "__main__":
    main()