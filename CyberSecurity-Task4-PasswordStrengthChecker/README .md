# Task 4 – Password Strength Checker

## Objective
Build a Python script that evaluates password strength and gives specific,
actionable feedback to help users create stronger passwords.

## Environment
- **OS:** Kali Linux 2026.2 (VirtualBox)
- **Language:** Python 3

## How It Works
The script (`password_strength_checker.py`) prompts the user for a
password (input is hidden, similar to a real login prompt) and scores it
out of 6 based on the following criteria:

| Check | Points |
|---|---|
| Length ≥ 12 characters | +2 |
| Length ≥ 8 characters (but < 12) | +1 |
| Contains an uppercase letter | +1 |
| Contains a lowercase letter | +1 |
| Contains a digit | +1 |
| Contains a special character | +1 |

**Additional rules:**
- If the password matches a list of commonly used weak passwords
  (e.g., `password`, `123456`, `qwerty`), the score is forced to 0
  regardless of other criteria, since these are trivially guessable.
- If the password contains 3 or more repeated characters in a row
  (e.g., `aaaa`, `1111`), the script flags it as a weak pattern.

**Final strength rating:**
- **Score 0–2:** WEAK
- **Score 3–4:** MEDIUM
- **Score 5–6:** STRONG

The script also prints specific, actionable suggestions (e.g., "Add at
least one special character") rather than just a pass/fail result, so the
feedback is genuinely useful.

## Steps to Reproduce

1. Ran the script:
   ```
   python3 password_strength_checker.py
   ```
2. Tested a weak password (a short password with no variety):
   - **Result:** WEAK (Score: 1/6), with suggestions to add length,
     uppercase, lowercase, and special characters.
3. Tested a medium-strength password (mixed case + digit, no special
   character):
   - **Result:** MEDIUM (Score: 4/6), with a suggestion to add a special
     character.
4. Tested a strong password (long, mixed case, digit, and special
   character):
   - **Result:** STRONG (Score: 6/6), confirming it meets all criteria.

## Why This Matters
Weak passwords remain one of the most common entry points for account
compromise. A simple strength checker like this demonstrates the basic
principles behind password policies used in real systems: length,
character variety, and avoidance of common/guessable patterns all
meaningfully increase resistance to brute-force and dictionary attacks.

## Possible Improvements
- Check against a larger breached-password database (e.g., via the
  Have I Been Pwned API) instead of a small hardcoded list.
- Estimate crack time based on entropy rather than a simple point score.
- Add a GUI or web front-end for non-technical users.

## Evidence
- `password_strength_checker.py` – the script
- `demo-video.mp4` – walkthrough showing weak, medium, and strong
  password results
- Screenshot(s) of terminal output

## Disclaimer
This exercise was performed strictly in a local, isolated environment for
educational purposes as part of the Oasis Infobyte Cyber Security
Internship. No real credentials or third-party systems were involved.
