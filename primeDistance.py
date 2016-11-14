import os

frameCount = 1
largestDiff = 0

def primeQuery(q):
    for i in range(2, q // 2 + 1):
        if q % i == 0:
            return False
    return True

