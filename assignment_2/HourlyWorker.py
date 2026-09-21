from Employee import Employee


class HourlyWorker(Employee):
    def __init__(self, id_num=0, first_name="no data", last_name="no data", hours_worked=0, pay_rate=0):
        super().__init__(id_num, first_name, last_name)
        self.setHoursworked(hours_worked)
        self.setPayrate(pay_rate)

    def setData(self, id_num, first_name, last_name, hours_worked, pay_rate):
        super().setData(id_num, first_name, last_name)
        self.setHoursworked(hours_worked)
        self.setPayrate(pay_rate)

    def setHoursworked(self, hours_worked):
        self.__hours_worked = hours_worked
    def setPayrate(self, pay_rate):
        self.__pay_rate = pay_rate

    def getHoursworked(self):
        return self.__hours_worked
    def getPayrate(self):
        return self.__pay_rate

    def displayData(self):
        return f"{self.getData()} {self.getHoursworked()} {self.getPayrate()}"

    def earnings(self):
        if self.getHoursworked() <= 40:
            weekly_pay = self.getHoursworked() * self.getPayrate()
        else:
            regular_pay = 40 * self.getPayrate()
            overtime_hours = self.getHoursworked() - 40
            overtime_pay = overtime_hours * self.getPayrate() * 1.5
            weekly_pay = regular_pay + overtime_pay

        return f"{self.getData()} {weekly_pay:.2f}"