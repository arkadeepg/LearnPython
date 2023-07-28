# Tuple is an immutable data type
# can't be modified or cleared

numbers = [1, 2, 3, 4]  # list

number = (1, 2, 3, 4)  # tuple

numbers[0] = 10
print(numbers)

# number[0] = 10        # not possible
print(number)

# Unpacking

coordinates = (1, 2, 3)
x, y, z = coordinates       # this will assign each item to the respective variable
        # OR
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
