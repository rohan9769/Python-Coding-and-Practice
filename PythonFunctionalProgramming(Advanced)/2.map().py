#Map,filter,zip are very common functions

#1)Map
# map(action,data on which action should be take)

def multi_by2(i):
    # new_list = []
    # for i in li:
    #     new_list.append(i*2)
    # return new_list
    return i*2

print(list(map(multi_by2,[1,2,3,4,5])))

