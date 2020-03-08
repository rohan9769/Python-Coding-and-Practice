# mode = r means read,w means write,a allows to append

with open('test.txt',mode='a') as my_file:
    text = my_file.write(' Hi my name is bob')
    print(text)
    #print(my_file.readlines())

with open('sad.txt',mode='w') as my_file: #write also creates a new file
    text = my_file.write(' Hi my name is bob')
    print(text)
    #print(my_file.readlines())