'''Yo, yo, yo, 148-3 to the 3 to the 6 to the 9, representing the ABQ'''


def main():
    '''What up, biatch?! Leave it at the tone.'''
    weather = input()
    status = input()
    distance = float(input())
    if distance < 0:
        print("Error")
    elif weather == "rainy" and status == "important":
        gusfring(distance)
    elif weather == "sunny" and status == "important":
        gusfring(distance)
    elif weather == "rainy" and status == "not important":
        print("Not go")
    elif weather == "sunny" and status == "not important":
        gusfring(distance)


def gusfring(num1):
    '''ddd'''
    if num1 < 1:
        print("Walk")
    elif num1 < 20:
        print("Motorcycle")
    elif num1 < 300:
        print("Car")
    else:
        print("Private jet")


main()
