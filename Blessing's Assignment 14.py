
'''
Challenge: Handle negative exponents efficiently.
====================================
Description: Develop a function named power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.
'''


#Input
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

#Processing
def power(base, exponent):
    result = 1
    if exponent >= 0:
        for _ in range(exponent):
            result *= base
    else:
        for _ in range(-exponent):
            result *= base
        result = 1 / result
    return result

#Output
print(power(base, exponent))