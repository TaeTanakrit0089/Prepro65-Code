"""LOS POLLOS HERMANOS"""


def my_main():
    """LOS POLLOS HERMANOS"""
    num = int(input())
    if num == 1:
        hector()
    if num > 1:
        hector()
        hectorno(num)


def hector():
    """LOS POLLOS HERMANOS"""
    print("-------------------------")
    print("|                       |")
    print("|                       |")
    print("|                       |")
    print("|   Pre-Progamming 65   |")
    print("|                       |")
    print("|                       |")
    print("|                       |")
    print("-------------------------")


def hectorno(times):
    """LOS POLLOS HERMANOS"""
    times -= 1
    print("|                       |\n\
|                       |\n\
|                       |\n\
|   Pre-Progamming 65   |\n\
|                       |\n\
|                       |\n\
|                       |\n\
-------------------------\n"*times)


my_main()
