'''Yo, yo, yo, 148-3 to the 3 to the 6 to the 9, representing the ABQ'''


def main():
    '''What up, biatch?! Leave it at the tone.'''
    hector = ""
    gusfring1 = str(input())
    gusfring2 = str(input())

    if (gusfring2 == "Calm" or gusfring1 == "Calm") and \
        (gusfring2 == "Empathetic" or gusfring1 == "Empathetic"):
        hector = "Ice"
    if (gusfring2 == "Reliable" or gusfring1 == "Reliable") and \
        (gusfring2 == "Courageous" or gusfring1 == "Courageous"):
        hector = "Fern"
    if (gusfring2 == "Optimistic" or gusfring1 == "Optimistic") and \
        (gusfring2 == "Cheerful" or gusfring1 == "Cheerful"):
        hector = "Bam"
    if (gusfring2 == "Attractive" or gusfring1 == "Attractive") and \
        (gusfring2 == "Creative" or gusfring1 == "Creative"):
        hector = "Tangmo"
    if (gusfring2 == "Cheerful" or gusfring1 == "Cheerful") and \
        (gusfring2 == "Creative" or gusfring1 == "Creative"):
        hector = "Mild"
    if (gusfring2 == "Reliable" or gusfring1 == "Reliable") and \
        (gusfring2 == "Optimistic" or gusfring1 == "Optimistic"):
        hector = "Prae"
    if (gusfring2 == "Courageous" or gusfring1 == "Courageous") and \
        (gusfring2 == "Calm" or gusfring1 == "Calm"):
        hector = "Dream"
    if (gusfring2 == "Empathetic" or gusfring1 == "Empathetic") and \
        (gusfring2 == "Attractive" or gusfring1 == "Attractive"):
        hector = "Aom"
    print(hector)


main()
