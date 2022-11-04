'''We had a good thing, you stupid son of a bitch. We had Fring.'''


def main(gusfring):
    '''We had a lab. We had everything we needed and it all ran like clockwork.'''
    mat = []
    occu = []
    done = []
    num_done = 0
    for i in range(gusfring):
        mat.append(input())
        mat[i] = mat[i].split(" ")
        mat[i][0] = int(mat[i][0])
        occu.append(mat[i][2])
    for i in range(10):
        mat.sort(key=lambda x: x[1])
        occu.sort()
    # occupation
    occu = list(dict.fromkeys(occu))
    occu_len = len(occu) + 1
    temp = 0
    while num_done != occu_len:
        if num_done >= gusfring:
            break
        no_list = 1
        print("OCCUPATION :", occu[temp].upper())
        for i in range(len(mat)):
            if occu[temp] == mat[i][2]:
                print("%d. %s, %d" % (no_list, mat[i][1], mat[i][0]))
                num_done += 1
                no_list += 1
                done.append(occu[temp])
        done = list(dict.fromkeys(done))

        # remove word that already print
        for i in range(len(mat)):
            if i >= len(mat):
                break
            elif occu[temp] == mat[i][2]:
                del mat[i]
        temp += 1

main(int(input()))
