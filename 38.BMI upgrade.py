'''Welcome to Los Pollos Hermanos'''


def main():
    '''Welcome to Los Pollos Hermanos'''
    weight1 = float(input())
    height1 = float(input()) / 100
    age1 = int(input())
    bmi1 = weight1 / pow(height1, 2)
    if age1 <= 18:
        print("Please use BMI for Children and Teens.")
    elif bmi1 >= 40:
        print("Obese Class III")
    elif bmi1 >= 35:
        print("Obese Class II")
    elif bmi1 >= 30:
        print("Obese Class I")
    elif bmi1 >= 25:
        print("Overweight")
    elif bmi1 >= 18.5:
        print("Normal")
    elif bmi1 >= 17:
        print("Mild Thinness")
    elif bmi1 >= 16:
        print("Moderate Thinness")
    else:
        print("Severe Thinness")


main()
