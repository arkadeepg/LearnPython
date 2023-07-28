is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day, drink plenty of water")
elif is_cold:
    print("It's a cold day, wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day!")


good_credit = False
price = 1000000
ten_p = int(price * 0.10)
twnty_P = int(price * .20)

if good_credit:
    print("Buyer needs to pay 10% down: ", ten_p)
else:
    print("Buyer needs to pay 20% down: ", twnty_P)
