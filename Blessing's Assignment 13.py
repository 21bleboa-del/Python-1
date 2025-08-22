
'''
Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.
===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
'''


#Input
user_input = input("Enter a string: ")

#Processing
is_palindrome = True
for i in range(len(user_input) // 2):
    if user_input[i] != user_input[-(i + 1)]:
        is_palindrome = False
        break

#Output
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")