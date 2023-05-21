import math

def calculate_area(a, b, c):
    # Check if the combination of sides is possible
    if a + b > c and b + c > a and c + a > b:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2

        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return None

# Example 
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

triangle_area = calculate_area(side1, side2, side3)

if triangle_area is not None:
    print("The area of the triangle is:", triangle_area)
else:
    print("The given sides cannot form a triangle.")

