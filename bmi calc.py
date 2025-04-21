print("This is a BMI Calculator")

# Get user input for name, height, and weight
name = input("Please enter your name: ")
height = float(input("Please enter your height in meters: "))
weight = int(input("Please enter your weight in kilograms: "))

# Initialize information dictionary
information = {'name': 'N/A', 'BMI': 'N/A', 'status': 'N/A'}

# Calculate BMI
bmi = weight / (height * height)

# Categorize BMI status
if bmi > 30:
    information['status'] = "Obese"
elif 25 < bmi <= 30:
    information['status'] = "Overweight"
elif 18.5 < bmi <= 25:
    information['status'] = "Normal Weight"
else:
    information['status'] = "Underweight"

# Assign the name and BMI to the dictionary
information['name'] = name
information['BMI'] = round(bmi, 2)

# Print the BMI report
print("------BMI REPORT------")
print(f"Name: {information['name']}")
print(f"BMI: {information['BMI']}")
print(f"Status: {information['status']}")
