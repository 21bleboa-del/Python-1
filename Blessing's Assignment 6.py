
'''
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
'''

#Input
usd = float(input("Enter an amount in usd: "))

#Processing
#Converting the 1 usd to eur = 0.92
exchange_rate = 0.92
eur = usd * exchange_rate

#Output
print("The converted amount in eur is: ", eur)
