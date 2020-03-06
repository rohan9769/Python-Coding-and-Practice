#
#
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
#
# my_list = make_list(100)
# print(my_list)
# print(list(range(20)))

#GENERAL WAY TO CREATE A GENERATOR
def generator_function(n):
    for i in range(n):
        yield i #yield pauses the function

g = generator_function(20)
print(next(g))
print(next(g))
print(next(g))

# for i in generator_function(50):
#     print(i)