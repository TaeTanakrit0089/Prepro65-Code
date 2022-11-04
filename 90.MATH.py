'''We had a good thing, you stupid son of a bitch. We had Fring.'''


def main():
    '''We had a lab. We had everything we needed and it all ran like clockwork.
    You could've shut your mouth, cooked, and made as much money as you ever needed.'''
    met = []
    gusfring = int(input())
    for i in range(gusfring):
        met.append(float(input()))
    multiply = float(input())
    for i in range(len(met)):
        met[i] = ('%.2f' % (met[i] * multiply))
    print(met)


main()
