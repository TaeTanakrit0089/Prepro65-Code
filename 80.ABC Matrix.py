"""So you think you can stop me and spit in my eye"""


def main():
    """So you think you can love me and leave me to die"""
    gusfring = ord(input().upper()) - 64
    gus_h, gus_w = gusfring + 1, gusfring + 1
    mat = [[-1 for x in range(gus_w)] for y in range(gus_h)]

    for i in range(gusfring):
        temp = i - 1
        for j in range(gusfring):
            if temp >= (j - 1):
                mat[i][j] = j

    for i in range(gusfring):
        for j in range(gusfring):
            if mat[i][j] >= 0:
                print(chr(int(mat[i][j]+65)), end=' ')

        print()


main()
