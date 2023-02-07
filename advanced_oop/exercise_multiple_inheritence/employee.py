from salary import Salary
from promotable import Promotable


class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate  # hourly salary

    def weekly_salary(self) -> float:
        return self.calculate(40)
