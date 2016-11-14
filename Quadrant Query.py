#John Harlan
#Quadrant Query
#CS 100

# 1. create variable, defaulting to "y" (yes) that will be used for repeatability
newPoint = "y";

# 2. Introduce Program
print("This program gives you info about where points lie on the Cartesian plane.")

# 3. Begin while loop for repeatability
while newPoint == "y":
    # 4. Ask user for x coordinate
    # 5. Store answer
    xCoord = float(input("What is the \'x\' coordinate of the point?\n>"))

    # 6. Ask user for y coordinate
    # 7. Store answer
    yCoord = float(input("What is the \'y\' coordinate of the point?\n>"))


    # 8. Determine where the point lies and tell user where

    # 8a1. Determine if the point is on the origin (0,0)
    # 8a2. Tell user the point is on the origin
    if xCoord == 0 and yCoord == 0:
        print("The point (", format(xCoord, ".3f"), ",", format(yCoord, ".3f"), ") lies on the origin.")

    # 8b1. Determine if the point is on the Y-Axis (X equals 0)
    # 8b2. Tell user the point is on the Y-Axis 
    elif xCoord == 0:                                                                                             # Y-AXIS
        print("The point (", format(xCoord, ".3f"), ",", format(yCoord, ".3f"), ") lies on the Y-axis.")

    # 8c1. Determine if the point is on the X-Axis (Y equals 0)
    # 8c2. Tell user the point is on the X-Axis 
    elif yCoord == 0:                                                                                             # X-AXIS
        print("The point (", format(xCoord, ".3f"), ",", format(yCoord, ".3f"), ") lies on the X-axis.")

    # 8d1. Determine if the point is in the First Quadrant (both positive)
    # 8d2. Tell user the point is in the First Quadrant
    elif xCoord > 0 and yCoord > 0:                                                                               # QUAD-1
        print("The point (", format(xCoord, ".3f"), ",", format(yCoord, ".3f"), ") is in the first Quadrant")

    # 8e1. Determine if the point is in the Second Quadrant (X negative, y positive)
    # 8e2. Tell user the point is in the Second Quadrant
    elif xCoord < 0 and yCoord > 0:                                                                               # QUAD-2
        print("The point (", format(xCoord, ".3f"), ",", format(yCoord, ".3f"), ") is in the second Quadrant")

    # 8f1. Determine if the point is in the Third Quadrant (both negative)
    # 8f2. Tell user the point is in the Third Quadrant
    elif xCoord < 0 and yCoord < 0:                                                                               # QUAD-3     
        print("The point (", format(xCoord, ".3f"), ",", format(yCoord, ".3f"), ") is in the third Quadrant")

    # 8g1. Determine if the point is in the Fourth Quadrant (X positive, Y negative)
    # 8g2. Tell user the point is in the Fourth Quadrant
    elif xCoord > 0 and yCoord < 0:                                                                               # QUAD-4
        print("The point (", format(xCoord, ".3f"), ",", format(yCoord, ".3f"), ") is in the fourth Quadrant")


    # 10. Ask user if they would like to enter another point
    # 11. Store answer
    newPoint = input("\n\n-----------------------\nWould you like to enter another point? (y/n)\n>");

    # 12. (LOOP) if the answer is something the computer isn't expecting
    while not(newPoint == 'y' or newPoint == 'n'):
        # 12a. Clarify what the computeris expecting and get new input
        # 12b. Store answer
        print(newPoint)
        newPoint = input("Please only input \'y\' or \'n\'.\n>")

# 13. Thank user for using program
print("Thanks for using my program.")

# 14. END
exit()
