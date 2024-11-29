from abc import ABC,abstractmethod
import math
class Shape(ABC):
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        Area=3.14*self.radius*self.radius
        print("area of circle:",Area)
class Retangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        Area=self.length*self.width
        print("area of retangle:",Area)

circle=Circle(radius=4)
circle.area()
retangle=Retangle(length=12,width=6)
retangle.area()
