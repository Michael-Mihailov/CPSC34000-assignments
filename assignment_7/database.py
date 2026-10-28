from dataclasses import dataclass

@dataclass
class Entry:
    id: int
    name_last: str
    name_first: str
    department: str
    role: str
    birth_year: int
    sex: str
    salary: int
    agrees: str
    unknown_float: float



class Database:
    def __init__(self, file_name):
        self.__entries = self.__read_file_to_list(file_name)


    # 6.1
    def delete_first_entry(self):
        if self.__entries:
            del self.__entries[0]
            return True
        return False

    # 6.3
    def largest_column_value_index(self, column_name):
        largest_value = None
        largest_index = -1
        for i, entry in enumerate(self.__entries):
            value = getattr(entry, column_name)
            if largest_value is None or value > largest_value:
                largest_value = value
                largest_index = i
        return largest_index

    # 6.6
    def save_to_file(self, file_name):
        text = self.get_heading_string()
        text += "\n"
        text += self.__str__()
        with open(file_name, "w") as file:
            file.write(text)

    # 6.7
    def delete_using_id(self, value):
        location = self.find_record_using_id(value)
        if location != -1:
            self.delete_record_at_address_location(location)
            return True
        return False
    def delete_record_at_address_location(self, location):
        if location >= 0 and location < len(self.__entries):
            del self.__entries[location]

    # 6.9
    def __str__(self):
        res = ""
        for entry in self.__entries:
            res += "%-20d%-20s%-20s%-20s%-20s%-20d%-20s%-20d%-20s%-20.2f\n" % (entry.id, entry.name_last, entry.name_first, entry.department, entry.role, entry.birth_year, entry.sex, entry.salary, entry.agrees, entry.unknown_float)
        return res
    def get_heading_string(self):
        return "%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % ("ID", "Last Name", "First Name", "Department", "Role", "Birth Year", "Sex", "Salary", "Agrees", "Unknown Float")
    def get_record_string(self, location):
        if location >= 0 and location < len(self.__entries):
            entry = self.__entries[location]
            return "%-20d%-20s%-20s%-20s%-20s%-20d%-20s%-20d%-20s%-20.2f\n" % (entry.id, entry.name_last, entry.name_first, entry.department, entry.role, entry.birth_year, entry.sex, entry.salary, entry.agrees, entry.unknown_float)
        else:
            return "Invalid location"

    def __read_file_to_list(self, file_name):
        # PRECONDITION: file is sorted in ascending order
        res = []
        file = open(file_name, "r")
        for line in file:
            values = line.replace(","," ").strip().split()
            entry = Entry(
                id=int(values[0]),
                name_last=values[1],
                name_first=values[2],
                department=values[3],
                role=values[4],
                birth_year=int(values[5]),
                sex=values[6],
                salary=int(values[7]),
                agrees=values[8],
                unknown_float=float(values[9])
            )
            res.append(entry)
        file.close()
        return res

    # Assignment 7 feature
    def add_record_using_id(self, entry):
        if self.find_record_using_id(entry.id) != -1:
            return False # id already exists

        position = self.__find_insertion_position(entry.id)
        self.__entries.insert(position, entry)
        return True

    # Assignment 7 feature
    def update_record_using_id(self, value, column_name, new_value):
        if column_name not in ("name_last", "name_first", "department", "role", "birth_year", "sex", "salary", "agrees", "unknown_float"):
            return False

        # Find the existing record
        location = self.find_record_using_id(value)

        if location == -1:
            return False

        # The primary key cannot be updated
        if column_name == "id":
            return False

        # Create a replacement record with the updated field
        entry = self.__entries[location]
        updated_entry = Entry(
            id=entry.id,
            name_last=new_value if column_name == "name_last" else entry.name_last,
            name_first=new_value if column_name == "name_first" else entry.name_first,
            department=new_value if column_name == "department" else entry.department,
            role=new_value if column_name == "role" else entry.role,
            birth_year=new_value if column_name == "birth_year" else entry.birth_year,
            sex=new_value if column_name == "sex" else entry.sex,
            salary=new_value if column_name == "salary" else entry.salary,
            agrees=new_value if column_name == "agrees" else entry.agrees,
            unknown_float=new_value if column_name == "unknown_float" else entry.unknown_float
        )

        self.__entries[location] = updated_entry
        return True

    # HELPER METHODS
    # uses binary search
    def find_record_using_id(self, value):
        length = len(self.__entries)
        low = 0
        high = length - 1
        while (low <= high):
            mid = (low + high) // 2
            if self.__entries[mid].id < value:
                low = mid + 1
            elif self.__entries[mid].id > value:
                high = mid - 1
            else:
                return mid
        return -1
    # Finds the insertion position for an ID
    def __find_insertion_position(self, value):
        low = 0
        high = len(self.__entries)
        while low < high:
            mid = (low + high) // 2
            if self.__entries[mid].id < value:
                low = mid + 1
            else:
                high = mid
        return low