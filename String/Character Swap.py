# Program to swap commas and dots

str1 = "Test.123,456"
print(str1)

str1 = str1.replace(',', "third")
print(str1)

str1 = str1.replace('.', ',')
print(str1)

str1 = str1.replace("third", '.')
print(str1)

n = len(str1)
for i in range(n):
    print(i)