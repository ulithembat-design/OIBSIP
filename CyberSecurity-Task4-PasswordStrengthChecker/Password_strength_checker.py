#!/usr/bin/env python3
"""
Password Strength Checker
Task 4 - OIBSIP Cyber Security Internship

Evaluates password strength based on length, character variety,
and common weak patterns, then gives specific feedback.
"""

import re
import getpass

COMMON_WEAK_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "letmein", "admin", "welcome", "monkey", "password1"
]


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long (12+ is better).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g. !@#$%).")

    if password.lower() in COMMON_WEAK_PASSWORDS:
        score = 0
        feedback = ["This is a commonly used password and is easily guessed. Choose something unique."]

    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating the same character multiple times in a row.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, feedback


def print_result(password):
    strength, score, feedback = check_password_strength(password)

    print("\n" + "=" * 50)
    print(f"Password Strength: {strength}  (Score: {score}/6)")
    print("=" * 50)

    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("Great job! This password meets all strength criteria.")
    print("=" * 50 + "\n")


def main():
    print("=" * 50)
    print("   PASSWORD STRENGTH CHECKER")
    print("   Task 4 - OIBSIP Cyber Security Internship")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    while True:
        password = getpass.getpass("Enter a password to check (hidden input): ")
        if password.lower() == "exit":
            print("Goodbye!")
            break
        if not password:
            print("Please enter a password.\n")
            continue
        print_result(password)


if __name__ == "__main__":
    main()