'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    gusa1 = float(input())
    gusn1 = int(input())
    gusr1 = float(input())
    for gusn1 in range(1, gusn1+1):
        print("%.2f" % (gusa1*pow(gusr1, gusn1-1)), end=" ")


main()
