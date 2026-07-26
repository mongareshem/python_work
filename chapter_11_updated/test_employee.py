import pytest
from employee_class import Employee

@pytest.fixture()
def employee():
    employee = Employee('Shem', 'Samson', 10000)
    return employee


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 15000

def test_give_custom_raise(employee):
    employee.give_raise(7_000)
    assert employee.annual_salary == 17000