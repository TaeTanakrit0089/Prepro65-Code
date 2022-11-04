'''I see a little silhouetto of a man'''


def main():
    '''Scaramouch, Scaramouch, will you do the Fandango'''
    i_loop, error_input = 0, 0
    input_all = []
    summer = 0
    has_soft, has_fruit, has_cup, has_ice = False, False, False, False
    cup = [['cup', 5], ['ice', 5]]
    fruit = [['orange', 17], ['banana', 13], ['strawberry', 10],
             ['cherrie', 15], ['watermelon', 12], ['lemon', 19], ['mango', 21],
             ['grape', 11]]
    softdrink = [['coke', 15], ['pepsi', 15], ['sprite', 15], ['fanta', 15]]
    while i_loop >= 0:
        con = True
        temp = input().lower()
        input_all.append(temp)
        if temp == 'end':
            if error_input >= 1 or has_cup == False or has_ice == False\
                    or input_all[len(input_all)-2] != 'ice' or input_all[0] != 'cup'\
                    or (has_fruit == False and has_soft == False) \
                    or count_iceandcup(input_all):
                print("Invalid order!")
                break
            elif has_soft == True and has_fruit == True:
                print("Here's your soft drink!")
            elif has_soft == False and has_fruit == True:
                print("Here's your juice!")
            else:
                print("Invalid order!")
            print("Cost %d baht." % int(summer))
            break
        for i in range(len(cup)):
            if temp in cup[i]:
                if temp == cup[0][0]:
                    has_cup = True
                elif temp == cup[1][0]:
                    has_ice = True
                summer += int(cup[i][1])
                con = False
                break
        for i in range(len(fruit)):
            if temp in fruit[i]:
                summer += int(fruit[i][1])
                con = False
                has_fruit = True
                break
        for i in range(len(softdrink)):
            if temp in softdrink[i]:
                summer += int(softdrink[i][1])
                con = False
                has_soft = True
                break
        del temp
        if con == False:
            continue
        error_input += 1
        
def count_iceandcup(gusfring):
    '''Thunderbolts and lightning, very, very frightening me'''
    cup_amount = 0
    ice_amount = 0
    for i in range(len(gusfring)):
        if gusfring[i] == 'cup':
            cup_amount += 1
        elif gusfring[i] == 'ice':
            ice_amount += 1
    if cup_amount != 1 or ice_amount != 1:
        return True
    else:
        return False


main()
