"""So you think you can stop me and spit in my eye"""


def main():
    """So you think you can love me and leave me to die"""
    gus_h, gus_w = int(input()), int(input())
    mat = [[0 for x in range(gus_w)] for y in range(gus_h)]

    for i in range(gus_h):
        for j in range(gus_w):
            mat[i][j] = (j+1) * (i+1)
            print(mat[i][j], end=' ')
        print("")


main()
