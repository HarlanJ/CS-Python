#1. Greet user
#2. start counting a running total (running = 0)
#3. Get 5 test scores
#3a. Set up a counter (count = 5)
#3b. begin looping (if count < 5)
#3b1. Ask user for score
#3b2. add answer to running total
#4. Determine average (running / 5)
#5. communicate results
#6. END

#1. Greet user
print("Hello! This program calculates the average of 5 test scores.")
#2. start counting a running total (running = 0)
running = 0.0
#3. Get 5 test scores
#3a. Set up a counter (count = 5)
count = 5
#3b. begin looping (if count < 5 and count >= 0)
while count > 0:
	#3b1. Ask user for score
	#3b2. add answer to running total
	running = running + float(input("What was the score on the test?"))
	#3b3. Subtract from count
	count = count - 1
#4. Determine average (running / 5)
#5. communicate results
print("The average score is:", format(running / 5, ".2f"))
#6. END
input("Thank you for using the program!")