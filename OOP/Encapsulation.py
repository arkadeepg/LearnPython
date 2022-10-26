# Program to understand Encapsulation

class car:                                              # Class Definition
    model = None                                        # Public Attribute
    shade = None
    __door = 5                                          # Private Attribute

    def display(self):                                  # Public Method
        print("Model of the car is: ", self.model)
        print("Doors in the car is: ", self.__door)
        self.__show()                                   # Function calling another function in same Class

    def __show(self):                                   # Private Method
        __colour = self.shade
        print("Colour of car is: ", __colour)

    def power(self, pwr):
        __power = pwr
        print("Power of the car is: ", __power, "bhp")


d1 = car()                                              # Object Initialisation


# Function1 definition
def car_op():                                           # Function to access Class members using a Class Object (Called Function)
    d1.model = "Tesla"
    d1.shade = "Brown"
    d1.display()
    d1.power(2000)


# Function2 definition
def car_call():
    car_op()                                            # Function calling another function in the program, Function must be defined beforehand (Calling Function)

# Function Calling
car_call()                                              # Calling first function