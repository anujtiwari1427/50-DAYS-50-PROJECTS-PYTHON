class BMIcalculator:

    def __init__(self,weight,height):
        self.weight = weight
        self.height = height
    
    def calculate_bmi(self):
        bmi = self.weight/(self.height**2)
        return round(bmi,2)
    
    def category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
        
# ---- BMI CALCULATOR WORKING

print("=== BMi calculator")

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

p1 = BMIcalculator(weight,height)

print("You BMI Is : ",p1.calculate_bmi())
print("Category:",p1.category())