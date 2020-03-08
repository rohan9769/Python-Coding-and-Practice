import re

pattern = re.compile(r"[a-zA-Z].([a])") #r stands for raw string

string = 'search this inside of this text please! Ron'


#a = re.search('ear',string)
a = pattern.search(string)

b = pattern.findall(string) #finds all the instances od the match

c = pattern.fullmatch(string)

d = pattern.match(string)
print(a.group(2))