def check_discount_eligibility():
    is_member_input = input("Are you a store member? (yes/no): ").strip().lower()
    is_member = is_member_input == "yes"

    amount_spent = float(input("Enter the amount spent: "))

    if is_member or amount_spent > 100:
        print("Eligible for discount.")
        if is_member and amount_spent > 100:
            print("Eligible for additional discount.")
    else:
        print("Not eligible for discount.")

def check_admission_eligibility():
    math = int(input("Enter Math score: "))
    science = int(input("Enter Science score: "))
    english = int(input("Enter English score: "))

    if (math > 70 and science > 70) or (math > 90 or science > 90):
        print("Qualified for admission (based on Math and Science scores).")
    elif english > 70 and (math > 70 or science > 70):
        print("Qualified for admission (based on English and either Math or Science).")
    else:
        print("Not qualified for admission.")

check_discount_eligibility()
print()
check_admission_eligibility()