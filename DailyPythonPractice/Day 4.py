# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# sen = input()
# u=0
# l=0
# for i in sen:
#     if i.isupper():
#         u+=1
#     elif i.islower():
#         l+=1
#     else:
#         continue
#
# print(f'UPPER CASE {u}')
# print(f'LOWER CASE {l}')

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:     9
# Then, the output should be:
# 11106

n = input()
print(int(n)+int(n*2)+int(n*3)+int(n*4))