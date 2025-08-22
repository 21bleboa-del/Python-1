
'''
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
'''

#Input
hours = float(input("Enter a time duration in hours: "))

#Processing
minutes = hours * 60
seconds = hours * 3600

#Output
print("The converted time duration in minutes and seconds are: ", minutes + seconds)
