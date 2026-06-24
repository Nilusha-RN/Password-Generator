import random
import string

print("=== Password Generator ===")

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(12):
    password += random.choice(characters)

print("Generated Password:", password)