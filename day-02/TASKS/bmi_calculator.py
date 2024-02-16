# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
# Be cautious when reading input of various data types.
print("BMI CALCULATOR FOR ALF")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Write the code ↓ to perform the calculations of user's BMI and categorize its status.
bmi = weight / (height*height)

nutritional_status = " "
if bmi < 18.5:
    nutritional_status = "UNDERWEIGHT"
elif bmi >= 18.5 and bmi <= 24.9:
    nutritional_status = "NORMAL WEIGHT"
elif bmi >= 25.0 and bmi <= 29.9:
    nutritional_status = "OVERWEIGHT"
elif bmi >= 30:
    nutritional_status = "OBESITY"

# Write the code ↓ to display the user's BMI and its classification.
# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.
print("\nHEIGHT: " + str(height) + " - WEIGHT: " + str(weight) + "\n" + "BMI: {:.2f}".format(bmi) + " - NUTRITIONAL STATUS: " + nutritional_status)

