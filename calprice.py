amt = int(input("enter your amount :"))
payment = input("payment method (credit,cash):")
if amt > 1000 :
    amt -= amt * .03
if payment == 'credit':
    amt -= 100
amt += amt * .18    
print("total price is : ", amt)