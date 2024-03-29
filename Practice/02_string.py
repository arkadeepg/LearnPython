# Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI 50 Expert"

str2 = str1.split(" ")
list1 = []

for i in str2:
    if any(j.isalpha() for j in i) and any(j.isdigit() for j in i):
        list1.append(i)
                
print(list1)                

###########################################################################
# Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician 2"
str2 = ""

for i in str1:
    if i.isalpha():
        str2 += str2.join(i)
    elif i.isdigit():
        str2 += str2.join(i)
    elif i == " ":
        str2 += str2.join(i)
        
print(str2)        

##########################################################################

# Find the last position of a given substring

str1 = "Emma is a data scientist who knows Python. Emma works at google."

index = str1.rfind("Emma") 

print(index)

#########################################################################
# Write a program to count occurrences of all characters within a string

str1 = "Apple"

str2 = {}

for i in str1:
    count = str1.count(i)
    str2[i] = count
    
print(str2)   

#########################################################################
# Append new string in the middle of a given string

s1 = "Ault"
s2 = "Kelly"

n = len(s1)
i = n // 2

temp = s1[i:n+1]

s1 = s1[0:i]

print(s1 + s2 + temp) 

########################################################################
# Replace each special symbol with # in the following string

str1 = "/*Jon is @developer & musician 2"
str2 = ""

for i in str1:
    if i.isalnum():
        str2 += str2.join(i)
    elif i == " ":
        str2 += str2.join(i)
    else:
        str2 += str2.join('#')
        
print(str2) 

#########################################################################
# Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

temp_str = str1.lower()

count = temp_str.count(sub_string.lower())

print("The USA count is:", count)


