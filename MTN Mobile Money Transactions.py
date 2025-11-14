amount = float(input("Please enter the amount you'd like to send:\n "))
if(amount <= 100):
    charges = 2
    print(f"Dear customer you have sent GHS {amount} and a charge of GHS {charges} has been deducted from your main account")
elif(amount > 100 and amount <= 500):
    charges = 5
    print(f"Dear customer you have sent GHS {amount} and a charge of GHS {charges} has been deducted from your main account")
elif(amount > 500 ):
    charges = 10
    print(f"Dear customer you have sent GHS {amount} and a charge of GHS {charges} has been deducted from your main account")
else:
    print(f"Please enter a valid amount to send")