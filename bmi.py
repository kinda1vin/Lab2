def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Underweight Weight")
        return -1
    elif bmi < 25:
        print("Normal Weight")
        return 0
    else :
        print("Overweight")
        return 1

returnValu = calculate_bmi(weight=57, height=1.73)
print(returnValu)