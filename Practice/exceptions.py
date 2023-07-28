# Program to understand Exception Handling


try:
    age = int(input("Enter your Age: "))
    income = int(input("Enter net salary: "))
    print(age)
    print(income/age)
except ZeroDivisionError:
    print("Age can't be zero.")
except ValueError:
    print("Invalid age entered.")
