import random
import string

print("=== Password Generator ===")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length must be at least 4.")

    else:
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

        elif length < len(password_list):
            print("Password length is too short for selected options.")

        else:
            remaining_length = length - len(password_list)

            for i in range(remaining_length):
                password_list.append(random.choice(characters))

            random.shuffle(password_list)

            password = "".join(password_list)

            print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")