'''Yo, yo, yo, 148-3 to the 3 to the 6 to the 9, representing the ABQ'''


def main():
    '''What up, biatch?! Leave it at the tone.'''
    gusfring1 = input()
    hector1 = int(gusfring1[0])
    hector2 = int(gusfring1[1])
    if(hector1 == 3 and hector2 == 1) or (hector1 == 1 and hector2 == 3):
        print("B")
    elif hector1 == hector2:
        print("B")
    elif hector1 == 2:
        print(check(hector2))
    else:
        print(check(hector1))


def check(mike1):
    '''Ding Ding'''
    if mike1 == 1:
        mike2 = "A"
    if mike1 == 2:
        mike2 = "B"
    if mike1 == 3:
        mike2 = "C"
    return mike2


main()
