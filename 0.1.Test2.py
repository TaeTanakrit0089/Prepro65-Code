"""Pyramid"""


def main():
    """Pyramid"""
    rows = int(input())
    time = 0

    for row in range(1, rows+1):
        for space in range(1, (rows-row)+1):
            print(end="  ")
        while time != (2*row-1):
            print("* ", end="")
            time += 1
        time = 0
        print()


main()
