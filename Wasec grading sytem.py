grades = float(input("Enter your scores you had in your exam:\n"))

if(grades >= 80 and grades <= 100):
    print(f"You had an A")
elif(grades >= 70 and grades <= 79):
    print(f"You had an B")
elif(grades >= 60 and grades <= 69):
    print(f"You had an C")
elif(grades >= 50 and grades <= 59):
    print(f"You had an D")
elif(grades >= 40 and grades <= 49):
    print(f"You had an E")
elif(grades >= 0 and grades <= 39):
    print(f"You had an F")
else:
    print(f"Invalid input...Please enter a valid input")