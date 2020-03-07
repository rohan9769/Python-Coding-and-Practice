from collections import *

li = [1,2,3,4,5,6,7]
print(Counter(li)) #Creates a dictionary that keeps track of how many items an item occured
sentence = 'Hey there,How are you?'
print(Counter(sentence))

#defaultdict allows us to access a key like this but give it a default value
dictionary = defaultdict(lambda:5,{'a':1,'b':2})
print(dictionary['d'])

#OrderedDeict()
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d1 = OrderedDict()
d1['b'] = 2
d1['a'] = 1

print(d1 == d)
