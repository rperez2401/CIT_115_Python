# Randy P
# 2/24/2025
# CIT/115/115L Python Professor Candido

#Compounding interest program

# Prompting Input

fPV = float(input("Enter the starting principal: "))

fRate = float(input("Enter the annual interest rate: "))/100

iM = int(input("How many times per year is the interest compounded? "))

fPeriods= float(input("For how many years will the account earn interest? "))

# Calculate interest

nRate = (1 + (fRate/iM))

nExpo = iM * fPeriods

fFV = fPV * (nRate ** nExpo)



# Print Calculation

print(f"At the end of {fPeriods} years you will have ${fFV: ,.2f}")




# Prompting Input

float_Principal = float(input("Enter the starting principal: "))

float_Interest_Rate = float(input("Enter the annual interest rate: "))/100

integer_compoundedMonthsInAYear = int(input("How many times per year is the interest compounded? "))

float_Years_Recurring= float(input("For how many years will the account earn interest? "))

# Calculate interest

float_CompoundedInterestRate = (1 + (float_Interest_Rate/integer_compoundedMonthsInAYears))

Exponent = integer_compoundedMonthsInAYear * float_Years_Recurring

AmountTotal = float_Principal * (float_CompoundedInterestRate ** Exponent)



# Print Calculation

print(f"At the end of {fPeriods} years you will have ${fFV: ,.2f}")