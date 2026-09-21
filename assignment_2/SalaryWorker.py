from Employee import Employee


class SalaryWorker(Employee):
    def __init__(self, id_num=0, first_name="no data", last_name="no data", salary=0):
        super().__init__(id_num, first_name, last_name)
        self.setSalary(salary)


    def setData(self, id_num, first_name, last_name, salary):
        super().setData(id_num, first_name, last_name)
        self.setSalary(salary)

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    def displayData(self):
        return f"{self.getData()} {self.getSalary()}"

    def earnings(self):
        weekly_pay = self.getSalary() / 52
        return f"{self.getData()} {weekly_pay:.2f}"