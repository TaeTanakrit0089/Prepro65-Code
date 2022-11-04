"""LOS POLLOS HERMANOS"""


def main():
    """LOS POLLOS HERMANOS"""
    gus_w, gus_h = 6, 11
    mat = [[0 for x in range(gus_w)] for y in range(gus_h)]
    money = float(input())
    done = 0
    for i in range(1, 11):
        if done == 1:
            break
        for j in range(1, 6):
            if done == 1:
                break
            mat[i][j] = float(input())
            if mat[i][j] < money:
                done = 1
                print("%.2f" % mat[i][j])
                print(i)
                break
    # sort mat
    if done == 0:
        final_min = [9999, 0]
        for i in range(gus_h):
            mat[i].sort()
            if (mat[i][1] <= final_min[0]) and (mat[i][1] != 0):
                final_min[0] = mat[i][1]
                final_min[1] = i
        print("%.2f" % final_min[0])
        print("%d" % final_min[1])


main()
