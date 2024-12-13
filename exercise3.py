# Exercise 03

# Prompt the user to enter their weight and height, and evaluate the input to allow numeric input
Weight = eval(input("Please enter the weight of your body: "))  
height = eval(input("Please enter the height of your body: "))

BMI = Weight / height**2

# BMI classification based on the calculated BMI value
if BMI < 18.5:
    print("You are underweight")  
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are Normal") 
elif BMI >= 25 and BMI <= 29.9:
    print("You are Overweight") 
else:
    print("You are Obese") 
