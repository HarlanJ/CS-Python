#John Harlan
#Prime Query (GHP 11-13)
#CS 100


#------ALGORITHM------
#1. Greet user
#2. Create place to hold onto the number you're testing (test)
#3.  if test is greater than 0
    #3a. Ask user for a number to test
    #3b. Store number
    #3c. If test is greater than 0
        #3c1. Default the answer to the test as prime
        #3c2. go through all the whole numbers between 2 and half of test,
        #3c2CONT. storing them in 'i'

            #3c2a. if the remainder of test divided by i is zero                
                #3c2a1. Change the answer to the test to being not a prime                
            #3c2b if the remainder of test divided by i is not zero
                #3c2b1. Continue to 3c3                
        #3c3. Tell the user if the number is prime
        #3c4. Goto 3        
#3d. If test is less than or equal to zero
    #3d1. goto 4 
#4. Thank the user
#5 END




#------PROGRAM------
#1. Greet user
print("This program will determine if the integer you enter is a prime number.\n"  \
      "-----------------------------------------------------------------------\n")

#2. Create place to hold onto the number you're testing (test)
test = 1

#3.  if test is greater than 0
while test > 0:
    #3a. Ask user for a number to test
    #3b. Store number
    test = int(input("Please enter an integer to test a prime number or " \
                     "enter 0 to quit\n>"))

    #3c. If test is greater than 0
    if test > 0:
        
        #3c1. Default the answer to the test as prime
        statement = "is a prime number."

        #3c2. go through all the whole numbers between 2 and half of test,
        #3c2CONT. storing them in 'i'
        for i in range(2, test // 2):
            
            #3c2a. if the remainder of test divided by i is zero
            if test % i == 0:
                
                #3c2a1. Change the answer to the test to being not a prime
                statement = "is not a prime number."
                
            #3c2b if the remainder of test divided by i is not zero
                #3c2b1. Continue to 3c3
                
        #3c3. Tell the user if the number is prime
        print("You entered", test, "and", test, statement, "\n")
        #3c4. Goto 3
        
#3d. If test is less than or equal to zero
    #3d1. goto 4
        
#4. Thank the user
print("Thanks for using my program.")

#5 END
