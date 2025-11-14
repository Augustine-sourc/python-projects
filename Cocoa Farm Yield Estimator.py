harvest = int(input("Please enter the number of harvests of Cocoa: \n"))
if harvest < 100 and harvest >= 0:
    income = harvest * 850
    print(f"Your income is GHS {income} since you havested less than 100 bags of cocoa")
elif harvest >= 100:
    income = (harvest * 850) + 2000
    print(f"Your income is GHS {income} since you havested 100 or more bags of cocoa")
else:
    print(f"Please enter a valid number of harvested bags of cocoa")