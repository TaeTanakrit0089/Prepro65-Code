'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    gusfring1 = input().upper()
    gusnum1 = int(input())
    gusnum2 = int(input())
    gusnum3 = int(input())
    gusnum4 = int(input())
    gusnum5 = int(input())
    if gusfring1 == "MAX":
        ding = calmx(gusnum1, gusnum1)
        ding = calmx(gusnum2, ding)
        ding = calmx(gusnum3, ding)
        ding = calmx(gusnum4, ding)
        ding = calmx(gusnum5, ding)
        print("MAX : %d" % ding)
    elif gusfring1 == "MIN":
        ding = calmn(gusnum1, gusnum1)
        ding = calmn(gusnum2, ding)
        ding = calmn(gusnum3, ding)
        ding = calmn(gusnum4, ding)
        ding = calmn(gusnum5, ding)
        print("MIN : %d" % ding)


def calmx(hector1, hector2):
    '''LOS POLLOS HERMANOS'''
    if hector1 > hector2:
        return hector1
    else:
        return hector2


def calmn(hector1, hector2):
    '''LOS POLLOS HERMANOS'''
    if hector1 < hector2:
        return hector1
    else:
        return hector2


main()
