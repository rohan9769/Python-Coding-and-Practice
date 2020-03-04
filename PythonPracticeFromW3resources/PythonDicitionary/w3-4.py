# Write a Python script to check whether a given key already exists in a dictionary.

dic1 = {1:10,2:20,3:30}

def key_present(x):
    if x in dic1:
        print("Present")
    else:
        print("Absent")

key_present(2)