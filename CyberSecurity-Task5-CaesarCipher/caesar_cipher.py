#!/usr/bin/env python3
"""
Caesar Cipher Encryption/Decryption Tool
Task 5 - OIBSIP Cyber Security Internship

Encrypts and decrypts text using the classic Caesar cipher technique,
where each letter is shifted by a fixed number of positions in the
alphabet.
"""


def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char  # leave numbers, spaces, punctuation unchanged
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def brute_force_decrypt(text):
    print("\n" + "=" * 50)
    print("BRUTE FORCE: trying all 25 possible shifts")
    print("=" * 50)
    for shift in range(1, 26):
        print(f"Shift {shift:2d}: {caesar_decrypt(text, shift)}")
    print("=" * 50 + "\n")


def main():
    print("=" * 50)
    print("   CAESAR CIPHER TOOL")
    print("   Task 5 - OIBSIP Cyber Security Internship")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message (known shift)")
        print("  3. Brute-force decrypt (unknown shift)")
        print("  4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            encrypted = caesar_encrypt(text, shift)
            print(f"\nEncrypted message: {encrypted}")

        elif choice == "2":
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter shift value used to encrypt (1-25): "))
            decrypted = caesar_decrypt(text, shift)
            print(f"\nDecrypted message: {decrypted}")

        elif choice == "3":
            text = input("Enter the encrypted message: ")
            brute_force_decrypt(text)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please choose 1-4.")


if __name__ == "__main__":
    main()