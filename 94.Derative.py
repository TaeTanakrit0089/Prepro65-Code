'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    met = input().split(",")
    met_size = len(met)
    for i in range(met_size):
        met[i] = int(met[i]) * i
    del met[0]
    met.append(0)
    print(met)


main()
