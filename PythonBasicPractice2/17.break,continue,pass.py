#break,continue,pass
#break - breaks instantly out of the block,say a loop
#continue - skips all the statement following it
#pass - doesn't do much,passes control to next line

my_list = [1,2,3,4]
for i in my_list:
    print(i)
    continue

my_list2 = [5,56,6,8]
for i in my_list2:
    print(i)
    break