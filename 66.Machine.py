'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    firstnum = int(input())
    lastnum = int(input())
    if firstnum < lastnum:
        calc(firstnum, lastnum + 1, 1)
    else:
        calc(firstnum, lastnum, -2)


def calc(gus1, gus2, gus3):
    '''LOS POLLOS HERMANOS'''
    summer = 0
    print("Integer Pass : ", end='')
    for i in range(gus1, gus2, gus3):
        if (i % 2) == 1:
            summer += i
            print(i, end=' ')

    print("\nSum Answer :", summer)


main()
