import random
import string
from datetime import datetime


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


def save_password(password, strength):
    with open("password_history.txt", "a") as file:
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date_time} | {password} | Strength: {strength}\n")


def view_history():
    try:
        with open("password_history.txt", "r") as file:
            history = file.read()

            if history == "":
                print("No password history found.")
            else:
                print("\n=== Password History ===")
                print(history)

    except FileNotFoundError:
        print("No password history found.")


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

        for i in range(length - len(password_list)):
            password_list.append(random.choice(characters))

        random.shuffle(password_list)
        password = "".join(password_list)
        strength = check_strength(password)

        print("\nGenerated Password:", password)
        print("Password Strength:", strength)

        save_password(password, strength)
        print("Password saved to password_history.txt")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n=== Password Generator ===")
    print("1. Generate Password")
    print("2. View Password History")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_password()
    elif choice == "2":
        view_history()
    elif choice == "3":
        print("Thank you for using Password Generator.")
        break
    else:
        print("Invalid choice. Please try again.")