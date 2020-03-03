#Return keyword automatically exits the function

# def add(a,b):
#     return a+b
#
# print(add(3,4))

#Nested Functions
def add(a,b):
    def add1(a,b):
        return a+b
    return add1(a,b)

total = add(10,20)
print(total)