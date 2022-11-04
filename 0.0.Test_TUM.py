"""Never Gonna Give You Up"""


def my_main():
    """Never Gonna Give You Up"""
    num_n = int(input())
    taste = str(input()).lower()
    if taste == "m" or taste == "s" or taste == "c"\
            or taste == "b" or taste == "r":
        space = num_n - 1
        diamond = 1
        for i in range(num_n):
            print(' '*space, end='')
            print(taste*diamond, end='')
            space -= 1
            diamond += 2
            print()
            i = i
        space = +1
        diamond -= 4
        for i in range(num_n-1):
            print(' '*space, end='')
            print('_'*diamond, end='')
            space += 1
            diamond -= 2
            print()
            i = i
    else:
        print("Hey!,buy another shop.")

my_main()
