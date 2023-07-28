# While and For loops

# While

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#
# guess_count = 0
# while guess_count < 3:
#     num = int(input("Make a guess (1-9): "))
#     guess_count += 1
#     if num == 9:
#         print("You won!")
#         break
# else:                                               # Else block of while loop
#     print("Sorry! better luck next time.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# For

# for num in range(0,10):
#     print(num)

# count = 0
# for price in [1, 2, 3]:
#     count += price
# print(f"Sum of list is: {count}")


# Nested For loop

# n = 5
#
# for i in range(n):
#     for j in range(i+1):
#         print("*", end='')
#     print()
#
# for i in range(n):
#     for j in range(i, n):
#         print("*", end='')
#     print()


number = [2, 2, 2, 2, 5]

# for i in range(number.__len__()):
#     for j in range(number[i]):
#         print("*", end=" ")
#     print()

for i in number:
    for j in range(i):
        print("*", end=" ")
    print()
