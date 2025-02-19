import math

class Vector2D:
    class Vector2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def magnitude(self):
            return math.sqrt(self.x**2 + self.y**2)

        def rotation(self):  # Angle with respect to x-axis
            return math.atan2(self.y, self.x)

        @staticmethod
        def distance(v1, v2):
            return math.sqrt((v2.x - v1.x)**2 + (v2.y - v1.y)**2)

        @staticmethod
        def dot_product(v1, v2):
            return v1.x * v2.x + v1.y * v2.y

        @staticmethod
        def cross_product(v1, v2):
            return v1.x * v2.y - v1.y * v2.x  # Returns a scalar in 2D

class Vector3D(Vector2D):  # Inherits from Vector2D
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Call the 2D constructor
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @staticmethod
    def distance(v1, v2):
        return math.sqrt((v2.x - v1.x)**2 + (v2.y - v1.y)**2 + (v2.z - v1.z)**2)

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross_product(v1, v2):
        return Vector3D(v1.y * v2.z - v1.z * v2.y,
                        v1.z * v2.x - v1.x * v2.z,
                        v1.x * v2.y - v1.y * v2.x)

    def __str__(self): #for printing the vector nicely
      return f"({self.x}, {self.y}, {self.z})"



# Example usage:
v2d1 = Vector2D(3, 4)
v2d2 = Vector2D(1, 2)

print(f"2D Magnitude: {v2d1.magnitude()}")
print(f"2D Distance: {Vector2D.distance(v2d1, v2d2)}")
print(f"2D Dot Product: {Vector2D.dot_product(v2d1, v2d2)}")
print(f"2D Cross Product: {Vector2D.cross_product(v2d1, v2d2)}")


v3d1 = Vector3D(1, 2, 3)
v3d2 = Vector3D(4, 5, 6)

print(f"3D Magnitude: {v3d1.magnitude()}")
print(f"3D Distance: {Vector3D.distance(v3d1, v3d2)}")
print(f"3D Dot Product: {Vector3D.dot_product(v3d1, v3d2)}")
print(f"3D Cross Product: {Vector3D.cross_product(v3d1, v3d2)}")

print(v3d1) #output: (1, 2, 3)