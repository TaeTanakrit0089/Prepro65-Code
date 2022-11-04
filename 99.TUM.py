"""Basic Index"""


def main():
    """index"""
    thelist = []
    while True:
        item = input()
        if item.lower() == "end":
            finde = int(input())
            print('List[%d] = "' % finde + str(thelist[finde])+'"')
            break
        thelist.append(item)


main()
