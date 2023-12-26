# Input variables from keyboard
temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
pressure = float(input("Enter pressure (hPa): "))

# Define quadratic equation coefficients
a = 0.01
b = -0.5
c = 25

# Calculate weather parameter
precipitation = a * temperature**2 + b * humidity + c

# Print result
print(f"Precipitation: {precipitation}")
