
'''
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age.
'''

#Input
age = float(input("Enter your age: "))

#Processing
if age < 18:
    category = "Minor"
elif age <= 65:
    category = "Adult"
else:
    category = "Senior citizen"

#Output
print("The category based on the entered age is: ", category)
