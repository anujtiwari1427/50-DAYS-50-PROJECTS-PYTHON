rent = int(input("enter the total rent = "))
food = int(input("enter the total amount of food = "))
electric_spend = int(input("enter the total amount of electric bill = "))
charge_per_unit = int(input("enter the total amount of charge = "))
person = int(input("enter the total number of person = "))
 
total_bill = electric_spend * charge_per_unit

output = (total_bill+food+rent // person )

print(output)