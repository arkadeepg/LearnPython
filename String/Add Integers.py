# Program to add integers in a String

str1 = input("Enter your string: ")


def str_sum(strng):
    sum = 0
    for i in range(len(strng)):
        if strng[i].isdigit():
            sum += int(strng[i])
    return sum


print("Value is: ", str_sum(str1))
