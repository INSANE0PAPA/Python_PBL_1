print("===================================")
print(" STUDENT GRADE MANAGEMENT SYSTEM ")
print("===================================")

while True:

    name = input("Enter Student Name : ")
    roll = input("Enter Roll Number : ")

    print("\nEnter Marks (Out of 100)")

    m1 = float(input("Python : "))
    m2 = float(input("Math : "))
    m3 = float(input("Physics : "))
    m4 = float(input("English : "))
    m5 = float(input("Computer : "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"

    elif percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 50:
        grade = "D"

    else:
        grade = "F"

    print("\n========== RESULT ==========")
    print("Student Name :", name)
    print("Roll Number  :", roll)
    print("Total Marks  :", total)
    print("Percentage   :", round(percentage,2),"%")
    print("Grade        :", grade)

    if grade == "F":
        print("Result       : FAIL")
    else:
        print("Result       : PASS")

    choice = input("\nDo you want to add another student? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\nThank You")
