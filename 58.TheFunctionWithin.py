'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    gusa = float(input())
    gusb = float(input())
    gusc = float(input())
    gusd = float(input())

    print(
        funone(funone(gusa)))
    print(
        funtwo(funone(gusa-gusb)))
    print(
        funthree(funone(gusa+gusb), funone(gusa+gusc), funtwo(funone(pow(gusd, 2)))))
    print(
        funfour(funthree(funone(gusa+gusb), funone(gusa-gusc), funtwo(funone(pow(gusd, 2)))),
                funtwo(funone(gusa-gusb)),
                funone(funone(funone(funone(funone(gusc))))),
                pow(gusd, 8)))


def funone(hectorx):
    '''LOS POLLOS HERMANOS'''
    summer = hectorx * 2
    return summer


def funtwo(hectorx):
    '''LOS POLLOS HERMANOS'''
    summer = (pow(hectorx, 4)*3) - pow(hectorx, 3) + (pow(hectorx, 2)*2) + 10
    return summer


def funthree(hectorx, hectory, hectorz):
    '''LOS POLLOS HERMANOS'''
    summer = pow(hectorz + hectorx, 2) - (hectorx*hectory) + pow(hectory, 2)
    return summer


def funfour(hectora, hectorb, hectorc, hectord):
    '''LOS POLLOS HERMANOS'''
    summer = (pow(hectora, 2) + pow(hectorb, 2) - pow(hectorc, 2)) / \
        (pow(hectord, 2) - (2*hectora*hectord)+(2*hectora))
    return summer


main()
