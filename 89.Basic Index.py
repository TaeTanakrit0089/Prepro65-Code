'''We had a good thing, you stupid son of a bitch. We had Fring.'''


def main():
    '''We had a lab. We had everything we needed and it all ran like clockwork.
    You could've shut your mouth, cooked, and made as much money as you ever needed.'''
    mat = ["" for x in range(100)]
    i = 0
    while i >= 0:
        mat[i] = input()
        if mat[i].lower() == 'end':
            break
        i += 1
    gusfring = int(input())
    if gusfring > i-1:
        print("Index Not Found")
    else:
        print('List[%d] = "%s"' % (gusfring, mat[gusfring]))


main()
