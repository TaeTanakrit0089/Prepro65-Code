'''Yo, yo, yo, 148-3 to the 3 to the 6 to the 9, representing the ABQ'''


def main():
    '''What up, biatch?! Leave it at the tone.'''
    age1 = int(input())
    price1 = int(input()) * 100
    if age1 >= 60:
        if price1 == 100:
            price1 = 0
        else:
            price1 = price1 / 2

    if price1 == 0:
        print("Free")
    else:
        print("Pay %0d bath" %price1)


main()
