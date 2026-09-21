class Employee:
    def __init__(self, id_num=0, first_name="no data", last_name="no data"):
        self.setId(id_num)
        self.setFirstName(first_name)
        self.setLastName(last_name)


    def setData(self, id_num, first_name, last_name):
        self.setId(id_num)
        self.setFirstName(first_name)
        self.setLastName(last_name)

    def setId(self, id_num):
        self.__id_num = id_num
    def setFirstName(self, first_name):
        self.__first_name = first_name
    def setLastName(self, last_name):
        self.__last_name = last_name

    def getId(self):
        return self.__id_num
    def getFirstName(self):
        return self.__first_name
    def getLastName(self):
        return self.__last_name

    def getData(self):
        return f"{self.__id_num} {self.__first_name} {self.__last_name}"

    def earnings(self):
        return "0"