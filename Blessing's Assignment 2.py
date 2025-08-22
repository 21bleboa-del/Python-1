'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''

#Input
length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))

#Processing
Area = length * width

#Output
print("The calculated area of the rectangle is: ", Area)

