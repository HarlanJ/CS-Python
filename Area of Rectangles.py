#John Harlan
#Area of Rectangles
#CS 100

# 1. Greet user
# 2. Ask user for length of first rectangle
# 3. Store answer (length)
# 4. Ask user for width of first rectangle
# 5. Store answer (width)
# 6. Compute area of first rectangle (width * length)
# 7. Store result (area1)
# 8. Ask user for length of second rectangle
# 9. store answer (length)
# 10. Ask user for width of second rectangle
# 11. Store answer (width)
# 12. Compute area of second rectangle (width * height)
# 13. Store result (area2)
# 14. Determine which is bigger
    # 14a. if area1 is greater than area2
        #14a1. Tell user the first rectangle is larger than the second
        #14a2. goto 15
    # 14b. if area2 is greater than area1
        #14b1. Tell user the second rectangle is larger than the first
        #14b2. goto 15
    # 14c. if area1 is the same as area2
        #14c1. Tell user the rectangles have the same area
        #14c2. goto 15
# 15. thank user for use=ing the program
# 16. END


#-----------CODE--------------#

# 1. Greet user
print("Hello, this program determines which of two rectangles is larger.")

# 2. Ask user for length of first rectangle
# 3. Store answer (length)
length = float(input("What is the length of the first rectangle?"))

# 4. Ask user for width of first rectangle
# 5. Store answer (width)
width = float(input("What is the width of the first rectangle?"))

# 6. Compute area of first rectangle (width * length)
# 7. Store result (area1)
area1 = length * width;

# 8. Ask user for length of second rectangle
# 9. store answer (length)
length = float(input("What is the length of the second rectangle?"))

# 10. Ask user for width of second rectangle
# 11. Store answer (width)
width = float(input("What is the width of the second rectangle?"))

# 12. Compute area of second rectangle (width * height)
# 13. Store result (area2)
area2 = (width * height)

# 14. Determine which is bigger
    # 14a. if area1 is greater than area2
    if area1 > area2:
        #14a1. Tell user the first rectangle is larger than the second
        print("The first rectangle is larger than the second.")
        #14a2. goto 15
    # 14b. if area2 is greater than area1
    elif area2 > area1:
        #14b1. Tell user the second rectangle is larger than the first
        print("The second rectangle is larger than the first.")
        #14b2. goto 15
    # 14c. if area1 is the same as area2
    elif area1 == area2:
        #14c1. Tell user the rectangles have the same area
        print("The rectangles are the same size")
        #14c2. goto 15
# 15. thank user for useing the program
print("Thank you for using my program")
# 16. END
exit()
