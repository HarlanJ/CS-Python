# John Harlan
# Stock Transaction
# CS 100

purchased = 2000
buyValue = 40.0
commission = .03 # 3 percent
sellValue = 42.75
sold = 2000

# 1.Calculate amount paid for the stocks
amountPaid = purchased * buyValue

# 2.Calculate commission paid to broker during purchase
purchCommission = amountPaid * commission

# 3.Calculate amount stocks sold for
amountReceived = sold * sellValue

# 4.Calculate the commission paid to broker during sale
sellCommission = amountReceived * commission

# 5.Calculate the total amount left
amountLeft = amountReceived - sellCommission - purchCommission - amountPaid

# 6.Display amount paid for stocks
print("Joe paid", amountPaid, "dollars for his stocks")

# 7.Display commission paid to broker during purchase
print("His broker was paid", purchCommission, "dollars during the purchase")

# 8.Display amount stocks sold for
print("Joe's stocks sold for", amountReceived, "dollars")

# 9.Display the commission paid to broker during sale
print("The broker was paid", sellCommission, "dollars during the sale")

# 10.Display the total amount left
if amountLeft < 0:
    print("Joe lost", abs(amountLeft), "dollars")
else:
    print("Joe made", amountLeft, "dollars")
