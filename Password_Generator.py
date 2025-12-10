import random
import string
import os

letters = string.ascii_letters          # a-zA-Z
numbers = string.digits                 # 0-9
symbols = string.punctuation            # !@#$%^&*...
passwords = []
length = 0

# Load passwords from file if it exists
filepath = "passwords.txt"
if os.path.exists(filepath):
    with open(filepath, "r") as file:
        for line in file:
            passwords.append(line.strip())

print("\nPassword Generator")
platform = input("This password is labeled for: ")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    length = input("Enter a number: ")

    if length.isdigit():
        length = int(length)
        if length <= 0:
            input("Length must be greater than 0.")
            continue
        else:
            break
    else:
        input("❌ Invalid input press enter to try again.")
        continue

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Enter a length of the password (Number): {length}")
    question1 = input("Include numbers? (y/n): ")
    if question1.lower() == "y" or question1.lower() == "n":
        while True:
            question2 = input("Include symbols? (y/n): ")
            if question2.lower() == "y" or question2.lower() == "n":
                break
            input("❌ Invalid input press enter to try again.")
        break
    else:
        input("❌ Invalid input press enter to try again.")

if question1 == "y" and question2 == "y":
    password = ''.join(random.choice(letters + numbers + symbols) for _ in range(length))
elif question1 == "n" and question2 == "y":
    password = ''.join(random.choice(letters + symbols) for _ in range(length))
elif question1 == "y" and question2 == "n":
    password = ''.join(random.choice(letters + numbers) for _ in range(length))
elif question1 == "n" and question2 == "n":
    password = ''.join(random.choice(letters) for _ in range(length))

print("\nGenerated password: ")
print(password)

strength = ""

if question1.lower() == "y" and question2.lower() == "y" and length >= 12:
    strength = "STRONG ✅"
elif question1.lower() == "y" and question2.lower() == "n" and length >= 8:
    strength = "MEDIUM ✅"
else:
    strength = "WEAK ✅"

print(f"Strength: {strength}")

passwords.append(f"{platform}: {password}")

with open("passwords.txt", "w") as file:
    for item in passwords:
        file.write(item + "\n")

print("Saved to passwords.txt ✅")
