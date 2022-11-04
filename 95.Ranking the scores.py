'''I see a little silhouetto of a man'''


def main():
    '''Scaramouch, Scaramouch, will you do the Fandango'''
    score_input = [int(i) for i in input().split(",")]
    score_sort = sorted(score_input)
    score_sort.reverse()
    score_output = []
    for i in score_input:
        score_output.append(score_sort.index(i) + 1)
    print(*score_output, sep=",")


main()
