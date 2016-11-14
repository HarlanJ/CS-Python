#John Harlan
#Celsius to Fahrenheit Converter
#CS 100

# Ask user for input
# Store input (celsius)
celsius = float(input("What temperature Celsius would you like to convert?\n>"))

# Perform calculation for Celsius to Fahrenheit (F = ((C * 9) / 5) + 32)
# Store result (fahrenheit)
fahrenheit = ((celsius * 9) / 5) + 32.0

# Perform calculation for Celsius to Kelvin (K = C + 273)
# Store Result (kelvin)
kelvin = celsius + 273.0

# Tell user result
print(celsius, "Celsius is", fahrenheit, "degrees Fahrenheit and", kelvin, "Kelvin")

# END
