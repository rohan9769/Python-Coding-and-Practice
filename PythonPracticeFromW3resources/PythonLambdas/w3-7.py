f = lambda str,sub:True if str.startswith(sub) else False
val = f('This is a book','Th')
print(val)