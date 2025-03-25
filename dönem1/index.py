import math

# Function to calculate the area of the circle base of the cylinder
def calculate_area(radius):
    return radius * radius * math.pi

# Function to calculate the volume of the cylinder
def calculate_volume(area, length):
    return area * length

# Replace these placeholders with user input in an interactive environment
radius = float(input("Enter the radius: "))
length = float(input("Enter the length of a cylinder: "))

area = calculate_area(radius)
volume = calculate_volume(area, length)

print(f"The area is {area:.4f}")
print(f"The volume is {volume:.1f}")
