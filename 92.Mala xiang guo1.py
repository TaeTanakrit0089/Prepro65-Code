'''We had a good thing, you stupid son of a bitch. We had Fring.'''

def main():
    '''We had a lab. We had everything we needed and it all ran like clockwork.'''
    i = 0
    temp = ''
    same = 0
    next_process = 0
    spice = 0
    while i >= 0:
        del temp
        temp = input().lower()
        if temp.isnumeric():
            spice = temp
            temp = input().lower()
            if temp != 'stop':
                print('Please choose a spicy level!')
                next_process = 1
                same += check(temp)
                break
            else:
                break
        else:
            same += check(temp)
        i += 1
    spice = int(spice)
    if next_process == 0:
        if same != 0:
            print("Get out!")
        elif i == 0:
            print("Huh? you didn't order anything!")
        else:
            if spice <= 0 or spice >= 5:
                print('Please choose a spicy level!')
            else:
                print(text(spice), "Mala xiang guo is here.")


def check(gusfring):
    '''You could've shut your mouth, cooked, and made as much money as you ever needed.'''
    menu = ['celery stalks', 'carrots', 'potatoes', 'mushrooms', 'tofu', 'lotus root',
            'cabbage', 'instant noodles', 'glass noodle', 'wonton', 'beef', 'pork loin',
            'chicken', 'fish balls', 'cheese ball', 'octopus', 'fish', 'shrimp', 'mussels']
    if gusfring not in menu:
        return 1
    else:
        return 0


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
