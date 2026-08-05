# BMI Calculator

**Oasis Infobyte SIP | Python Programming Track | Task 2 (Beginner Tier)**

## Objective
A command-line Python program that calculates a user's Body Mass Index (BMI)
from their weight and height, and classifies the result into a standard
health category.

## Tech Stack
- Python 3
- `input()` for user input
- Basic arithmetic (no external libraries required)

## How It Works
1. The program prompts the user to enter their **weight (kg)** and
   **height (m)**.
2. BMI is calculated using the standard formula:

   ```
   BMI = weight (kg) / height (m)**2
   ```

3. The result is rounded to 2 decimal places and classified into one of
   four categories:

   | BMI Range      | Category       |
   |----------------|----------------|
   | < 18.5         | Underweight    |
   | 18.5 - 24.9    | Normal weight  |
   | 25.0 - 29.9    | Overweight     |
   | >= 30.0        | Obese          |

## Input Validation
- Non-numeric input (e.g. letters or symbols) is rejected with a clear
  error message, and the user is re-prompted.
- Negative or zero values are rejected with a clear error message, and
  the user is re-prompted.

## How to Run
```bash
python bmi_calculator.py
```
Then follow the on-screen prompts to enter weight and height.

## Example Output
```
========================================
           BMI CALCULATOR
========================================

Enter your weight in kg: 70
Enter your height in m (e.g. 1.75): 1.75

----------------------------------------
Your BMI is: 22.86
Category:    Normal weight
----------------------------------------
```

## Folder Contents
- `bmi_calculator.py` - main program script
- `README.md` - this file
- Screenshots of the program running (added separately)

## Author
Ulithemba Tsala
