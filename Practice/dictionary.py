# key: value pair
# data is stored with respect to a key
# mutable

# customer = {
#     "Name": "Ram Kumar",
#     "Age": 30,
#     "Dept": "CS"
# }
#
# print(customer["Name"])
#
# print(customer.get("dob"))


num = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phone = input("Enter your phone number: ")

for digit in phone:
    print(num.get(digit, digit.upper()), end=" ")
    # print(num[digit], end=" ")
