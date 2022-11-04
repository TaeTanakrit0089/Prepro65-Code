"""So you think you can stop me and spit in my eye"""


def main():
    """So you think you can love me and leave me to die"""
    gusfring = int(input())
    mid = (gusfring+1)/2
    for i in range(gusfring):
        for j in range(gusfring):
            if calc(mid, gusfring, i) + calc(mid, gusfring, j) < mid:
                print("*", end='')
            else:
                print(' ', end='')
        print()


def calc(mid, all_num, current_num):
    """Oh, baby, can't do this to me, baby"""
    return abs(current_num-(all_num-mid))


main()
