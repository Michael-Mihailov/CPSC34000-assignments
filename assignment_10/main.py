from tree import Tree


def load_tree(filename):
    tree = Tree()
    file = open(filename, "r")
    for line in file:
        fields = line.split()
        record = (int(fields[0]), fields[1], float(fields[2]), fields[3], fields[4], int(fields[5]))
        tree.insert(record)
    file.close()
    return tree


def add_new_record(tree):
    key = int(input("Item number: "))
    item = input("Item: ")
    cost = float(input("Cost: "))
    item_type = input("Type: ")
    category = input("Category: ")
    quantity = int(input("Quantity in stock: "))
    tree.insert((key, item, cost, item_type, category, quantity))


def update_record(tree, node):
    print("1. Item Number")
    print("2. Item")
    print("3. Cost")
    print("4. Type")
    print("5. Category")
    print("6. Quantity in Stock")
    choice = input("Which value do you want to update? ")

    new_data = list(node.data)
    if choice == "1":
        key = int(input("New item number: "))
        if key == node.key:
            print("Item number was not changed")
            return
        if tree.search(key) != None:
            print("INVALID: Item Already Exists")
            return
        new_data[0] = key
        tree.delete(node.key)
        tree.insert(tuple(new_data))
    elif choice == "2":
        new_data[1] = input("New item: ")
        node.data = tuple(new_data)
    elif choice == "3":
        new_data[2] = float(input("New cost: "))
        node.data = tuple(new_data)
    elif choice == "4":
        new_data[3] = input("New type: ")
        node.data = tuple(new_data)
    elif choice == "5":
        new_data[4] = input("New category: ")
        node.data = tuple(new_data)
    elif choice == "6":
        new_data[5] = int(input("New quantity: "))
        node.data = tuple(new_data)
    else:
        print("Invalid Menu Choice")
        return

    print("Updated Record")


def modify_record(tree):
    key = int(input("Enter the item number: "))
    node = tree.search(key)
    if node is None:
        print("Item number not found")
        return

    print()
    node.print_record()
    print()
    
    print("1. Change a value")
    print("2. Delete this record")
    print("3. Go back")
    choice = input("Choose an option: ")

    if choice == "1":
        update_record(tree, node)
    elif choice == "2":
        tree.delete(key)
        print("Deleted Record")
    elif choice == "3":
        return
    else:
        print("Invalid Menu Choice")
        return


def main():
    tree = load_tree("garden.txt")

    while True:
        print()
        print("Main Options:")
        print("1. Add a tuple")
        print("2. Find, change, or delete a node")
        print("3. Display the tree in item number order")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_record(tree)
        elif choice == "2":
            modify_record(tree)
        elif choice == "3":
            tree.display()
        elif choice == "4":
            print("Exit Complete")
            break
        else:
            print("Invalid Menu Choice")



if __name__ == "__main__":
    main()