# Hard-coded variables
temperature = 20  # Degrees Celsius
humidity = 60  # Percentage
pressure = 1013  # hPa

# Quadratic equation coefficients
a = 0.01
b = -0.5
c = 25

# Calculate weather parameter (e.g., precipitation)
precipitation = a * temperature**2 + b * humidity + c

# Print result
print(f"Precipitation: {precipitation}")
