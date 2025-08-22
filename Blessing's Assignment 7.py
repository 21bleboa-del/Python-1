
'''
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.
'''

#Input
year = float(input("Enter a year: "))

#Processing
if ((year % 4 == 0 and year % 100 != 0)
    or (year % 400 == 0)):
    result = "Leap year"
else:
    result = "Not a leap year"

#Output
print("The entered year is: ", result)