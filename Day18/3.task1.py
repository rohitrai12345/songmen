# Take two numbers as input and add those numbers. Handle the possible exceptions.
 
try:
    data = int(input ("enter a first number"))
    data = int(input("enter a second number"))
    result = num1+num2
    print(result)
except:
    print("error is raised")


# Take two numbers input and divide a number by another number. Handle the possible exceptions.


try:
    data = int(input ("enter a first number"))
    data = int(input("enter a second number"))
    result = num1/num2
    print(result)
except:
    print("error is raised")


# Create a dictionary student with keys id, name, age, department. Take a input from the user, which info (id, name, age or department) he wants to access and print the result. Handle the possible exceptions.


student = {"id": 1, "name": "Ram", "age": 30, "department": "CS"}
key = input("Enter the info you want to access ")
try:
    result = student[key]
except KeyError:
    print(f"The {key} is not present in the student")
else:
    print(f"The {key} of the student is {result}")


if key in student:
    print(f"The {key} of the student is {student[key]}")
else:
    print(f"The {key} is not present in the student")
    

result = student.get(key, "N/A")
print(f"The {key} of the student is {student[key]}")



