# a = [5,4,10,1,6,2]
# for i in range(len(a)):
#     temp = a[i]
#     k=i
#     while k>0 and a[k-1]>temp:
#         a[k] = a[k-1]
#         k-=1
#     a[k] = temp
#
# print(a)

a =  [5,4,10,1,6,2]
for i in range(1,len(a)):
    temp = a[i]
    j=i
    while j>0 and a[j-1]>temp:
        a[j] = a[j-1]
        j-=1
    a[j] = temp
print(a)
