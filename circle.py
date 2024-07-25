def Findarea(radius):
    PI = 3.142
    
    return PI * (radius * radius)
print("Area of the circle is", Findarea(5))



def calculate_diameter(radius):
    """
    Function to calculate the diameter of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle
    
    Returns:
    float: The diameter of the circle
    """
    return 2 * radius

# Example usage:
radius = 9
diameter = calculate_diameter(radius)
print(f"The diameter of the circle with radius {radius} is {diameter}")



# All Formulae
# Import necessary libraries
import math

# List of mathematical formulas
formulas = {
    "Area of a Circle": "π * r^2",
    "Circumference of a Circle": "2 * π * r",
    "Area of a Triangle": "(1/2) * b * h",
    "Area of a Rectangle": "l * w",
    "Perimeter of a Rectangle": "2 * (l + w)",
    
    
    "Area of a Square": "a^2",
    "Perimeter of a Square": "4 * a",
    "Pythagorean Theorem": "a^2 + b^2 = c^2",
    "Quadratic Formula": "(-b ± √(b^2 - 4ac)) / 2a",
    "Slope of a Line": "(y2 - y1) / (x2 - x1)",
    
    "Distance Formula": "√((x2 - x1)^2 + (y2 - y1)^2)",
    "Midpoint Formula": "((x1 + x2) / 2, (y1 + y2) / 2)",
    "Simple Interest": "P * r * t",
    "Compound Interest": "P * (1 + r/n)^(nt)",
    
    "Volume of a Cube": "a^3",
    "Volume of a Rectangular Prism": "l * w * h",
    "Volume of a Cylinder": "π * r^2 * h",
    "Volume of a Cone": "(1/3) * π * r^2 * h",
    
    "Volume of a Sphere": "(4/3) * π * r^3",
    "Surface Area of a Sphere": "4 * π * r^2",
    "Euler's Formula": "e^(iπ) + 1 = 0"
}

# Print all formulas
print("List of Fundamental Mathematical Formulas:\n")
for name, formula in formulas.items():
    print(f"{name}: {formula}")
