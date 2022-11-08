# Program to check if a string is Palindrome

str1 = input("Enter your string: ")


def str_palindrome(strng):
    str2 = strng[::-1]
    if strng == str2:
        print("Palindrome.")
    else:
        print("Not a Palindrome.")


str_palindrome(str1)
