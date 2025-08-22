
'''
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
'''

#Input
char = input("Please enter a single character: ")

#Processing
if len(char) == 1 and char.isalpha():
    char = char.lower()

    if char in 'aeiou':
        print("The character is a vowel.")
    else:
        print("The character is a consonant")
else:
    if len(char) != 1:
        print("Error: Please enter only one character")
    else:
        print("Error: The input is not a letter")

#Output: already embedded in the processing section. If I add another output section,
# it will give " The character is a vowel or consonant" and "The entered character is: b".