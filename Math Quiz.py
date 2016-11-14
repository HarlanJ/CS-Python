#John Harlan
#Math Quiz (231)
#CS 100

#------Algorithm------
#1. greet user
#2. store a random number to quiz user with (num1)
#3. stroe a random number to quiz user with (num2)
#4. quiz the user
#5. ask user the question (num1 + num2)
#6. store answer
#7. determine if the user is correct
#8a. if the user is correct
    #8a1. notify user that they're right
#8b. if user is incorrect
    #8b1. tell user they were not correct
    #8b2. tell user the correct answer


#-------Program-------
import random


def getRandom():
    return random.randint(0, 999)

def quiz(a, b):
    #5. ask user the question (num1 + num2)
    print(" ", a, "\n+", b, "\n____", sep='')

    #6. store answer
    ans = int(input(''))
    return ans

def isCorrect(ans, a, b):
    #8a. if the user is correct
    if(ans == a + b):
        #8a1. notify user that they're right
        print("Congratualtions! You are correct!")
    #8b. if user is incorrect
    else:
        #8b1. tell user they were not correct
        #8b2. tell user the correct answer
        print("Incorrect, the answer is:", a + b)
    return

def main():
    #1. greet user
    print("Hello! This program will quiz you on 10 addition problems")

    #2. store a random number to quiz user with (num1)
    num1 = getRandom()

    #3. stroe a random number to quiz user with (num2)
    num2 = getRandom()

    #4. quiz the user
    answer = quiz(num1, num2)

    #7. determine if the user is correct
    isCorrect(answer, num1, num2)
    return

for i in range(10):
    main()
