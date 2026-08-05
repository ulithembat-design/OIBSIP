"""
BMI Calculator
Oasis Infobyte SIP - Python Programming Track - Task 2
Beginner Tier

Calculates a user's Body Mass Index (BMI) from weight and height,
and classifies the result into a standard health category.
"""


def get_positive_float(prompt):
    """
    Ask the user for a number until they give a valid, positive value.
    Handles two error cases:
      1. Non-numeric input (e.g. letters, symbols)
      2. Negative or zero values (weight/height can't be <= 0)
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
        except ValueError:
            print("  Error: Please enter a valid number (e.g. 65 or 65.5).\n")
            continue

        if value <= 0:
            print("  Error: Value must be greater than 0. Please try again.\n")
            continue

        return value


def calculate_bmi(weight_kg, height_m):
    """BMI = weight (kg) / height (m) squared."""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    """Return the standard WHO-style BMI category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 40)
    print("           BMI CALCULATOR")
    print("=" * 40)
    print()

    weight = get_positive_float("Enter your weight in kg: ")
    height = get_positive_float("Enter your height in m (e.g. 1.75): ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print()
    print("-" * 40)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category:    {category}")
    print("-" * 40)


if __name__ == "__main__":
    main()