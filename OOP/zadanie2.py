class Employee:

    def __init__(self, name, last_name, rate):
        self.name = name
        self.last_name = last_name
        self.rate = rate
        self.registered_time = 0

    def register_time(self, time):
        self.registered_time = time

    def pay_salary(self):
        if self.registered_time < 8:
            to_pay = self.rate * self.registered_time
        else:
            to_pay = 8 * self.rate + (self.registered_time - 8) * self.rate * 2
        self.registered_time = 0
        return to_pay

def test_employee_init():
    employee = Employee("Rafał", "Korzeniewski", 200)
    assert employee.name == "Rafał"
    assert employee.last_name == "Korzeniewski"
    assert employee.rate == 200

def test_employee_register_time():
    employee = Employee("Rafał", "Korzeniewski", 200)
    employee.register_time(5)
    assert employee.registered_time == 5

def test_employee_pay_salary():
    employee = Employee("Rafał", "Korzeniewski", 200)
    assert employee.pay_salary() == 0
    employee.register_time(5)
    assert employee.pay_salary() == 5*200
    assert employee.pay_salary() == 0
    employee.register_time(10)
    assert employee.pay_salary() == 8*200+2*2*200
    assert employee.pay_salary() == 0

