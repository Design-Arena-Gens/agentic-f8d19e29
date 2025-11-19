#!/usr/bin/env python3
"""
Password Generator
Generates secure random passwords based on user preferences
"""

import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_digits=True, use_symbols=True):
    """
    Generate a random password with specified criteria

    Args:
        length: Length of the password (default: 12)
        use_uppercase: Include uppercase letters (default: True)
        use_lowercase: Include lowercase letters (default: True)
        use_digits: Include digits (default: True)
        use_symbols: Include special symbols (default: True)

    Returns:
        Generated password string
    """
    characters = ""

    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: At least one character type must be selected!"

    # Ensure at least one character from each selected type
    password = []
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill remaining length with random characters
    for _ in range(length - len(password)):
        password.append(random.choice(characters))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

def password_generator():
    """Main password generator function"""
    print("=" * 50)
    print("SECURE PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        print("\nPassword Configuration:")

        try:
            length = int(input("Enter password length (8-128): "))
            if length < 8 or length > 128:
                print("Password length must be between 8 and 128!")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate password
        password = generate_password(length, use_uppercase, use_lowercase,
                                    use_digits, use_symbols)

        print("\n" + "=" * 50)
        print(f"Generated Password: {password}")
        print("=" * 50)

        # Password strength analysis
        strength_score = 0
        if use_lowercase: strength_score += 1
        if use_uppercase: strength_score += 1
        if use_digits: strength_score += 1
        if use_symbols: strength_score += 1
        if length >= 12: strength_score += 1
        if length >= 16: strength_score += 1

        if strength_score >= 5:
            strength = "Very Strong 🔒"
        elif strength_score >= 4:
            strength = "Strong 🔐"
        elif strength_score >= 3:
            strength = "Moderate ⚠️"
        else:
            strength = "Weak ⚠️"

        print(f"Password Strength: {strength}")
        print(f"Length: {len(password)} characters")

        # Generate another password
        another = input("\nGenerate another password? (y/n): ")
        if another.lower() not in ['y', 'yes']:
            print("Thank you for using Password Generator!")
            break

if __name__ == "__main__":
    password_generator()
