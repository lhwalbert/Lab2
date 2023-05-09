def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**2)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("You are Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("You are Normal Weight")
    else:
        print("You are Overweight Weight")