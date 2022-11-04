'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    num1 = float(input())
    text1 = input()

    summary1 = (((pow(num1+4, 1/4))+(num1/4))/((4*num1)-4))*44
    num2 = int(num1 // 44)
    print(text1*num2)
    print("%.4f" % summary1)


main()
