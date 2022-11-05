# Program to find length of a String

str1 = input("Enter the string: ")  # take input as String


def str_len(strng):  # function to calculate no. of characters
    count = 0
    for i in strng:
        count += 1
    return count


# print(str1)
print("Length of the String is: ", str_len(str1))  # print total no. of characters


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def str_count(strng):
    count_num = 0
    count_chr = 0
    for i in strng:
        if i.isalpha():
            count_chr += 1
        else:
            count_num += 1
    print("Number of Integers: ", count_num)
    print("Number of Characters: ", count_chr)


str_count(str1)
