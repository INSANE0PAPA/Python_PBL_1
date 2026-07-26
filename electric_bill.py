print("======================================")
print("     ELECTRICITY BILL CALCULATOR")
print("======================================")

while True:

    name = input("\nEnter Consumer Name : ")
    cid = input("Enter Consumer ID : ")

    units = float(input("Enter Units Consumed : "))

    # Calculate Energy Charge
    if units <= 100:
        bill = units * 1.5

    elif units <= 200:
        bill = units * 2.5

    elif units <= 300:
        bill = units * 4.0

    else:
        bill = units * 5.5

    fixed_charge = 100

    total_bill = bill + fixed_charge

    surcharge = 0

    if total_bill > 1000:
        surcharge = total_bill * 0.10
        total_bill = total_bill + surcharge

    print("\n========== ELECTRICITY BILL ==========")
    print("Consumer Name :", name)
    print("Consumer ID   :", cid)
    print("Units Used    :", units)
    print("Energy Charge : ₹", round(bill, 2))
    print("Fixed Charge  : ₹", fixed_charge)
    print("Surcharge     : ₹", round(surcharge, 2))
    print("--------------------------------------")
    print("Total Bill    : ₹", round(total_bill, 2))
    print("======================================")

    choice = input("\nCalculate another bill? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\nThank You!")
