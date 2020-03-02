username = input('Username :')
password = str(input('Password :'))
c = len(password)
print(c)
pass_length = '*'*c
print(f"Hey {username},your password {pass_length} is {c} characters long")

