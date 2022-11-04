'''Saul Goodman'''


def main():
    'Saul'
    saul = int(input())
    return saul


def remove(s, indx):
    return ''.join(filter(lambda y: s.index(y) != 1, s))


x = main()
remove(x, 0)
remove(x, 2)
remove(x, 4)
remove(x, 6)
remove(x, 8)
print(x)
