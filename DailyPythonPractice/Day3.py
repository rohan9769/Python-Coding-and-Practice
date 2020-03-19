# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# x = input().split()
# print(' '.join(x))
# y = set(x)
# print(' '.join(y))
# print(' '.join(sorted(y)))



# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

# nums = [int(x) for x in input().split(',')]
# vals = []
# for i in range(len(nums)):
#     if nums[i]%5==0:
#         vals.append(nums[i])
# print(vals)
#

# Write a program that accepts a sentence and calculate the number of letters and digits.
#
# Suppose the following input is supplied to the program:
#
# hello world! 123
# Then, the output should be:
#
# LETTERS 10
# DIGITS 3

x = input()
print(x)
l=0
d=0
for i in x:
    if i.isalpha():
        l = l+1
    elif i.isnumeric():
        d = d+1
    else:
        continue

print(f'LETTERS : {l}')
print(f'DIGITS : {d}')