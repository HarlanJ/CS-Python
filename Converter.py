import math

print("──────────────────────WELCOME──────────────────────\nThis program converts a number from one base to\nanother\n\n")

def main():
    inputNum = input("What number would you like to convert?\n(comma deliniated list)\n")
    inputBase = int(input("What base is the number?\n"))
    outputBase = int(input("What base do you want?\n"))
    inputPlaces = inputNum.split(',')

    decimalNumber = int(0)

    counter = int(0)
    
    for i in inputPlaces:
        decimalNumber += int(inputPlaces[counter]) * (inputBase ** int(counter))
        counter += 1

    print(decimalNumber)

    output = []

    while decimalNumber > 0:
        temp = decimalNumber
        decimalNumber = decimalNumber // outputBase
        temp = temp % outputBase
        output += [temp]

    output.reverse()
    print(output)
    main()

main()
