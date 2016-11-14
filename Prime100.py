#John Harlan
#Prime Number function
#CS 100

#------Algorithm------
#1. Ask user for a number to test
#2. store answer (query)
#3a. If query is prime
        #3a1a.create a place to store if the query is prime,defaulting to True
                                                                         #(prime)
        #3a1b. create somplace to store the current number (i) defaulting to 2
        #3a1c. check to see if query is divisible by i
            #3a1c1. if query / the current number has no remainder
                #3a1c2. set prime to false
                #3a1c3. goto 3a1c2
            #3a1c2. increase i by 1
            #3a1c3. goto  3a1c
        #3a1d. return the the value of prime
    #3a2. tell user that the query is prime
    #3a3. goto 4
#3b. If query is not prime
    #3b1. Tell user that the query is not prime
    #3b2. goto 4
#4. end of main function


#-------Program-------
import math

def is_prime(a):
    #3a1a. create a place to store if the query is prime, defaulting to True (prime)
    prime = True

    #3a1b. create somplace to store the current number (i) defaulting to 2
    i = 2
    #3a1c. check to see if query is divisible by i
    while (i < math.sqrt(a) + 1 and prime):
        #3a1c1. if query / the current number has no remainder
        if a % i == 0:
            #3a1c2. set prime to false
            prime = False

            #3a1c3. goto 3a1c2
        #3a1c2. increase i by 1
        i += 1
        #3a1c3. goto  3a1c

    #3a1d. return the the value of prime
    return prime

def main():
    for i in range(1, 100):
        if is_prime(i):
            print(i)

main()
