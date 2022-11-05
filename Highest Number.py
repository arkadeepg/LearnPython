# Highest Number among three

first = int(input("Enter First number : "))
second = int(input("Enter Second Number : "))
third = int(input("Enter Third Number : "))

# if (first > second) & (first > third):
#     highest = first
# elif (second > first) & (second > third):
#     highest = second
# else:
#     highest = third

# highest = 00
# int(highest)
highest = first
if second > highest:
    if second > third:
        highest = second
    else:
        highest = third
elif third > highest:
    # if third > second:
    highest = third

print("Highest number is ", highest, '.')