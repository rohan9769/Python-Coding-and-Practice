class Toy:
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name' : 'yoyo',
            'haspets':False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
         print('yess??')

    def __getitem__(self, i):
        return self.my_dict


action_fig = Toy('Red',55)

print(action_fig.__str__()) #same as doing str(action_fig)
print(len(action_fig))
print(action_fig())
print(action_fig['name'])