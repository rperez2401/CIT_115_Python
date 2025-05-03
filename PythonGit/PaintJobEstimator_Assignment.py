# Randy P
# 04/21/2025 - 04/27/2025
# CIT/115/115L Python Professor Candido

#### Paint Job Estimator ####

import math

### Define All Necessary Functions ###

## Prompts for input and stores as a float
def getFloatInput(s_prompt):
    flt_number = -1
    while flt_number < 1:
        try:
            flt_number = float(input(s_prompt))
            if flt_number < 1:
                print("Input must be a positive numeric value.")
        except ValueError:
            print("Input must be a positive numeric value")
    return flt_number

## Get gallons of paint. Takes two parameters: Square Feet of Wall, Feet Per Gallon
# Gallons of paint come in only whole numbers - Round up only, return Integer.

def getGallonsOfPaint(sqr_ft_of_wall, ft_per_gallon):
    return math.ceil(sqr_ft_of_wall / ft_per_gallon)

## Get total amount of labor hours needed to paint a wall. Two Parameters: Hours of labor per gallon and total gallons.
# Labor Hours are variable - Return Float

def getLaborHours(labor_hrs_per_gallon, total_gallons):
    return total_gallons * labor_hrs_per_gallon

## Get total cost of labor. Takes two parameters: Labor Charge per hour and total labor hours
# Return Float

def getLaborCost(labor_total_hrs, labor_charge_per_hr):
    return labor_total_hrs * labor_charge_per_hr

## Get cost of pain supplies. Takes two parameters: Paint Price Per Gallon, Total Gallons
# Return Float

def getPaintCost(price_per_gallon, total_gallons):
    return price_per_gallon * total_gallons

## Get Sales Tax based on predetermined list of taxes. One Parameter: StringInput
# Return Float

def getSalesTax(state):
    while True:
        try:
            match str(state.lower()):
                case "ct" | "vt":
                    return 0.06
                case "ma":
                    return 0.0625
                case "me":
                    return 0.085
                case "ri":
                    return 0.07
                case _:
                    return 0.0
        except ValueError:
            print("Input must be a positive numeric value")

## Show cost estimates must print to screen and export data

def showCostEstimates(total_gallons, total_hrs, paint_cost, labor_cost, sales_tax, name):
    tax = (paint_cost + labor_cost) * sales_tax
    total_cost = tax + paint_cost + labor_cost
    print(f"Gallons of paint: {total_gallons}")
    print(f"Hours of labor: {total_hrs:.1f}")
    print(f"Paint charges: ${paint_cost:,.2f}")
    print(f"Labor charges: ${labor_cost:,.2f}")
    print(f"Tax: ${tax:,.2f}")
    print(f"Total cost: ${total_cost:,.2f}")

## output to file
    with open(f'{name}_PaintJobOutput.txt', 'w') as outfile:
        outfile.write(f"Gallons of paint: {total_gallons}"'\n')
        outfile.write(f"Hours of labor: {total_hrs}"'\n')
        outfile.write(f"Paint charges: ${paint_cost:,.2f}"'\n')
        outfile.write(f"Labor charges: ${labor_cost:,.2f}"'\n')
        outfile.write(f"Tax: ${tax:,.2f}"'\n')
        outfile.write(f"Total cost: ${total_cost:,.2f}"'\n')
## print file name
    print(f"File: {name}_PaintJobOutput.txt was created.")

## Main()

def main():

    # Prompt for variable values
    fltSqr_Ft_Wall = getFloatInput("Enter wall space in square feet: ")
    fltPaint_Price = getFloatInput("Enter paint price per gallon: ")
    fltFt_Per_Gallon = getFloatInput("Enter feet per gallon: ")
    fltLabor_Per_Gallon = getFloatInput("How many labor hours per gallon: ")
    fltLabor_Chrg_Hr = getFloatInput("Labor charge per hour: ")
    strState = input("State job is in: ")
    strName = input("Customer Last Name: ")

    # Call function calculations
    intTotal_Gal = getGallonsOfPaint(fltSqr_Ft_Wall, fltFt_Per_Gallon)
    fltLabor_Hrs = getLaborHours(fltLabor_Per_Gallon, intTotal_Gal)
    fltLabor_Cost = getLaborCost(fltLabor_Hrs, fltLabor_Chrg_Hr)
    fltPaint_Cost = getPaintCost(fltPaint_Price, intTotal_Gal)
    fltSales_Tax = getSalesTax(strState)

    # Call Cost Estimate Function
    showCostEstimates(intTotal_Gal,fltLabor_Hrs,fltPaint_Cost,fltLabor_Cost,fltSales_Tax,strName)
## End of Program ##

### Run Program###
main()



