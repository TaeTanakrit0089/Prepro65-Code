"""Gustavo Fring"""


def main():
    """Gustavo Fring"""
    print("Name:", input())
    weight = int(input())
    height = float(input())/100

    print("Weight:", weight, "kg.")
    print("Height:", "{:.2f}".format(height), "m.")
    print("BMI:", "{:.2f}".format(weight / (pow(height, 2))))


main()
