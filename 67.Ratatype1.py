'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    gusfring1 = input().lower()
    summer = 0
    summer += check("6", gusfring1)
    summer += check("y", gusfring1)
    summer += check("h", gusfring1)
    summer += check("n", gusfring1)
    summer += check("7", gusfring1)
    summer += check("u", gusfring1)
    summer += check("j", gusfring1)
    summer += check("m", gusfring1)
    print(summer)


def check(hector1, hector2):
    '''LOS POLLOS HERMANOS'''
    if hector1 in hector2:
        return hector2.count(hector1)
    else:
        return 0


main()
