# Program to understand Inheritance

# Single Inheritance
class base:
    def display(self):
        print("Parent")


class derived(base):
    def show(self):
        print("Child")


obj1 = derived()

obj1.display()


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

obj2.gdisplay()
obj2.pdisplay()
obj2.cdisplay()