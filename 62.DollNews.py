"""I see a little silhouetto of a man"""


def main(gusfring1, gusfring2, allow):
    """Scaramouch, Scaramouch, will you do the Fandango"""
    if allow == 0:
        return 0
    if gusfring2 == "stop":
        allow = 0
        print(gusfring1)
        return 0
    elif gusfring2 == "north":
        gusfring1 = north(gusfring1)
    elif gusfring2 == "east":
        gusfring1 = east(gusfring1)
    elif gusfring2 == "west":
        gusfring1 = west(gusfring1)
    elif gusfring2 == "south":
        gusfring1 = south(gusfring1)
    # .................................
    gusfring2 = input().lower()
    main(gusfring1, gusfring2, allow)


def north(ding):
    """Galileo, Figaro - magnificoo"""
    if (ding == 1) or (ding == 2):
        return ding
    else:
        if ding == 3:
            return 1
        elif ding == 4:
            return 2


def east(ding):
    """I'm just a poor boy nobody loves me"""
    if (ding == 2) or (ding == 4):
        return ding
    else:
        if ding == 1:
            return 2
        elif ding == 3:
            return 4


def west(ding):
    """He's just a poor boy from a poor family"""
    if (ding == 1) or (ding == 3):
        return ding
    else:
        if ding == 2:
            return 1
        elif ding == 4:
            return 3


def south(ding):
    """Spare him his life from this monstrosity"""
    if (ding == 3) or (ding == 4):
        return ding
    else:
        if ding == 1:
            return 3
        elif ding == 2:
            return 4


main(int(input()), input().lower(), 1)
