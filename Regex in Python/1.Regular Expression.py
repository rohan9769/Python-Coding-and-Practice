import re

pattern = re.compile('ear')

string = 'search in this text please!'
#a = re.search('ear',string)
a = pattern.search(string)
print(a)
b = pattern.findall(string) #finds all the instances od the match
print(b)
c = pattern.fullmatch(string)
print(c)
d = pattern.match(string)
print(d)
 # print(a.span()) #gives the index where it occurs
 # print(a.start()) #gives index where text starts
 # print(a.end()) #gives index where text ends
 # print(a.group()) #return part where the text was a match
