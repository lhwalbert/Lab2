def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**2)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("You are Under Weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("You are Normal Weight")
        return 0
    else:
        print("You are Overweight Weight")
        return 1
        