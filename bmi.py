def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Underweight Weight")
    elif bmi < 25:
        print("Normal Weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")
calculate_bmi(weight=57, height=1.73)