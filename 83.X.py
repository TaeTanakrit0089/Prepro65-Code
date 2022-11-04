"""So you think you can stop me and spit in my eye"""


def main(gusfring):
    """So you think you can love me and leave me to die"""
    for i in range(gusfring):
        for j in range(gusfring):
            if (i == j) or (i+j == gusfring - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


main(int(input()))
