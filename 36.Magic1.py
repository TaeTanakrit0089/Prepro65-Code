"""Yo, yo, yo, 148-3 to the 3 to the 6 to the 9, representing the ABQ"""


def my_main():
    """What up, biatch?! Leave it at the tone."""
    gusfring1 = str(input())
    gusfring2 = 12800
    if gusfring1 == "Magician":
        hector1 = input()
        hector2 = int(input())
        if hector1 == "Fairy Tail" and hector2 > 0:
            hector3 = (gusfring2*hector2)*0.80
            print("Total %d Jewel" % hector3)
        elif hector1 == "Sabertooth" and hector2 > 5:
            hector3 = (gusfring2*hector2)*0.85
            print("Total %d Jewel" % hector3)
        elif hector1 == "Lamia Scale" and hector2 >= 3:
            hector3 = (gusfring2*hector2)*0.9
            print("Total %d Jewel" % hector3)
        elif hector1 == "Blue Pegasus" and hector2 > 10:
            hector3 = (gusfring2*hector2)*0.95
            print("Total %d Jewel" % hector3)
        else:
            hector3 = gusfring2*hector2
            print("Total %d Jewel" % hector3)
    else:
        hector2 = int(input())
        hectording = gusfring2*hector2
        print("Total %d Jewel" % hectording)


my_main()
