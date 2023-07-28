class NewPoint:
    def move(self):
        print("Moved.")

    def draw(self):
        print("Draw.")


point1 = NewPoint()
point1.x = 10
point1.y = 20
print(point1.x)
point1.move()

point2 = NewPoint()
point2.y = 30
print(point2.draw())


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Constructor


class NewPoint:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def move(self):
        print("Moved.")

    def draw(self):
        print("Draw.")


point1 = NewPoint(10, 20)
print(point1.x)
