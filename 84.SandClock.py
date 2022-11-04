"""So you think you can stop me and spit in my eye"""


def main():
    """So you think you can love me and leave me to die"""
    gusfring = int(input())
    gusfring = (gusfring * 2) + 1
    mid = (gusfring+1)/2
    print("*"*gusfring)
    for i in range(gusfring):
        for j in range(gusfring):
            if calc(mid, gusfring, i) == calc(mid, gusfring, j):
                print("*", end='')
            else:
                print(' ', end='')
        print()
    print("*"*gusfring)


def calc(mid, all_num, current_num):
    """Oh, baby, can't do this to me, baby"""
    return abs(current_num-(all_num-mid))


main()
