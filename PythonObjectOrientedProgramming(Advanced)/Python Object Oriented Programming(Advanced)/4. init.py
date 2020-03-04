class Rectangle:

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calcPerimeter(self):
        p = 2*(self.l + self.b)
        return p

    def calcArea(self):
        a = self.l * self.b
        return a


Rect1 = Rectangle(5,4)
print(Rect1.calcPerimeter())
print(Rect1.calcArea())