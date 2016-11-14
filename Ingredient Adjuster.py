#John Harlan
#Ingredient Adjuster
#CS 100

# 48 cookies = 1.5 cups of sugar + 1 cup of butter + 2.75 cups of flour

def main():
    # Ask user for number of cookies
    # Store answer (cookies)
    cookies = float(input("How many cookies would you like to make?\n>"))

    # Calulate sugar ((1.5 * cookies) / 48)
    # Store answer (sugar)
    sugar = (1.5 * cookies) / 48.0

    # Calculate butter (cookies / 48)
    # Store answer (butter)
    butter = cookies / 48

    # Calculate flour ((2.75 * cookies) / 48)
    # Store answer (flour)
    flour = (2.75 * cookies) / 48

    # Tell user results
    print("To make ", cookies, " cookies, you will need:\n", \
          format(sugar, '.2f'), " cups of sugar\n", \
          format(butter, '.2f'), " cups of butter\n", \
          format(flour, '.2f'), " cups of flour", sep='')
    redoQuery()

    
def redoQuery():
    
    # -->>EXTRA<<--
    #┌  Ask user if they would like to check another batch size
    #│  Store answer (yn)
    #│
    #│    ┌──────────┐ yes
    #│    │ Is yn y? ├─────────────┐
    #│    └─────┬────┘   ┌─────────┴───────┐
    #│          │no      │ restart program │
    #│          │        └─────────────────┘
    #│          │
    #│    ┌─────┴────┐ yes
    #│    │ Is yn n? ├────────────┐
    #│    └─────┬────┘    ┌───────┴──────┐
    #│          │ no      │ Exit program │
    #│          │         └──────────────┘
    #│          │
    #│  ┌───────┴───────────────┐
    #│  │ Ask user to try again │
    #│  └───────┬───────────────┘
    #└──────────┘
    
    yn = input("Would you like to check another batch size? (y/n)\n>")
    if yn == 'y':
        main()
    elif yn =='n':
        exit()
    else:
        print("Please enter only a lowercase \'y\' or lowercase \'n\'," \
              "then press enter")
        redoQuery()

# Run program
main()
# END       
