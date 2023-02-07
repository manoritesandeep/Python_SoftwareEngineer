from employee import Employee


rolf = Employee(15.0)
print(rolf.weekly_salary())

rolf.promote(5.0)
print(rolf.weekly_salary())