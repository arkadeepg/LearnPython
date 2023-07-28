# Comparison Operators
# ==    equals
# !=    not equals
# >     greater than
# <     lesser than
# >=    greater than or equal
# <=    less than or equal

name = input("Enter your name: ")
char = len(name)

if char < 3:
    print("Name must be at least 3 characters.")
elif char > 10:
    print("Name can be maximum of 10 characters.")
else:
    print("Name looks good.")
