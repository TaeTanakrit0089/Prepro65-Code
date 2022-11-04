"""LOS POLLOS HERMANOS"""


def main():
    """LOS POLLOS HERMANOS"""
    text = input()
    i = 0
    while i == 0:
        change = str(input())
        text_before = text
        for j in range(len(text)):
            text = text.replace(change, '')
            j = j
        if text_before == text:
            print(text)
            break


main()
