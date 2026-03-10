import re

while True:
    password = input("\nEnter your password: ")
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        print("❗ Password should be at least 8 characters")

    if re.search("[a-z]", password):
        score += 1
    else:
        print("❗ Add lowercase letters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        print("❗ Add uppercase letters")

    if re.search("[0-9]", password):
        score += 1
    else:
        print("❗ Add numbers")

    if re.search("[@#$%^&*!]", password):
        score += 1
    else:
        print("❗ Add special characters")

    print("\nPassword Score:", score, "/5")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")

    again = input("\nCheck another password? (yes/no): ")

    if again.lower() != "yes":
        print("Program finished")
        break