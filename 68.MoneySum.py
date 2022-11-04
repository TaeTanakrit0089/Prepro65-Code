'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    summer = 0
    for i in range(10):
        gusfring = int(input())
        if gusfring < 0:
            summer += -5
        else:
            summer += gusfring
        i = i
    if summer < 0:
        print(-5)
    else:
        print(summer)


main()
