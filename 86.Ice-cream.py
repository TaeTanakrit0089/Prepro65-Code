"""So you think you can stone me and spit in my eye"""


def main():
    """So you think you can love me and leave me to die"""
    gusfring = int(input())
    pollos = input().lower()
    if (pollos == 'm') or (pollos == 's') or (pollos == 'c') or \
            (pollos == 'b') or (pollos == 'r'):
        pyramid(gusfring, pollos)
        print_cone(gusfring, '_')

    else:
        print('Hey!,buy another shop.')


def calc(mid, all_num, current_num):
    """Oh, baby, can't do this to me, baby"""
    return abs(current_num-(all_num-mid))


def print_cone(gusfring, lospollos):
    """Just gotta get out, just gotta get right outta here"""
    middle = gusfring - 1
    space = 1
    star = (2*middle) - 1
    for i in range(middle):
        printlo(' ', space)
        printlo(lospollos, star)
        print()
        space += 1
        star -= 2
        i = i
# ..........From Pyramid


def pyramid(gusfring, lospollos):
    """Oh, Yeah! Oh, Yeah!"""
    space = gusfring - 1
    star = 1
    for i in range(gusfring):
        printlo(' ', space)
        printlo(lospollos, star)
        print()
        space -= 1
        star += 2
        i = i


def printlo(hector1, hector2):
    '''Nothing really matters, Anyone can see'''
    for i in range(hector2):
        print(hector1, end='')
        i = i


main()
