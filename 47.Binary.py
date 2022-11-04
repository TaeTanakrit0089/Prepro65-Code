"""Saul Goodman"""


def main(gusfring1):
    """Saul Goodman"""
    gusfring1 = gusfring1[2::]
    gusfring1 = gusfring1.replace("", ", ")[2::]
    gusfring1 = gusfring1.replace("1", "open")
    gusfring1 = gusfring1.replace("0", "close")
    gusfring1 = gusfring1[:-2]
    return gusfring1


print(main(str(bin(int(input())))))
