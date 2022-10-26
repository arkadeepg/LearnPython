# Program to understand Inheritance

# Single Inheritance
class base:
    def display(self):
        print("Parent")


class derived(base):
    def show(self):
        print("Child")


obj1 = derived()

print("Single Inheritance")
obj1.display()
obj1.show()
print()


# Multi-level Inheritance

class grandparent:
    def gdisplay(self):
        print("Grandparent Class")

class parent(grandparent):
    def pdisplay(self):
        print("Parent Class")

class child(parent):
    def cdisplay(self):
        print("Child Class")

obj2 = child()

print("Multi-level Inheritance")
obj2.gdisplay()
obj2.pdisplay()
obj2.cdisplay()
print()


# Hierarchical Inheritance

class parent():
    def pdisplay(self):
        print("PARENT")

class child1(parent):
    def c1display(self):
        print("Child1")

class child2(parent):
    def c2display(self):
        print("Child2")


c1 = child1()
c2 = child2()

print("Hierarchical Inheritance")
c1.pdisplay()
c1.c1display()
c2.pdisplay()
c2.c2display()
print()


# Multiple Inheritance

class father():
    def fdisplay(self):
        print("Father")

class mother():
    def mdisplay(self):
        print("Mother")

class child(father, mother):
    def cdisplay(self):
        print("Child")


obj = child()

print("Multiple Inheritance")
obj.fdisplay()
obj.mdisplay()
obj.cdisplay()
print()