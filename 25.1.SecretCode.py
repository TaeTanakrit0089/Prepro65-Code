'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    saul = int(input())
    saul2 = (saul // pow(10, 8)) % 10
    saul4 = (saul // pow(10, 6)) % 10
    saul6 = (saul // pow(10, 4)) % 10
    saul8 = (saul // pow(10, 2)) % 10
    saul10 = (saul // pow(10, 0)) % 10
    print('%d%d%d%d%d'%(saul2, saul4, saul6, saul8, saul10))


main()
