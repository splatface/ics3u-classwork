system = int(input("Type: 1 for imperial, 2 for metric measurements: "))

if system == 1:
    height = float(input("Height in inches: "))
    weight = float(input("Weight in pounds: "))
    bmi = (0.453592*weight) / ((0.0254*height)**2)
    print("Your BMI is: ", round(bmi,2))


if system == 2:
    height = float(input("Height in meters: "))
    weight = float(input("Weight in kg: "))
    bmi = weight/(height**2)
    print("Your BMI is: ", round(bmi,2))

if bmi < 15.0:
    print("BMI Category: very severely underweight")

elif bmi <= 16.0 and bmi >= 15.0:
    print("BMI Category: severely underweight")

elif bmi <= 18.4 and bmi >= 16.1:
    print("BMI Category: underweight.")

elif bmi <= 24.9 and bmi >= 18.5:
    print("BMI Category: normal weight.")

elif bmi <= 29.9 and bmi >= 25.0:
    print("BMI Category: overweight.")

elif bmi <= 34.9 and bmi >= 30.0:
    print("BMI Category: moderately obese.")

elif bmi <= 39.9 and bmi >= 35.0:
    print("BMI Category: severely obese.")

elif bmi >= 40.0:
    print("BMI Category: very severely obese")