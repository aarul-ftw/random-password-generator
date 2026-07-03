import random
import string

print("------------ PASSWORD GENERATOR ------------")

while True:
    length = int(input("Enter the desired length of the password (between 8 and 16 characters): "))

    if length < 8:
        print("❌ Password length should be at least 8 characters.\n")

    elif length > 16:
        print("❌ Password length should not exceed 16 characters.\n")

    else:
        break

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\n✅ Generated Password:", password)