'''We had a good thing, you stupid son of a bitch. We had Fring.'''


def main():
    '''We had a lab. We had everything we needed and it all ran like clockwork.'''
    menu = ['celery stalks', 'carrots', 'potatoes', 'mushrooms', 'tofu', 'lotus root',
            'cabbage', 'instant noodles', 'glass noodle', 'wonton', 'beef', 'pork loin',
            'chicken', 'fish balls', 'cheese ball', 'octopus', 'fish', 'shrimp', 'mussels']
    i, spice_level = 0, 0
    con = True
    gusfring = []
    while i >= 0:
        temp = input().lower()
        if temp == 'stop' or temp == '':
            gusfring.append(temp)
            break
        elif temp.isnumeric():
            gusfring.append(temp)
            spice_level = int(temp)
        else:
            gusfring.append(temp)

    for i in range(len(gusfring)):
        #
        if ((gusfring[i] not in menu and gusfring[i] != 'stop') and gusfring[i].isalpha()
            ) or not(spice_level >= 1 and spice_level <= 4):
            print("Get out!")
            con = False
            break
        elif len(gusfring) == 1 or (gusfring[i] not in menu and len(gusfring) == 2):
            print("Huh? you didn't order anything!")
            con = False
            break
        elif spice_level == 0 or gusfring[len(gusfring)-2].isalpha() or check_dup(gusfring):
            print("Please choose a spicy level!")
            con = False
            break
    if con == False:
        quit()
    print(text(spice_level), "Mala xiang guo is here.")


def check_dup(gusfring):
    all_num = 0
    for i in range(len(gusfring)):
        if gusfring[i].isnumeric():
            all_num += 1
    if all_num != 1:
        return True
    else:
        return False


def text(lospollos):
    '''Gusfring'''
    if lospollos == 1:
        return "Mild"
    elif lospollos == 2:
        return "Medium"
    elif lospollos == 3:
        return "Hot"
    elif lospollos == 4:
        return "Extra hot"


main()
