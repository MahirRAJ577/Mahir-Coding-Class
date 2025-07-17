days = float(input("Input how many working days your student has : "))
absdays = float(input("Input how many absent days your student has : "))

E = (100.0 - (absdays/days)*(100/1))

print("The eligibility is:", E)

if E <= 74:
    print("This student can not enter the examination.")
else:
    print("This student is eligible for the examination.")