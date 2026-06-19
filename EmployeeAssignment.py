class Employee:
    def __init__(self, name, emp_number):
        self.__name = name
        self.__emp_number = emp_number

    def set_name(self, name):
        self.__name = name

    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    def get_name(self):
        return self.__name

    def get_emp_number(self):
        return self.__emp_number


class ProductionWorker(Employee):
    def __init__(self, name, emp_number, shift, pay_rate):
        Employee.__init__(self, name, emp_number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate


class ShiftSupervisor(Employee):
    def __init__(self, name, emp_number, salary, bonus):
        Employee.__init__(self, name, emp_number)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus


def main():
    worker = ProductionWorker(
        input("Employee Name: "),
        input("Employee Number: "),
        int(input("Shift (1=Day, 2=Night): ")),
        float(input("Hourly Pay Rate: "))
    )

    print("\nProduction Worker Information")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_emp_number())
    print("Shift:", worker.get_shift())
    print("Pay Rate:", worker.get_pay_rate())

    supervisor = ShiftSupervisor(
        input("\nSupervisor Name: "),
        input("Supervisor Number: "),
        float(input("Annual Salary: ")),
        float(input("Annual Bonus: "))
    )

    print("\nShift Supervisor Information")
    print("Name:", supervisor.get_name())
    print("Employee Number:", supervisor.get_emp_number())
    print("Salary:", supervisor.get_salary())
    print("Bonus:", supervisor.get_bonus())


main()
