"""I see a little silhouetto of a man"""


def main():
    """Scaramouch, Scaramouch, will you do the Fandango"""
    f1 = 9223372036854775807
    f2 = 9223372036854775807
    f3 = 9223372036854775807
    summer = 1
    for i in range(10):
        fin = int(input())
        if fin == f3:
            summer += 1
        if fin < f1:
            f1 = fin
        if (f2 >= f3) and (f3 <= fin) and (f3 != f1):
            f2 = f3
        f3 = fin
        i = i
    if (summer == 10) or (summer == 0):
        print("Almost the min :", f3)
    else:
        print("Almost the min :", f2)


main()
