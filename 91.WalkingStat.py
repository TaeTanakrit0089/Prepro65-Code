'''We had a good thing, you stupid son of a bitch. We had Fring.'''
import math


def main(gusfring):
    '''We had a lab. We had everything we needed and it all ran like clockwork.
    You could've shut your mouth, cooked, and made as much money as you ever needed.'''
    mat = []
    avg = 0
    for i in range(gusfring):
        mat.append(float(input()))
        avg += mat[i]
    avg = avg / gusfring
    for i in range(gusfring):
        print(math.ceil(abs(mat[i] - avg)))


main(int(input()))
