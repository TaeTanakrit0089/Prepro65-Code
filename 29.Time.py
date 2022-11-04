'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    num1 = int(input())  # sec
    
    second1 = int(num1 % 60)
    num1 = num1//60  # min
    
    min1 = int(num1 % 60)
    num1 = num1//60  # hours
    
    hours1 = int(num1 % 24)
    day1 = num1//24  # days
    
    print("%02d:%02d:%02d:%02d" % (day1, hours1, min1, second1))


main()
