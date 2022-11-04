"""LOS POLLOS HERMANOS"""


def main():
    """LOS POLLOS HERMANOS"""
    first = int(input())
    last = int(input())
    for i in range(1, first+1):
        for j in range(1, last+1):
            print("(%d, %d)" % (i, j), end=' ')
        print("")


main()
