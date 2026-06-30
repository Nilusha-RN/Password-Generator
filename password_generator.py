import random
import string


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def generate_password():
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            return

        use_uppercase = input("Include uppercase letters? (yes/no): ").lower()
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower()
        use_numbers = input("Include numbers? (yes/no): ").lower()
        use_symbols = input("Include symbols? (yes/no): ").lower()

        characters = ""
        password_list = []

        if use_uppercase == "yes":
            characters += string.ascii_uppercase
            password_list.append(random.choice(string.ascii_uppercase))

        if use_lowercase == "yes":
            characters += string.ascii_lowercase
            password_list.append(random.choice(string.ascii_lowercase))

        if use_numbers == "yes":
            characters += string.digits
            password_list.append(random.choice(string.digits))

        if use_symbols == "yes":
            characters += string.punctuation
            password_list.append(random.choice(string.punctuation))

        if characters == "":
            print("You must select at least one character type.")
            return

        if length < len(password_list):
            print("Password length is too short for selected options.")
            return

        remaining_length = length - len(password_list)

        for i in range(remaining_length):
            password_list.append(random.choice(characters))

        random.shuffle(password_list)

        password = "".join(password_list)

        print("\nGenerated Password:", password)
        print("Password Strength:", check_strength(password))

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n=== Password Generator ===")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_password()

    elif choice == "2":
        print("Thank you for using Password Generator.")
        break

    else:
        print("Invalid choice. Please try again.")