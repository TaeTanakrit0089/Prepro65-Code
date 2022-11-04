'''LOS POLLOS HERMANOS'''


def main():
    '''LOS POLLOS HERMANOS'''
    text1 = []
    for i in range(int(input())):
        text1.insert(i, input())
        if text1[i] == text1[i][::-1]:
            print(text1[i])


main()
