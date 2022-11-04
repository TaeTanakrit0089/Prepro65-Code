"""Welcome To Los Pollos Hermanos"""


def main():
    """Welcome To Los Pollos Hermanos"""
    gusfring = [replace(input()), replace(input()), replace(input()), replace(input()),
                replace(input())]
    print(gusfring[0])
    print(gusfring[1])
    print(gusfring[2])
    print(gusfring[3])
    print(gusfring[4])


def replace(hector1):
    '''Ding'''
    if hector1 == '1':
        return " ^----^"
    elif hector1 == '2':
        return "( 0--0 )"
    elif hector1 == '3':
        return "<------>"
    elif hector1 == '4':
        return "(------)"
    elif hector1 == '5':
        return " u----u"


main()
