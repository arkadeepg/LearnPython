# functions (methods can be performed in a list)

# numbers = [5, 5, 2, 3, 1, 7, 9]
# print("Original List: ", numbers)
#
# numbers.append(13)
# print("Append operation: ", numbers)
#
# numbers.insert(0, 99)
# print("Insert operation(0, 99): ", numbers)
#
# numbers2 = numbers.copy()
# print("Copied to another list: ", numbers2)
#
# numbers.remove(13)
# print("Remove item: ", numbers)
#
# numbers.pop()
# print("Pop item: ", numbers)
#
# # print(numbers.index(13))
# print("Check for an item(13): ", 13 in numbers)
#
# print("Number of item(5): ", numbers.count(5))
#
# numbers.sort()
# print("Sort list: ", numbers)
#
# numbers.reverse()
# print("Reverse list: ", numbers)
#
# numbers.clear()
# print("Clear list: ", numbers)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("remove duplicates from a list")

list1 = [2, 2, 3, 3, 5, 9]
list2 = []

for num in list1:
    if num in list2:
        continue
    else:
        list2.append(num)

print(list1)
print(list2)
