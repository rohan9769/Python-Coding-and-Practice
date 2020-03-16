from student import *
s = Student()
#Storing data
s.setaddress('Kama Lane')
s.setid(10)
s.setname('Rhe')
s.setmarks(25)

#retrieve data and display
print(f'id is {s.getid()}')
print(f'Name is {s.getname()}')
print(f'Address is {s.getaddress()}')
print(f'Marks is {s.getmarks()}')