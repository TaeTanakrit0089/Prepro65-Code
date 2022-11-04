"""Saul Goodman"""


def my_main():
    """Saul Goodman"""
    gus1 = str(input()).capitalize()
    gus2 = str(input()).capitalize()
    gus3 = str(input()).capitalize()
    fring1 = len(gus1)
    fring2 = len(gus2)
    fring3 = len(gus3)

    if fring1 < fring2 < fring3:
        print(gus1)
        print(gus2)
        print(gus3)
    if fring1 < fring3 < fring2:
        print(gus1)
        print(gus3)
        print(gus2)
    if fring3 < fring2 < fring1:
        print(gus3)
        print(gus2)
        print(gus1)
    if fring3 < fring1 < fring2:
        print(gus3)
        print(gus1)
        print(gus2)
    if fring2 < fring1 < fring3:
        print(gus2)
        print(gus1)
        print(gus3)
    if fring2 < fring3 < fring1:
        print(gus2)
        print(gus3)
        print(gus1)


my_main()
