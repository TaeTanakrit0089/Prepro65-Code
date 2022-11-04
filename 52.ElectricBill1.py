"""Welcome To Los Pollos Hermanos"""


def main():
    """Welcome To Los Pollos Hermanos"""
    print("	")
    hector("TV", int(input()), 3, 1)
    hector("Microwave", int(input()), 1, 1)
    hector("Hair dryer", int(input()), 0.5, 1)
    hector("light bulb", int(input()), 5, 4)
    hector("Refrigerator", int(input()), 24, 1)


def hector(salamanca, ding1, ding2, ding3):
    '''WHERE THE HELL IS SchRadEr
    salamanca = NAME
    ding1 = Watt
    ding2 = Hours
    ding3 = ea '''
    boom = float((ding1*ding2/1000) * ding3) * 30
    print(salamanca + " %d Watt %d ea for %d hours\n%.2f unit." %
          (ding1, ding3, ding2, boom))


main()
