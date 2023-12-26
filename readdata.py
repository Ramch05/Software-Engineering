import csv

# Define file path
file_path = "weatherHistory.csv"

# Read data from file
with open(file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = next(reader)

temperature = float(data["temperature"])
humidity = float(data["humidity"])
pressure = float(data["pressure"])

# Define quadratic equation coefficients
a = 0.01
b = -0.5
c = 25

# Calculate weather parameter
precipitation = a * temperature**2 + b * humidity + c

# Print result
print(f"Precipitation: {precipitation}")


