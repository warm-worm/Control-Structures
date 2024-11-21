###
# Program that simulates the operation of an electronic thermometer.
# It is extremely hot, for a temperature above 35 degrees,
# It is hot, for a temperature above 30 degrees,
# It is warm, for a temperature of at least 15 degrees,
# It is cold, for a temperature of at least 0 degrees,
# Warning, frost, for a temperature below 0 degrees.
#
temperature = int(input("Enter the temperature: "))
if temperature > 35:
    print("It's extermely hot!")
elif temperature > 30:
    print("It's hot.")
elif temperature >= 15:
    print("It's warm.")
elif temperature >= 0:
    print("It's cold.")
elif temperature < 0:
    print("Warning, frost!")
