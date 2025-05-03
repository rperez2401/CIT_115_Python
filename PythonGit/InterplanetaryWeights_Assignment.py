# Author: Randy P
# Date: 2/18/2025
# CIT-115/115L Python; Professor Brian Candido ; STCC
# Inter Planetary Weights Program

# Constants: Surface Gravity Factor

MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

# INPUT PROMPT

sName = str(input("what is your name: "))
fWeight = float(input(f"What is your weight: "))

# Compute

fMer = fWeight * MERCURY
fVen = fWeight * VENUS
fMoo = fWeight * MOON
fMar = fWeight * MARS
fJup = fWeight * JUPITER
fSat = fWeight * SATURN
fUra = fWeight * URANUS
fNep = fWeight * NEPTUNE
fPlu = fWeight * PLUTO

# Print Weights

print(f"{sName}, here are your weights on our Solar System's Plants:")
print(f"Weight on Mercury: {fMer:10.2f}")
print(f"Weight on Venus:   {fVen:10.2f}")
print(f"Weight on our Moon:{fMoo:10.2f}")
print(f"Weight on Mars:    {fMar:10.2f}")
print(f"Weight on Jupiter: {fJup:10.2f}")
print(f"Weight on Saturn:  {fSat:10.2f}")
print(f"Weight on Uranus:  {fUra:10.2f}")
print(f"Weight on Neptune: {fNep:10.2f}")
print(f"Weight on Pluto:   {fPlu:10.2f}")