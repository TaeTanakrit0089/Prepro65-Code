"""Saul Goodman"""


def my_main():
    """Saul Goodman"""
    gussex = input().casefold()
    num1 = input()
    name = input().capitalize()
    bigsur = input().capitalize()
    age = int(input())
    career = input().upper()

    print("======")
    print("ID :", num1[0:6])
    print("Name : "+"Mrs."*(gussex == "female") +
          "Mr."*(gussex == "male"), name, bigsur)
    print("Age : " + str(age) + " years old")
    print("Occupation :", career)
    print("======")


my_main()
