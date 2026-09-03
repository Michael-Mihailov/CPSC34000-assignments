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

    # 6.2
    def sum_column(self, column_name):
        total = 0
        for entry in self.__entries:
            total += getattr(entry, column_name)
        return total

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

    # 6.4
    def sort_entries_string_key(self, column_name):
        if type(getattr(self.__entries[0], column_name)) is str:
            self.__sort_entries_ascending(column_name)

    # 6.5
    def sort_entries_numeric_key(self, column_name):
        if type(getattr(self.__entries[0], column_name)) is int or type(getattr(self.__entries[0], column_name)) is float:
            self.__sort_entries_descending(column_name)

    # 6.6
    def save_to_file(self, file_name):
        text = self.get_heading_string()
        text += "\n"
        text += self.__str__()
        with open(file_name, "w") as file:
            file.write(text)

    # 6.7
    def delete_using_key(self, column_name, value):
        location = self.find_record_using_key(column_name, value)
        if location != -1:
            self.delete_record_at_address_location(location)
    def find_record_using_key(self, column_name, value):
        for i in range(len(self.__entries)):
            if getattr(self.__entries[i], column_name) == value:
                return i
        return -1
    def delete_record_at_address_location(self, location):
        if location >= 0 and location < len(self.__entries):
            del self.__entries[location]

    # 6.8 SKIP THIS ONE

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


    def __sort_entries_ascending(self, column_name):
        self.__entries.sort(key=lambda entry: getattr(entry, column_name))
    def __sort_entries_descending(self, column_name):
        self.__entries.sort(key=lambda entry: getattr(entry, column_name), reverse=True)

    def __read_file_to_list(self, file_name):
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