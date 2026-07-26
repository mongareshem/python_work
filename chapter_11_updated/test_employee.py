from employee_class import Employee

def test_give_default_raise():
    employee = Employee('Shem', 'Samson', 10000)
    employee.give_raise()
    assert employee.annual_salary == 15000