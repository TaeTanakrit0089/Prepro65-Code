'''Saul Goodman'''


def main(gusfring):
    '''Saul Goodman'''
    text_input, text_sort_age, text_sort_occu = [], [], []
    for i in range(gusfring):
        text_input.append(input())
        text_input[i] = text_input[i].split(" ")
        text_sort_age.append(int(text_input[i][0]))
        text_sort_occu.append(text_input[i][2])
        text_input[i][0] = int(text_input[i][0])

    text_input.sort(key=lambda row: row[1])
    text_sort_age.sort()
    text_sort_occu.sort()
    text_sort_occu = list(dict.fromkeys(text_sort_occu))

    for i in text_sort_occu:
        numbering = 1
        print("OCCUPATION :", i.upper())
        for j in range(len(text_input)):
            if i == text_input[j][2]:
                print("%d. %s, %d" %
                      (numbering, text_input[j][1], text_input[j][0]))
                numbering += 1


main(int(input()))
