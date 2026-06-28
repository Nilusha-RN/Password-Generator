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

        if use_uppercase == "yes":
            characters += string.ascii_uppercase

        if use_lowercase == "yes":
            characters += string.ascii_lowercase

        if use_numbers == "yes":
            characters += string.digits

        if use_symbols == "yes":
            characters += string.punctuation

        if characters == "":
            print("You must select at least one character type.")

        else:
            password = ""

            for i in range(length):
                password += random.choice(characters)

            print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")