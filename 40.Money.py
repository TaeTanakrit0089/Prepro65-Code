'''Hello! And welcome to the Los Pollos Hermanos family.'''


def main():
    '''My name is Gustavo, but you can call me "Gus". I am thrill that you'll be joining our team'''
    guspaid = float(input())
    gusprice = float(input())
    if guspaid == gusprice:
        print("จ่ายมาพอดี")
    elif guspaid < gusprice:
        print("จำนวนเงินไม่พอ")
    else:
        salamanca(guspaid - gusprice)


def lalo1(num1, num2):
    '''Each and every day, we serve our customers exceptional food, with impecable service.'''
    sum1 = num1 // num2
    num1 = num1 % num2
    if num2 > 12:
        print("เเบงค์ %d บาท : %d" % (num2, sum1))
    elif num2 < 1:
        print("เหรียญ %d สตางค์ : %d" % (num2*100, sum1))
    else:
        print("เหรียญ %d บาท : %d" % (num2, sum1))
    return num1


def salamanca(tuco1):
    '''We take pride in everything that we do. And after this week's online seminar'''
    tuco1 = lalo1(tuco1, 500)
    tuco1 = lalo1(tuco1, 100)
    tuco1 = lalo1(tuco1, 50)
    tuco1 = lalo1(tuco1, 20)
    tuco1 = lalo1(tuco1, 12)
    tuco1 = lalo1(tuco1, 10)
    tuco1 = lalo1(tuco1, 5)
    tuco1 = lalo1(tuco1, 2)
    tuco1 = lalo1(tuco1, 1)
    tuco1 = lalo1(tuco1, 0.5)
    tuco1 = lalo1(tuco1, 0.25)
    return tuco1


main()
