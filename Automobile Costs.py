#John Harlan
#Automible Costs
#CS 100

#------ALGORITHM------
#01. ask user for monthly loan
#02. store answer
#03. ask user for insurance payment
#04. store answer
#05. ask user for monthly gas money
#06. store answer
#07. ask user for monthly oil expense
#08. store answer
#09. ask user for monthly tire costs
#10. store answer
#11. ask user for monthly maintenance cost
#12. store answer
#13. calculate total cost
#14. save result
#15. tell user total monthly expence
#16. calculate yearly cost (monthly expence * 12)
#17. tell user yearly cost


#-------PROGRAM-------
def get_loan_pmt():
    #01. ask user for monthly loan
    return float(input("What is your monthly loan payment?\n>"))

def get_insurance():
    #03. ask user for insurance payment
    return float(input("What do you you pay monthly for your insurance?\n>"))

def get_gas():
    #05. ask user for monthly gas money
    return float(input("How much money do you spen on gas monthly?\n>"))

def get_oil():
    #07. ask user for monthly oil expense
    return float(input("How much do you spend on oil per month?\n>"))

def get_tires():
    #09. ask user for monthly tire costs
    return float(input("What are your monthly expenses for tour tires?\n>"))

def get_maint():
    #11. ask user for monthly maintenance cost
    return float(input("What are your monthly maintenance costs?\n>"))

def show_expenses(loan, ins, gas, oil, tire, maint):
    #13. calculate total cost
    #14. save result
    expense = loan + ins + gas + oil + tire + maint

    #15. tell user total monthly expence
    print("Your monthly car expenses are $", format(expense, ".2f"), sep='')

    #16. calculate yearly cost (monthly expence * 12)
    #17. tell user yearly cost
    print( "Your yearly car expenses are $", format(expense * 12, ".2f"), sep='')
    return

def main():
    #01. ask user for monthly loan
    #02. store answer
    loan = get_loan_pmt()

    #03. ask user for insurance payment
    #04. store answer
    insurance = get_insurance()

    #05. ask user for monthly gas money
    #06. store answer
    gas = get_gas()

    #07. ask user for monthly oil expense
    #08. store answer
    oil = get_oil()

    #09. ask user for monthly tire costs
    #10. store answer
    tires = get_tires()

    #11. ask user for monthly maintenance cost
    #12. store answer
    maint = get_maint()

    #13. calculate total cost
    #14. save result
    #15. tell user total monthly expence
    #16. calculate yearly cost (monthly expence * 12)
    #17. tell user yearly cost
    show_expenses(loan, insurance, gas, oil, tires, maint)
    return

main()
