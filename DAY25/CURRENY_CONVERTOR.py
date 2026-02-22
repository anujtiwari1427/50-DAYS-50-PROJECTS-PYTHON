# ==============================
# Currency Converter Project
# Base Currency: INR
# ==============================

# Exchange rates (Example static rates)
exchange_rates = {
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.0095,
    "JPY": 1.80,
    "AUD": 0.018,
    "CAD": 0.016
}

def show_menu():
    print("\n===== Currency Converter (INR Base) =====")
    print("Available Currencies:")
    for currency in exchange_rates:
        print("->", currency)
    print("Type 'exit' to quit")

def convert_from_inr(amount, target_currency):
    if target_currency in exchange_rates:
        converted = amount * exchange_rates[target_currency]
        return round(converted, 2)
    else:
        return None

def main():
    while True:
        show_menu()
        
        choice = input("\nEnter target currency: ").upper()
        
        if choice == "EXIT":
            print("Thank you for using Currency Converter!")
            break
        
        try:
            amount = float(input("Enter amount in INR: "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue
        
        result = convert_from_inr(amount, choice)
        
        if result is None:
            print("Invalid currency code!")
        else:
            print(f"{amount} INR = {result} {choice}")

if __name__ == "__main__":
    main()