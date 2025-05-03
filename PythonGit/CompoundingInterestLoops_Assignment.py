# Randy P
# 04/07/2025 - 04/13/2025
# CIT/115/115L Python Professor Candido

#### Compounding Interest Loops ####

### Global Variables
Month = 0
###

### Define Functions ###
## This Function calculates the monthly balance and prints to screen
def calc_monthly_balance(flt_principalBalance, flt_compoundedInterestRate, int_compoundedMonthsInAYear):
    global Month
    while Month < int_compoundedMonthsInAYear:
        flt_principalBalance *=  flt_compoundedInterestRate # Multiplies principal balance w/ compounded interest rate
        Month += 1 # Add month to Month Variable
        print(f"Month: {Month} Account Balance is: ${flt_principalBalance: ,.2f}")
    return flt_principalBalance

## This Function calculates how many months it'll take to reach target goal and prints to screen
def calc_months_total(flt_principalBalance, flt_accountBalance, flt_goalTotal, flt_compoundedInterestRate):
    global Month
    if flt_goalTotal == 0: # Ignore others and don't print anything
        pass
    elif flt_accountBalance > flt_goalTotal: # Calculate how many month it took to reach past goal
        Month = 0
        while flt_principalBalance < flt_goalTotal:
            flt_principalBalance *= flt_compoundedInterestRate  # Multiplies principal balance w/ compounded interest rate
            Month += 1  # Add month to Month Variable
        print(f"It will take: {Month} months to reach the goal of ${flt_goalTotal: ,.2f}")
    else: # Calculate how many months until you pass goal
        while flt_accountBalance < flt_goalTotal:
            flt_accountBalance *= flt_compoundedInterestRate
            Month += 1 # Add month to Month Variable
        print(f"It will take: {Month} months to reach the goal of ${flt_goalTotal: ,.2f}")

## Prompt for integer value
def prompt_for_input_integer(s_prompt):
    intNumber = 0
    while intNumber <= 0:
        try:
            intNumber = int(input(s_prompt))
            if intNumber <= 0:
                print("Input must be a positive numeric value.")
        except ValueError:
            print("Input must be a positive numeric value.")
    return intNumber
## Prompt for float value
def prompt_for_input_float(s_prompt):
    fltNumber = 0
    while fltNumber <= 0:
        try:
            fltNumber = float(input(s_prompt))
            if fltNumber <= 0:
                print("Input must be a positive numeric value.")
        except ValueError:
            print("Input must be a positive numeric value")
    return fltNumber

## Prompt for total goal value
def prompt_for_input_goal(s_prompt):
    fltNumber = -1
    while fltNumber < 0:
        try:
            fltNumber = float(input(s_prompt))
            if fltNumber < 0:
                print("Input must be 0 or greater.")
        except ValueError:
            print("Please enter a valid number that is 0 or greater.")
    return fltNumber

## This Function runs the program
def main():
    ### Prompt input for variables
    flt_principalBalance = prompt_for_input_float("What is the Original Deposit (positive value): ")
    flt_InterestRate = prompt_for_input_float("What is the Interest Rate (positive value): ")/100 #interest rate as a percentage
    int_compoundedMonthsInAYear = prompt_for_input_integer("What is the Number of Months (positive value): ")
    flt_goalTotal = prompt_for_input_goal("What is the Goal Amount (can enter 0 but not negative): ")

    ### Calculate Compounded Interest Rate
    flt_compoundedInterestRate = (1 + (flt_InterestRate/int_compoundedMonthsInAYear))

    ## Run calculations
    flt_accountBalance = calc_monthly_balance(flt_principalBalance, flt_compoundedInterestRate, int_compoundedMonthsInAYear)
    calc_months_total(flt_principalBalance, flt_accountBalance, flt_goalTotal, flt_compoundedInterestRate)

    exit()
## End of Program Code ##



### Start Program ###
main()