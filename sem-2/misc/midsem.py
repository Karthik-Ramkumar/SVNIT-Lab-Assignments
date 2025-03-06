d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(key, value)


# variables stored inside a class is called attributes
class Student:
    college_name = "SVNIT"                                          # class attribute
    def __init__(self,name,rollno):                                 # obj atrr > class atrr
        self.name = name                                            # object attribute
        self.rollno = rollno
        print(name)     # prints automatically cause self is called on creation of object
        print(rollno)
    
    def welcome(self):
        print(f"Welcome {self.name} to {self.college_name}")

std = Student('Karthik','U24AI001')
print(std.name)
print(std.college_name)
# or
print(Student.college_name)




class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type) # calling parent class's constructor

car1 = ToyotaCar("prius", "electric")
car1.start()



# class method
class car:
    name = "toyota"
    def changeName(self, name):
        self.name = name
        self.__class__.name = 'honda'  # accessing class from inside method
        car.name = 'honda'
    
    @classmethod
    def changeName(cls, Name):          # cls is class
        cls.name = Name  


class Car:
    def __init__(self, brand, speed):
        self.brand = brand  
        self.speed = speed

    @property
    def speed(self):  # Getter
        return self._speed

    @speed.setter
    def speed(self, value):  # Setter
            self._speed = value

car1 = Car("Toyota", 120)
print(car1.brand)  # Directly accessing public variable
print(car1.speed)  # Using @property getter

car1.speed = 150  # Using @property setter
print(car1.speed)
