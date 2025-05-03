# rperez
# 03/08/2025 - 03/10/2025
# CIT/115/115L Python Prof C

#### Temperature Conversion Program ####


print("Randy's Temp Converter: ")

### Prompt input



## Variable for Numerical Value
fTemperature = float(input("Enter a temperature value: "))

## Variable for Unit Measurement
sTempUnit = str(input("Is the temp F for Fahrenheit or C for Celsius?: "))


### Iniate calculation based on unit input
match sTempUnit:
    ## Converting to Celsius
    case "f" | "F":
        match fTemperature:

            # Invalid Temperature
            case _ if fTemperature > 212:
                print("Temp can not be >212.")

            # Valid Temperature
            case _:
                fCelsius= (5.0/9)* (fTemperature - 32)
                print(f"The Celsius equivalent is: {fCelsius: .1f}°C")

    ## Converting to Fahrenheit
    case "c" | "C":
        match fTemperature:

            # Invalid Temperatue
            case _ if fTemperature > 100:
                print("Temp can not be >100.")

            # Valid Temperature
            case _:
                fFahrenheit = ((9.0/5.0 * fTemperature) + 32)
                print(f"The Fahrenheit equivalent is: {fFahrenheit: .1f}°F")


    ## Improper Unit
    case _:
        print("You must enter a F or C")
