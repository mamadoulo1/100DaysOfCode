# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight/(height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 1.85 <= bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")