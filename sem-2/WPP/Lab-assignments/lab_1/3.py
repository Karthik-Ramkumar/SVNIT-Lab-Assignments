feet = float(input("Enter length in feet "))

conversions = [
    ("Inches", 12),
    ("Yards", 1/3),
    ("Miles", 1/5280),
    ("Millimeters", 304.8),
    ("Centimeters", 30.48),
    ("Meters", 0.3048),
    ("Kilometers", 0.0003048)
]

print("\nChoose a conversion:")
for i, item in enumerate(conversions, 1):
    print(f"{i}. {item[0]}")

choice = int(input("\nEnter your choice (1-7): "))

if 1 <= choice <= len(conversions):
    unit, factor = conversions[choice - 1]
    result = feet * factor
    print(f"{feet} feet is {result} {unit}.")
else:
    print("Invalid choice")

