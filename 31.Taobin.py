'''I have a good job until my boss accusing me of stealing. OH! Let better call saul'''


def main():
    '''I was in a party and i have my own business, You're under arreseted. LET BETTER CALL SAUL!'''
    num1 = float(input())
    num2 = float(input())
    num3 = abs(num1-num2)
    print("%d" % max1(num3))
    print("%d" % min1(num3))
    print("%.01f" % num3)


def max1(default1):
    '''Saul Goodman'''
    sum1 = 0
    sum1 += find1(default1, 0.25)
    default1 = default1 % 0.25
    sum1 += find1(default1, 0.5)
    default1 = default1 % 0.5
    sum1 += find1(default1, 1)
    default1 = default1 % 1
    sum1 += find1(default1, 2)
    default1 = default1 % 2
    sum1 += find1(default1, 5)
    default1 = default1 % 5
    sum1 += find1(default1, 10)
    default1 = default1 % 10
    return sum1


def find1(num1, num2):
    '''Saul Goodman'''
    num1 = num1 // num2
    sum1 = num1
    return sum1


def min1(default1):
    '''Saul Goodman'''
    sum1 = 0
    sum1 += find1(default1, 10)
    default1 = default1 % 10
    sum1 += find1(default1, 5)
    default1 = default1 % 5
    sum1 += find1(default1, 2)
    default1 = default1 % 2
    sum1 += find1(default1, 1)
    default1 = default1 % 1
    sum1 += find1(default1, 0.5)
    default1 = default1 % 0.5
    sum1 += find1(default1, 0.25)
    default1 = default1 % 0.25
    return sum1


main()
