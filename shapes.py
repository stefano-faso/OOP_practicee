import math


class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_width(self):
        print(f"Width: {self.width}")

    def get_height(self):
        print(f"Height: {self.height}")

    def area(self):
        area = self.width * self.height
        print(area)

    def perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        print(perimeter)


class Rectangle(Shape):
    pass


class Square(Shape):
    def __init__(self,side):
        super().__init__(side, side)
        self.side = side

    def area(self):
        area = self.side * self.side
        print(area)

    def perimeter(self):
        perimeter = self.side * 4
        print(perimeter)


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)
        self.base = base
        self.height = height

    def area(self):
        area = round(0.5*(self.base * self.height))
        print(area)

    def perimeter(self):
        hyp = int(round(math.sqrt((self.base ** 2) + (self.height ** 2)),0))
        perimeter = hyp + self.base + self.height
        print(perimeter)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.radius = radius

    def area(self):
        area = int((math.pi * self.radius)**2)
        print(area)


#class Cube(Square):


a = Shape(10,10)
a.area()
a.perimeter()
r = Rectangle(10,10)
r.area()
r.perimeter()
s = Square(10)
s.area()
s.perimeter()
t = Triangle(10,10)
t.area()
t.perimeter()
c = Circle(10)
c.area()