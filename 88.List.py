'''We had a good thing, you stupid son of a bitch. We had Fring.'''


def main(gusfring):
    '''We had a lab. We had everything we needed and it all ran like clockwork.
    You could've shut your mouth, cooked, and made as much money as you ever needed.'''
    mat = ["" for x in range(gusfring)]
    for i in range(gusfring):
        mat[i] = input()
    print('["', end='')
    print(*mat, sep='", "', end='')
    print('"]', end='')


main(int(input()))
