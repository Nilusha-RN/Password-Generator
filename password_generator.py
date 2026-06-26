import random
import string

print("=== Password Generator ===")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length must be at least 4.")

    else:
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower()

        characters = string.ascii_lowercase + string.digits + string.punctuation

        if use_uppercase == "yes":
            characters += string.ascii_uppercase

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")