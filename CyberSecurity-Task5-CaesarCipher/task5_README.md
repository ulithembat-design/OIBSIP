# Task 5 – Caesar Cipher Encryption/Decryption Tool

## Objective
Build a Python tool that demonstrates the classic Caesar cipher — one of
the earliest known encryption techniques — including encryption,
decryption, and a brute-force attack demonstration.

## Environment
- **OS:** Kali Linux 2026.2 (VirtualBox)
- **Language:** Python 3

## What is a Caesar Cipher?
A Caesar cipher is a substitution cipher where each letter in the
plaintext is shifted a fixed number of positions down the alphabet. For
example, with a shift of 3, `A` becomes `D`, `B` becomes `E`, and so on.
It's named after Julius Caesar, who reportedly used it to protect
military messages.

While historically significant, the Caesar cipher is cryptographically
weak by modern standards — it only has 25 possible keys (shifts), making
it trivial to break with a brute-force attack.

## How the Script Works
The script (`caesar_cipher.py`) offers three functions:

1. **Encrypt** – Takes a message and a shift value, and encrypts it by
   shifting each letter forward in the alphabet. Non-letter characters
   (spaces, numbers, punctuation) are left unchanged.
2. **Decrypt** – Takes an encrypted message and the known shift value,
   and reverses the process to recover the original message.
3. **Brute-force decrypt** – Takes an encrypted message with an *unknown*
   shift and tries all 25 possible shifts, printing every possible
   decryption so the correct one can be spotted by eye.

## Steps to Reproduce

1. Ran the script:
   ```
   python3 caesar_cipher.py
   ```
2. Chose option 1 (Encrypt) and entered a test message with a shift of 3.
   The script returned the encrypted text.
3. Chose option 2 (Decrypt) and entered the encrypted text with the same
   shift value (3), confirming it correctly returned the original
   message.
4. Chose option 3 (Brute-force decrypt) and entered the encrypted text
   without specifying the shift. The script printed all 25 possible
   decryptions, demonstrating how quickly this cipher can be broken
   without knowing the key.

## Why This Matters
The Caesar cipher is a foundational concept in cryptography education.
Demonstrating both the encryption/decryption process *and* the
brute-force attack highlights an important security principle: a cipher
with a small keyspace (here, only 25 possible shifts) offers effectively
no real protection against a determined attacker, even without advanced
tools. This is the same underlying idea behind why modern encryption
standards rely on enormous keyspaces to remain secure.

## Possible Improvements
- Add support for the Vigenère cipher (a polyalphabetic extension of the
  Caesar cipher) for comparison.
- Add automatic detection of the correct decryption using English
  letter-frequency analysis, rather than requiring the user to visually
  scan all 25 outputs.
- Build a simple GUI or web interface.

## Evidence
- `caesar_cipher.py` – the script
- `demo-video.mp4` – walkthrough showing encryption, decryption, and
  brute-force attack
- Screenshot(s) of terminal output

## Disclaimer
This exercise was performed strictly in a local, isolated environment for
educational purposes as part of the Oasis Infobyte Cyber Security
Internship.
