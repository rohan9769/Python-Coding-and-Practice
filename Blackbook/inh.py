#Program to use the teacher class
from teacher import *
t = Teacher()

#Storing data
t.setaddress('Kama Lane')
t.setid(10)
t.setname('Rhea')
t.setsalary(50000)

#retrieve data and display
print(f'id is {t.getid()}')
print(f'Name is {t.getname()}')
print(f'Address is {t.getaddress()}')
print(f'Salary is {t.getsalary()}')