num = int(input("Enter your number: "))


def armstrng(num):
    value = num
    digits = len(str(num))
    res = 0
    for i in range(digits):
        temp = value % 10
        res += temp ** digits
        value = value // 10

    if num == res:
        print(True)
    else:
        print(False)


armstrng(num)
