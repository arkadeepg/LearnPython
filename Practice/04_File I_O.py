# Python module to understand File I/O
# File modes: 'r'- read, 'w'-write, 'a'- append, '+'- read/write
# File operations: read, write, close
##########################################################################
# Basic Read/ Write

# file = open("mytext.txt", "w")
# text = "This is a line"
# file.write(text)
# file.close()
#
# file = open("mytext.txt", "r")
# content = file.read()
# print(content)
# file.close()

###########################################################################
# Append

# file = open("mytext.txt", 'a')
#
# for i in range(5):
#     file.write(f"This is line number {i+1}.\n")
#
# file.close()

###########################################################################
# Count number of Lines, Characters and Numbers

# file = open("mytext.txt", 'r')
# content = file.read()
#
# char = num = line = 0
#
# for i in content:
#     if i.isalpha():
#         char += 1
#     elif i.isnumeric():
#         num += 1
#     elif i == "\n":
#         line += 1
#
# print(f"No. of Lines: {line}")
# print(f"No. of Characters: {char}")
# print(f"No. of Digits: {num}")
#
# file.close()

############################################################################
# copy lines of a file to multiple

file = open("mytext.txt", 'r')
lines = len(file.readlines())

new_files = int(input("How many files? : "))

new_lines = lines // new_files

file.close()
file = open("mytext.txt", 'r')

i = 0

for i in range(new_files):
    temp = open(f"file{i}", 'w')
    for j in range(new_lines):
        data = file.readline()
        temp.write(data)
    temp.close()

if lines != new_lines * new_files:
    diff = lines - new_lines * new_files
    temp = open(f"file{i}", 'a')
    for x in range(diff):
        data = file.readline()
        temp.write(data)
    temp.close()

file.close()

###########################################################################
# move odd lines

# file = open("mytext.txt", 'r')
# odd = open("oddline.txt", 'w')
# even = open("evenline.txt", 'w')
#
# read_line = file.readlines()
#
# for i in range(len(read_line)):
#     if i % 2 == 0:
#         odd.write(read_line[i])
#     else:
#         even.write(read_line[i])
#
# file.close()
# odd.close()
# even.close()

#############################################################################
# Read text file into a variable and replace all newlines with space

# with open('sample.txt', 'r') as file:
#     data = file.read().replace('\n', ' ')
#     print(data)
