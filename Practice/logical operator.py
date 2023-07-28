# and, or, not are Logical operators

has_good_credit = True
has_high_income = True

if has_good_credit or has_high_income:
    print("Eligible for loan")

has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible")
