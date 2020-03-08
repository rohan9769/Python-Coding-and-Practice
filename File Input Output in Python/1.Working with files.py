my_file = open('test.txt')
print(my_file)

# my_file.seek(0) #Moves cursor to specified index
# print(my_file.read()) #reads the content of the file
# my_file.seek(0)
# print(my_file.read())

#print(my_file.readline()) #reads the file and prints only the first line,writing it again will print next line
print(my_file.readlines()) #reads entire file

my_file.close() #always have to close the file after opening it 