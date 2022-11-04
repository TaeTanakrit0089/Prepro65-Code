"""Mamaaa, Just killed a man,"""


def main(gusfring):
    """Put a gun against his head, pulled my trigger, Now he's dead"""
    spice_level = 'none'
    error_output = False
    correct_output = False
    if gusfring == "stop" or gusfring == "":
        print("Huh? you didn't order anything!")

    while gusfring != 'stop':
        output = check(gusfring)

        if output == 'wrong':
            error_output = True

        elif output == 'spiceLevel':
            spice_level = get_spicy(gusfring)
        else:
            correct_output = True
            spice_level = 'none'

        gusfring = str(input()).lower()
        if gusfring == 'stop':
            break

    if error_output:
        print("Get out!")
    elif spice_level != 'none' and correct_output:
        print("%s Mala xiang guo is here." % spice_level)
    elif spice_level != 'none' and not correct_output:
        print("Huh? you didn't order anything!")
    elif spice_level == 'none' and correct_output:
        print("Please choose a spicy level!")


def check(gusfring):
    """Mamaaa, life had just begun,"""
    menu = ['celery stalks', 'carrots', 'potatoes', 'mushrooms', 'tofu', 'lotus root',
            'cabbage', 'instant noodles', 'glass noodle', 'wonton', 'beef', 'pork loin',
            'chicken', 'fish balls', 'cheese ball', 'octopus', 'fish', 'shrimp', 'mussels']
    if gusfring in menu:
        return 'correct'
    elif gusfring == '1' or gusfring == '2' or gusfring == '3' or gusfring == '4':
        return 'spiceLevel'
    elif gusfring == 'stop':
        return 'stop'
    else:
        return 'wrong'


def get_spicy(spice_level):
    """But now I've gone and thrown it all away"""
    if spice_level == '1':
        return "Mild"
    if spice_level == '2':
        return "Medium"
    if spice_level == '3':
        return "Hot"
    if spice_level == '4':
        return "Extra hot"


main(input().lower())
