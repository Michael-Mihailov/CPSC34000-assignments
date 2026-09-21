from Employee import Employee
from HourlyWorker import HourlyWorker
from SalaryWorker import SalaryWorker


def main():
    employees = []

    with open("employee.txt", "r") as file:
        for line in file:
            data = line.split()

            if not data:
                continue

            employee_type = data[0]

            if employee_type == "S":
                # S ID First Last Salary
                employee = SalaryWorker(id_num=int(data[1]), first_name=data[2], last_name=data[3], salary=float(data[4]))
                employees.append(employee)
            elif employee_type == "H":
                # H ID First Last Hours PayRate
                employee = HourlyWorker(id_num=int(data[1]), first_name=data[2], last_name=data[3], hours_worked=float(data[4]), pay_rate=float(data[5]))
                employees.append(employee)
            elif employee_type == "C" or employee_type == "P":
                # I wasn't assigned these employee types, skip them
                continue

    print("***** Employee Report *****")
    print(f"{'Employee':<20}{'Employee':<15}{'First':<15}{'Last':<15}{'Weekly':<15}")
    print(f"{'Type':<20}{'Number':<15}{'Name':<15}{'Name':<15}{'Pay':<15}")

    for employee in employees:
        if isinstance(employee, SalaryWorker):
            employee_type = "Salary Worker"
        elif isinstance(employee, HourlyWorker):
            employee_type = "Hourly Worker"
        else:
            employee_type = "Employee"

        print(
            f"{employee_type:<20}"
            f"{employee.getId():<15}"
            f"{employee.getFirstName():<15}"
            f"{employee.getLastName():<15}"
            f"{employee.earnings().split()[-1]:<15}"
        )


if __name__ == "__main__":
    main()