#list unpacking
# a,b,c = [1,2,3]
# print(a,b)

a,b,c,*other,d = [1,2,3,4,5,6,7,8]
print(a,b)
print(other)
print(c)
print(d)