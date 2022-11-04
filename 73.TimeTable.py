"""LOS POLLOS HERMANOS"""


def main():
    """LOS POLLOS HERMANOS"""
    first = int(input())
    last = int(input())
    for i in range(2, first+1):
        print("-----")
        for j in range(1, last+1):
            print(i, "x", j, "=", i*j)
    print("-----")


main()
