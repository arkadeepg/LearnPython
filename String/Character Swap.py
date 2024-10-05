# Program to swap commas and dots

str1 = "Test.123,456"
print(str1)

str1 = str1.replace(',', "third")
print(str1)

str1 = str1.replace('.', ',')
print(str1)

str1 = str1.replace("third", '.')
print(str1)

# String traversal

for i in str1:
    print(i, end='')
