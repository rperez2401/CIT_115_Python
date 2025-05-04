# rperez
# 05/05/2025 - 05/10/2025
# CIT/115/115L Python Prof C

#### Real Estate Analyzer ####

### Define All Necessary Functions ###

## Prompts for input and stores as a float
def getFloatInput(strPrompt):
    while True:
        try:
            flt_number = float(input(strPrompt))
            if flt_number <= 0:
                continue
            return flt_number
        except ValueError:
            print("Input a number that is greater than 0.")
    return flt_number

## Get MEDIAN
# Takes in list argument
def getMedian(lst_Sales):
    flt_Length = len(lst_Sales) # Grabs length of list

    if flt_Length % 2 == 0: # Checks if list length is even
        flt_MidNum1 = flt_Length // 2
        flt_MidNum2 = flt_MidNum1 -1
        return (lst_Sales[flt_MidNum1] + lst_Sales[flt_MidNum2]) / 2


    else: # If Odd, return whole number value for median
        flt_MidNum = flt_Length // 2
        return lst_Sales[flt_MidNum]

## Define Main()
def main(): # Program Function

    # empty list
    lst_Sales = []

    # Prompt user to fill list using the append method
    while True:
        lst_Sales.append(getFloatInput("Enter property sales value: "))
        while True:
            str_AddMore = input("Add another sale? (Y/N)").upper()
            if str_AddMore not in ['Y', 'N']:
                print("Please enter Y or N.")
                continue
            if str_AddMore == 'N':
                break # return to greater loop with 'N' value
            else:
                break #return to greater loop with 'Y' value
        if str_AddMore == 'Y':
            continue # Loop list input
        else:
            break # Continue Main Function
    lst_Sales.sort() # Sort list from low to high value
    flt_Count = len(lst_Sales)
    # Min
    flt_Minimum = lst_Sales[0]
    # Max
    flt_Maxmimum = lst_Sales[-1]
    # Sum
    flt_TotalSum = sum(lst_Sales)
    # AVG
    flt_Avg = flt_TotalSum/flt_Count
    # Commission
    flt_Comm = flt_TotalSum * 0.03
    # MED
    flt_Median = getMedian(lst_Sales)

    ## Print Data
    for sale_count in range(0, flt_Count): # Prints list
        print(f"Property {sale_count + 1} $ {lst_Sales[sale_count]:>15,.2f}")
    print(f"Minimum:    $ {flt_Minimum:>15,.2f}")
    print(f"Maximum:    $ {flt_Maxmimum:>15,.2f}")
    print(f"Total:      $ {flt_TotalSum:>15,.2f}")
    print(f"Average:    $ {flt_Avg:>15,.2f}")
    print(f"Median:     $ {flt_Median:>15,.2f}")
    print(f"Commission: $ {flt_Comm:>15,.2f}")
#### End of Program ####

### Start Program ###
## Call Main()
main()