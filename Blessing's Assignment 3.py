
'''
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).
===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.
'''


#Input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

#Processing
BMI = weight / (height ** 2)

#Output
print("Your calculated BMI is: ", BMI)
