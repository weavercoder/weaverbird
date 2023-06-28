name = input("What's your name: ").strip().title()
print(f"Hello, {name}!")

marital_status = input("Are you married? (yes/no): ")

if marital_status.lower() == "yes":
    spouse_p_no = input("Enter your spouse's phone number: ")
    print(f"Spouse's phone number: {spouse_p_no}")
else:
    own_p_no = input("Enter your own phone number: ")
    print(f"Your phone number: {own_p_no}")

