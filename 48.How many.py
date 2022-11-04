"""Saul Goodman"""


def main():
    """Saul Goodman"""
    gusfring1 = input()
    gusfring2 = input()
    gusfind(gusfring1, gusfring2)


def gusfind(hector1, hector2):
    """Saul Goodman"""
    gussum = 0
    hector1 = hector1.lower()
    hector2 = hector2.lower()
    gussum += hector1.count(hector2)
    #hector1 = hector1.upper()
    #hector2 = hector2.upper()
    #gussum += hector1.count(hector2)
    if gussum == 0:
        print("No word and character.")
    elif len(hector2) == 1:
        print("Character : %d" % gussum)
    elif len(hector2) > 1:
        print("Word : %d" % gussum)
    return 0


main()
