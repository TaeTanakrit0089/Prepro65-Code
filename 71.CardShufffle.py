'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    tuco1 = 'A'
    tuco2 = 'B'
    tuco3 = 'C'
    for i in range(int(input())):
        ptemp = ''
        gusfring1 = input()
        if (gusfring1 == "12") or (gusfring1 == "21"):
            ptemp = tuco1
            tuco1 = tuco2
            tuco2 = ptemp
        elif (gusfring1 == "13") or (gusfring1 == "31"):
            ptemp = tuco1
            tuco1 = tuco3
            tuco3 = ptemp
        elif (gusfring1 == "23") or (gusfring1 == "32"):
            ptemp = tuco2
            tuco2 = tuco3
            tuco3 = ptemp
        i = i

    print(tuco1, tuco2, tuco3, sep="\n")


main()
