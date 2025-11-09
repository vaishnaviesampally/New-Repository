# BMI Calculator in Python

def calculate_bmi(weight, height):
    """Calculate BMI using the formula: weight (kg) / height^2 (m^2)"""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Return BMI category based on the calculated BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("==== BMI Calculator ====")
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("⚠️ Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
