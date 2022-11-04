'''I see a little silhouetto of a man'''


def main():
    '''Scaramouch, Scaramouch, will you do the Fandango'''
    has_soda = False
    summer = 0
    i = 0
    mat = []
    while i >= 0:
        temp = input().lower()
        if temp == 'end':
            i = -1
        mat.append(temp)
    # Check or mat.count('ice') != 1
    if mat[0] != 'cup' or mat[-2] != 'ice' or mat.count('cup') != 1\
            or len(mat) <= 3:
        print("Invalid order!")
        quit()
    for i in range(len(mat)):
        has_soda = check_juice(mat[i], has_soda)
        if check_error(mat[i]):
            print("Invalid order!")
            quit()
        summer += check(mat[i])
    if has_soda == True:
        print("Here's your soft drink!")
    else:
        print("Here's your juice!")
    print("Cost %d baht." % summer)


def check(gusfring):
    '''Thunderbolts and lightning, very, very frightening me'''
    cuttery = [['cup', 5], ['ice', 5]]
    juice = [['orange', 17], ['banana', 13], ['strawberry', 10],
             ['cherrie', 15], ['watermelon', 12], ['lemon', 19], ['mango', 21],
             ['grape', 11]]
    soda = [['coke', 15], ['pepsi', 15], ['sprite', 15], ['fanta', 15]]
    for i in range(len(cuttery)):
        if gusfring in cuttery[i]:
            return int(cuttery[i][1])
    for i in range(len(juice)):
        if gusfring in juice[i]:
            return int(juice[i][1])
    for i in range(len(soda)):
        if gusfring in soda[i]:
            return int(soda[i][1])
    return 0


def check_error(gusfring):
    '''Galileo, Figaro - magnificoo'''
    cuttery = [['cup', 5], ['ice', 5]]
    juice = [['orange', 17], ['banana', 13], ['strawberry', 10],
             ['cherrie', 15], ['watermelon', 12], ['lemon', 19], ['mango', 21],
             ['grape', 11]]
    soda = [['coke', 15], ['pepsi', 15], ['sprite', 15], ['fanta', 15]]
    if gusfring == 'end' or gusfring == 'cup' or gusfring == 'ice':
        return False
    for i in range(len(cuttery)):
        if gusfring in cuttery[i]:
            return False
    for i in range(len(juice)):
        if gusfring in juice[i]:
            return False
    for i in range(len(soda)):
        if gusfring in soda[i]:
            return False
    return True


def check_juice(gusfring, hector):
    '''magnificooooooooooooooo'''
    soda = [['coke', 15], ['pepsi', 15], ['sprite', 15], ['fanta', 15]]
    for i in range(len(soda)):
        if gusfring in soda[i]:
            return True
    return hector


main()
