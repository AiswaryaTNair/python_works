
from abc import ABC, abstractmethod
class Shape(ABC):   
    def side(self):   
        pass  
    def area(self):
        pass
    
class Circle(Shape):
    def side(self):
        print('circle has no side')
    def area(self):
        r=int(input('enter the radius'))
        area=3.14*(r*r)
        print('area of circle is',area)
class Triangle(Shape):
    def side(self):
        print('triangle has 3 sides')
    def area(self):
        b=int(input('enter the base'))
        h=int(input('enter the height'))
        area=(b*h)/2
        print('area of triangle is', area)
class Rectangle(Shape):
    def side(self):
        print('rectangle has 4 sides')
    def area(self):
        a=int(input('enter the length'))
        b=int(input('enter the width'))
        area=a*b
        print('area of rectangle is',area)


circle=Circle()
circle.side()
circle.area()

triangle=Triangle()
triangle.side()
triangle.area()

rectangle=Rectangle()
rectangle.side()
rectangle.area()


'''
from abc import ABC, abstractmethod
class shape(ABC):   
    def area(self):   
        pass  
    
class circle(shape):
    def area(self):
        r=int(input('enter the radius'))
        area=3.14*(r*r)
        print('area of circle is',area)
class triangle(shape):
    def area(self):
        b=int(input('enter the base'))
        h=int(input('enter the height'))
        area=(b*h)/2
        print('area of triangle is', area)
class rectangle(shape):
    def area(self):
        a=int(input('enter the length'))
        b=int(input('enter the width'))
        area=a*b
        print('area of rectangle is',area)

circle=circle()
circle.area()

triangle=triangle()
triangle.area()

rectangle=rectangle()
rectangle.area()
'''
