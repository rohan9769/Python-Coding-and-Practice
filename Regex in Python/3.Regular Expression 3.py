import re
pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
string = 'ron@xyz.com'
a = pattern.search(string)
print(a)

pattern2 = re.compile(r'[A-za-z0-9$#%@]{8,}\d')
check = 'ron@34527'
b = pattern2.fullmatch(check)
print(b)