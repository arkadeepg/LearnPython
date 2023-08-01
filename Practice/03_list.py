# Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly", "Yes"]

list3 = []

length = len(list1) if len(list1) > len(list2) else len(list2)

for i, j in zip(list1, list2):
    list3.append(i+j)
    
print(list3) 

####################################################################################
# Replace list’s item with new value if found

list1 = [5, 10, 15, 20, 25, 50, 20]

pos = list1.index(20)

list1[pos] = 200

print(list1)

####################################################################################
# Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)

print(list1)

####################################################################################
# Display all duplicate items from a list

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

list1 = []

for i in sample_list:
    if i not in list1:
        list1.append(i)
    else:
        print(i)

