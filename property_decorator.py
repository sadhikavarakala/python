import math

class Circle:
    def __init__(self, radius):
        self._radius = radius # used _radius for clarity 

    @property
    def radius(self):
        return self._radius 
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return math.pi * (self._radius ** 2)
    
c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.area}")

c.radius = 10
print(f"Updated Radius: {c.radius}")
print(f"Updated Area: {c.area:2f}")

'''
@property on area: makes it act like a read-only attribute
@radius.setter: allows setting the radius with a check
Never need to call circle.are() - just access .area like a variable
'''