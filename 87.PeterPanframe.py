"""So you think you can stone me and spit in my eye"""


def main():
    """So you think you can love me and leave me to die"""
    gusfring = input()
    gus_length = len(gusfring)
    row1(gus_length)
    row2(gus_length)
    row3(gusfring, gus_length)
    row2(gus_length)
    row1(gus_length)


def row1(holly):
    """Oh, baby, can't do this to me, baby"""
    for i in range(holly):
        temp = i % 3 + 1
        if (temp == 1) or (temp == 2):
            print("..♦.", end='')
        elif temp == 3:
            print("..◊.", end='')
    print(".")


def row2(holly):
    """Just gotta get out, just gotta get right outta here"""
    print(".", end='')
    for i in range(holly):
        temp = i % 3 + 1
        if (temp == 1) or (temp == 2):
            print("♦.♦.", end='')
        elif temp == 3:
            print("◊.◊.", end='')
    print()


def row3(skyler, holly):
    """Oh Yeah Oh yeah"""
    print("♦.%s.♦" % skyler[0], end='')
    for i in range(1, holly):
        temp = i % 3 + 1
        if (temp == 2) or (temp == 3):
            print(".%s.◊" % skyler[i], end='')
        elif temp == 1:
            print(".%s.♦" % skyler[i], end='')
    print()


main()
