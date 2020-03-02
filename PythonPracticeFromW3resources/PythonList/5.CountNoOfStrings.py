words = ['abc','xyz','aba','1221']
# n = int(input("Enter Length of List"))
# for i in range(n):
#     x = input("Enter the String")
#     lst.append(x)

print(words)

count = 0
for i in words:
    if len(i)>=2 and (i[0]==i[-1:]):
        count = count+1

print(count)


