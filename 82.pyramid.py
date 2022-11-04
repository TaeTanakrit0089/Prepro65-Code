"""So you think you can stop me and spit in my eye"""


def main():
    """So you think you can love me and leave me to die"""
    gusfring = int(input())
    space = gusfring - 1
    star = 1
    for i in range(gusfring):
        printlo(' ', space)
        printlo('*', star)
        print()
        space -= 1
        star += 2
        i = i


def printlo(hector1, hector2):
    """Oh, baby, can't do this to me, baby"""
    for i in range(hector2):
        print(hector1, end=' ')
        i = i


main()
