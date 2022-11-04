"""LOS POLLOS HERMANOS"""


def main():
    """LOS POLLOS HERMANOS"""
    gus1 = float(input())
    gus2 = input().upper()
    fromword = gus2[0]
    toword = gus2[2]
    if (fromword == "K"):
        if(toword == "C"):
            print("Celsius : %.2f" % (gus1-273.15))
        elif(toword == "F"):
            print("Fahrenheit : %.2f" % ((gus1*9/5)-459.67))
        elif(toword == "R"):
            print("Rankine  : %.2f" % ((gus1-273.15)*4/5))
    elif (fromword == "F"):
        if(toword == "C"):
            print("Celsius : %.2f" % ((gus1-32)*5/9))
        elif(toword == "K"):
            print("Kelvin : %.2f" % (((gus1+459.67)*5/9)))
        elif(toword == "R"):
            print("Rankine  : %.2f" % ((gus1-273.15)*4/5))

main()
