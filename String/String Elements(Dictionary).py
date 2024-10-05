# Program to find count of characters in a String

str1 = "Enter the string: "  # take input as String


def char_count(strng):
    element = {}
    key = element.keys()
    for i in strng:
        if i in key:
            element[i] += 1
        else:
            element[i] = 1
    return element


def display(elmnt):
    for i in elmnt:
        print(i, elmnt.get(i), end=",")


print(str1)
element1 = char_count(str1)
display(element1)
