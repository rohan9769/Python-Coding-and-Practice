walmart_cart = ['pens','pencils','eraser','food','toys','cars','milk']
print(walmart_cart[0:2])
walmart_cart[0] = 'Laptop'
print(walmart_cart)
print(walmart_cart[1:3])
print(walmart_cart[0:3])
new_cart = walmart_cart
new_cart[0] = 'Mouse'
print(new_cart)
print(walmart_cart)

new_cart = walmart_cart[:]
new_cart[0] = 'Mou'
print(new_cart)
