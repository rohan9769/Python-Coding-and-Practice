basket = ['a','c','d','b','e']

basket.sort() #sorts in order
print(basket)

sorted(basket)
print(basket)
#Sorted produces a new array,Sorted is a method,Sorted doesn't modify creates a new copy


new_basket = basket.copy()
print(new_basket)

basket.reverse()
print(basket)