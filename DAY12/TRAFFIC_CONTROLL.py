vehicles = int(input("Enter number of vehicles: "))

if vehicles > 50:
    print("Green light: 60 seconds")
elif vehicles > 20:
    print("Green light: 40 seconds")
else:
    print("Green light: 20 seconds")
    