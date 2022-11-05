# Program to reverse a String

str1 = input("Enter your string: ")


def str_reverse(strng):
    str2 = ""
    n = len(strng)
    for i in range(n-1, -1, -1):
        str2 = str2 + strng[i]
    return str2


print("New string is: ", str_reverse(str1))
