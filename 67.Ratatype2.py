'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    firsttext = input()
    gusfring1 = 0
    if "6" in firsttext:
        gusfring1 += firsttext.count("6")
    if "Y" in firsttext:
        gusfring1 += firsttext.count("Y")
    if "H" in firsttext:
        gusfring1 += firsttext.count("H")
    if "N" in firsttext:
        gusfring1 += firsttext.count("N")
    if "7" in firsttext:
        gusfring1 += firsttext.count("7")
    if "U" in firsttext:
        gusfring1 += firsttext.count("U")
    if "J" in firsttext:
        gusfring1 += firsttext.count("J")
    if "M" in firsttext:
        gusfring1 += firsttext.count("M")
    print(gusfring1)


main()
