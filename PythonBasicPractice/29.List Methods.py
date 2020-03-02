box = [1,2,3,4,5,6]
print(len(box)) #counts from 1 not 0

#adding element
box.append(45)
new_box = box
print(new_box)

box.insert(2,33) #insert modifies,does not create a new copy pf the list
print(new_box)

box.extend([7,8,9])
print(new_box)


#Removing
box.pop(2) #removes element at index 2
print(new_box)
box.pop() #removes the last element in the list
print(new_box)

box.remove(45) #removes value 45 from the list
print(new_box)

#clear() removes everyting from the list