# Return the count of a given substring from a string:

str_x = "Emma is good developer. Emma is a writer"
sub_str = "Emma"

def substring(str1, str2):
    count = 0
    strng = str1.split(" ")
    for i in strng:
        if i == str2:
            count += 1
    print(count)

substring(str_x, sub_str)

###################################################################################
# Remove first n characters from a string:

def remove_chars(str1, n):
    str1 = str1[n:]
    print(str1)

remove_chars("pynative", 2)

###################################################################################
# Print the following pattern:
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for i in range(1,6):
    for j in range(i):
        print(i, end = "")
    print()

###################################################################################
# write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


def list_op(l1, l2):
    lst = []
    
    for i in l1:
        if i % 2 != 0:
            lst.append(i)
            
    for i in l2:
        if i % 2 == 0:
            lst.append(i)
            
    print(lst)

list_op(list1, list2)

###################################################################################
# Write a Program to extract each digit from an integer in the reverse order, with a space separating the digits.

num = int(input("Provide your number: "))

def reverse(num):
    # str1 = str(num)
    # str2 = ""
    # for i in str1[::-1]:
    #     str2 += f"{i} "
    # print(str2)
    
    while num > 0:
        ele = num % 10
        print(ele, end=" ")
        num = num // 10

reverse(num)
