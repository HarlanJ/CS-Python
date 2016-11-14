#John Harlan
#Sum Of Numbers
#CS 100

#------ALGORITHM------
#1. Greet user
#2. Create someplace to store the total (total)
#3. ask user for a number
#4. store answer (ans)
#5. begin loop
#5a. if ans is greater than or equal to 0
#5a1. add ans to total
#5a2. Ask user for another number
#5a3. Store answer (ans)
#5a4. goto 5
#5b. is ans is less than 0
#5b1. goto 6
#6. tell the user the sum (total)


#------PROGRAM------
#1. Greet user
print("Welcome! This program calculates the sum of a group of positive numbers,",\
" to close the program and display the result, enter a negative number.")

#2. Create someplace to store the total (total)
total = 0

#3. ask user for a number
#4. store answer (ans)
ans = float(input("Please input a positive number to add, enter a negative to get",\
"sum and leave program\n>"))

#5. begin loop
while ans >= 0:
    #5a. if ans is greater than or equal to 0
    #5a1. add ans to total
    total += ans
    
    #5a2. Ask user for another number
    #5a3. Store answer (ans)
    ans = float(input("Please input another number\n>"))
    
    #5a4. goto 5
    
#5b. is ans is less than 0
#5b1. goto 6
#6. tell the user the sum (total)
print("The total of the numbers you entered was", format(total, ".2f"))
