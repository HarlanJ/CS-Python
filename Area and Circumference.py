#Calculate the area and circumference of a circle from its radius
# 1. prompt for radius
# 2. apply area formula
# 3. apply circumference formula
# 4. Display area and circumference

import math

radius = int(input("Enter the radius of the circle:\n"))

area = math.pi * math.pow(radius, 2);
circumference = math.pi * radius * 2

print("The area of a circle with radius", radius, "is", area, "\nThe circumference is", circumference)
