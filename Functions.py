# Program to understand Functions and Parameters in Python

print("Required Argument")


def func_required(a, b):
    print("A is:  ", a)
    print("B is:  ", b)
    print("Sum is:", a + b)
    print()


func_required(2, 3)

print("Keyword Argument")


def func_keyword(a, b):
    print("A is:  ", a)
    print("B is:  ", b)
    print("Sum is:", a + b)
    print()


func_keyword(b=3, a=2)

print("Default Argument")


def func_default(a, b=3):
    print("A is:  ", a)
    print("B is:  ", b)
    print("Sum is:", a + b)
    print()


func_default(a=2)

print("Variable Length Argument")


def func_var(*vars):
    sum = 0
    var1 = 65
    for var in vars:
        sum += var
        print(chr(var1), "is:  ", var)
        var1 += 1
    print("Sum is:", sum)


func_var(2, 3, 5)