class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            combined_salary = self.salary + other.salary
            return Employee("Combined", combined_salary)  # Or a more descriptive name
        else:
            raise TypeError("Can only add Employee objects.")

    def __sub__(self, other):
        if isinstance(other, Employee):
            salary_difference = self.salary - other.salary
            return salary_difference  # Return just the difference
        else:
            raise TypeError("Can only subtract Employee objects.")

    def __lt__(self, other):  # Less than
        if isinstance(other, Employee):
            return self.salary < other.salary
        else:
            return NotImplemented  # Important for other comparisons to work

    def __le__(self, other):  # Less than or equal to
        if isinstance(other, Employee):
            return self.salary <= other.salary
        else:
            return NotImplemented

    def __gt__(self, other):  # Greater than
        if isinstance(other, Employee):
            return self.salary > other.salary
        else:
            return NotImplemented

    def __ge__(self, other):  # Greater than or equal to
        if isinstance(other, Employee):
            return self.salary >= other.salary
        else:
            return NotImplemented

    def __eq__(self, other):  # Equal to
        if isinstance(other, Employee):
            return self.salary == other.salary
        else:
            return NotImplemented

    def __ne__(self, other):  # Not equal to
        if isinstance(other, Employee):
            return self.salary != other.salary
        else:
            return NotImplemented

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# Example usage:
emp1 = Employee("Alice", 60000)
emp2 = Employee("Bob", 75000)

combined_emp = emp1 + emp2
print(combined_emp)  # Output: Name: Combined, Salary: 135000

salary_diff = emp2 - emp1
print(salary_diff)  # Output: 15000

print(emp1 < emp2)  # Output: True
print(emp1 == emp2)  # Output: False