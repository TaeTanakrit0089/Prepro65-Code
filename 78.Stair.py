"""So you think you can stop me and spit in my eye"""


def main():
    """So you think you can love me and leave me to die"""
    gusfring = int(input())
    gus_w, gus_h = gusfring, gusfring
    mat = [[' ' for x in range(gus_w)] for y in range(gus_h)]
    temp = 0
    for i in range(gusfring):
        temp = i - 1
        for j in range(gusfring):
            if temp <= (j - 1):
                mat[i][j] = '*'

    for i in range(gusfring):
        for j in range(gusfring):
            print(mat[i][j], end=' ')
        print()


main()
