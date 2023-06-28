class test():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def display(self):
        print(self.val1, self.val2)


obj1 = test(9, 9)

obj1.display()


def sum(*number):
    val = 0
    for num in number:
        val += num
    print(number)


sum(3, 2, 7)
