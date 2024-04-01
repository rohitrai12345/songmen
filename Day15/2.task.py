#•Create a class Person with instance attributes name and age. Create a method get_details in this class to print name and age.
#has context menu

class person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def get_details(self):
        return (f" Person name is {self.name} adn age is {self.age}.")
v=person('Arun', 22)
print(v.get_details())

# Create another class Employee with attributes salary and designation and inherits the Person class. Create a method get_details in this class to print name, age, salary and designation of the Employee
# has context menu

class employee(person):
    employee_type=" salayr and designation"
    def __init__(self,salary, designation):
        self.salary=salary
        self.designation=designation

    def get_details(self):
        return (f" Person name is slary is {self.salary} and designation is {self.designation}.")
v1=employee('none', 'student')
print(v1.get_details())
