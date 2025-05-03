# Randy P
# 03/24/2025 - 04/01/2025
# CIT/115/115L Python Professor Candido

#### Grade Analyzer V.2 ####

### Prompt name

sName = str(input("What is your name? "))

### Loop Test Score Prompt
## Prompt Test Scores
while True:
    try:
        while (iTest1 := int(input("Test 1: "))) <= 0:
            print("Test scores must be greater than 0.")
        while (iTest2 := int(input("Test 2: "))) <= 0:
            print("Test scores must be greater than 0.")
        while (iTest3 := int(input("Test 3: "))) <= 0:
            print("Test scores must be greater than 0.")
        while (iTest4 := int(input("Test 4: "))) <= 0:
            print("Test scores must be greater than 0.")
        break
    except ValueError:
        print("Input must be a numeric value")
        
print(iTest1, iTest2, iTest3, iTest4)
### Prompt Drop Lowest Grade?
while True:
    sDropLowest = str(input("Do you wish to Drop the Lowest Grade Y or N? ")).lower()

    ## Set Divisor
    if sDropLowest != "n" and sDropLowest != "y":
        print("Input must be character letter Y or N")
        continue
    
    if sDropLowest.lower() == "y":
       fltDivisor = 3.0
       if   iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4:
            iLowest = iTest1
            break
       elif iTest2 < iTest3 and iTest2 < iTest4:
            iLowest = iTest2
            break
       elif iTest3 < iTest4:
            iLowest = iTest3
            break
       else:
            iLowest = iTest4
            break
    else:
       iLowest = 0
       fltDivisor = 4.0
       break

fAvgScore = (iTest1 + iTest2 + iTest3 + iTest4 - iLowest) / fltDivisor

### Print Name and Average Score
print(f"{sName}'s test average is: {fAvgScore: .1f}")

### Print Letter Grade
if fAvgScore >= 97.0:
    print("Letter Grade for the test is: A+")

elif fAvgScore >= 94.0:
    print("Letter Grade for the test is: A")

elif fAvgScore >= 90.0:
    print("Letter Grade for the test is: A-")

elif fAvgScore >= 87.0:
    print("Letter Grade for the test is: B+")

elif fAvgScore >= 84.0:
    print("Letter Grade for the test is: B")

elif fAvgScore >= 80.0:
    print("Letter Grade for the test is: B-")

elif fAvgScore >= 77.0:
    print("Letter Grade for the test is: C+")

elif fAvgScore >= 74.0:
    print("Letter Grade for the test is: C")

elif fAvgScore >= 70.0 :
    print("Letter Grade for the test is: C-")

elif fAvgScore >= 67.0 :
    print("Letter Grade for the test is: D+")

elif fAvgScore >= 64.0:
    print("Letter Grade for the test is: D")

elif fAvgScore >= 60.0:
    print("Letter Grade for the test is: D-")

else:
    print("Letter Grade for the test is: F")
exit()

#### End of Program Code ####
