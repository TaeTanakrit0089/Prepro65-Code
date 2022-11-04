"""LOS POLLOS HERMANOS"""


def main():
    """LOS POLLOS HERMANOS"""
    gus1 = int(input())
    gus2 = input().lower()
    if gus2 == "fog":
        print("%.2f" % hectorf(hectorg(gus1)))
    else:
        print("%.2f" % hectorg(hectorf(gus1)))


def hectorf(ding1):
    """LOS POLLOS HERMANOS"""
    return float((15+ding1-pow(ding1, 3)) / ((pow(ding1, 2)/3)+11))


def hectorg(ding1):
    """LOS POLLOS HERMANOS"""
    return float(pow(ding1, 3)+(4*ding1)-1)


main()
