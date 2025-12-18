from abc import ABC, abstractmethod

class employee:
    def calculate_salary(self): 
        pass

class PartTimeEmployee(employee):
    def __init__(self, hourly_wage, hours_worked):
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked

p= PartTimeEmployee(20, 80)
print(p.calculate_salary())  