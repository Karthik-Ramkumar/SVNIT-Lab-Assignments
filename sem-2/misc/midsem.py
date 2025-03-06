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
    college_name = "SVNIT" # class attribute
    def __init__(self,name,rollno):                                 # obj atrr > class atrr
        self.name = name # object attribute
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