"""Saul Goodman"""


def my_main():
    """Saul Goodman"""
    fish = str(input())
    human = int(input())
    num = fish.count("<^))))><")
    if num == 0:
        print("No one will eat them  because we cannot be divided the fish.")
    elif num < human:
        if (num*2) % human == 0:
            print("We can share the fish together Yahoooo!!!")
        else:
            print("No one will eat them  because we cannot be divided the fish.")
    elif num > human:
        print("We have many fish ahoyy!!!")
    else:
        print("We have enough fish for everyone.")


my_main()
