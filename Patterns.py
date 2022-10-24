# Program to print patterns

n = 4

# right triangle
for i in range(n):
    for j in range(i + 1):
        print("*", end="")  # by default print function ends with new line, 'end' function to avoid that
    print("\r")  # end the line, \n is for new line

print()

# right downward triangle
for i in range(n):  # row
    for j in range(i, n):  # column
        # print(i,j)
        print("*", end="")
    print("\r")

print()

# left triangle
for i in range(n):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print("\r")

print()

# left downward triangle
for i in range(n):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(i, n):
        print("*", end="")
    print("\r")

print()

# pyramid
for i in range(n):
    for j in range(i, n):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i + 1):
        print("*", end="")
    print("\r")

print()

# reverse pyramid
for i in range(n):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(i, n - 1):
        print("*", end="")
    for j in range(i, n):
        print("*", end="")
    print("\r")

print()