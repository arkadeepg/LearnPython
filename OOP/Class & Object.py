# New object to work with OOP

# # Class Definition, with initial value
# class student:
#     # pass  # 'pass' keyword to avoid error of blank class/ function
#
#     std = 6                                         # Class Variable
#
#     def __init__(self, fname, lname, empid):        # default Constructor to initialise data members
#         self.fname = fname
#         self.lname = lname
#         self.empid = empid
#
#     def write(self):
#         std = 9                                     # Instance Variable
#         print("Instance Variable", std)
#         print("Class Variable", self.std)
#
#
# # Object initialisation
# Ram = student("Ram", "Sharma", 911)
# Mohan = student("Mohan", "Mishra", 121)
#
# # Accessing Class Members using Objects
# print(Ram.empid)
# Ram.write()


# Class without initial value
class dog:
    age = None
    breed = "pug"

    def write1(self):
        print(self.breed)

    def write2(self):
        print(self.breed)


# Object initialisation
Tommy = dog()

# Accessing Class Members using Objects
# Attribute with blank(None) value
print(Tommy.age)

Tommy.age = 19

print(Tommy.age, "\n")

# Attribute with some initial value
print(Tommy.breed)
print("Location", id(Tommy.breed))

Tommy.breed = "gsd"

print(Tommy.breed)
print("Location", id(Tommy.breed))