# a = 10
# def confusion(b):
#     print(b)
#     global a
#     a=90
#
#
# confusion(300)
# print(a)


total = 0
def count():
    global total
    total = total+1
    return total

print(count())

x = "Hello"[0]
print(x)