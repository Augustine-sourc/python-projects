print("***********ROUTES***********")
print(f"Accra => Madina = GHS 5 \n"
      f"Accra => Kasoa = GHS 10 \n"
      f"Accra => Tema = GHS 8 \n")

route = input("Enter your route: ").lower()
passenger_numb = int(input("Enter your number of passengers: "))

if(route == "madina"):
    fare = passenger_numb * 5
    print(f"The total fare for {passenger_numb} passenger(s) is GHS {fare}")
elif(route == "kasoa"):
    fare = passenger_numb * 10
    print(f"The total fare for {passenger_numb} is GHS {fare}")
elif(route == "tema"):
    fare = passenger_numb * 8
    print(f"The total fare for {passenger_numb} is GHS {fare}")
else:
    print("Please enter a valid route (tema or madina or kasoa)")
