import math

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses.")

    def perimeter(self):
        raise NotImplementedError("Perimeter method must be implemented by subclasses.")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage:
rect = Rectangle(5, 10)
print(f"Rectangle Area: {rect.area()}")        # Output: 50
print(f"Rectangle Perimeter: {rect.perimeter()}") # Output: 30

circle = Circle(7)
print(f"Circle Area: {circle.area()}")          # Output: 153.93804001791397
print(f"Circle Perimeter: {circle.perimeter()}")   # Output: 43.982297150257104