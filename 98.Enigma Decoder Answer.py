"""Never Gonna Give You Up"""


def my_main():
    """Never Gonna Give You Up"""
    input_code = list(input())
    de_code = [input() for x in range(3)]
    char_set = []

    for i in de_code:
        character_number = 0
        for j in i.upper():
            character_number += ord(j) - 65
        char_set.append(character_number % 26)

    def change_number_to_words(var_ch, shi_amount):
        """change_number_to_words"""
        if var_ch.isupper():
            return chr((ord(var_ch) - shi_amount - 65) % 26 + 65).lower()

    getchar = 0
    content = ""
    for i in input_code:
        if i == " ":
            content += " "
            continue
        content += change_number_to_words(i.upper(),
                                          char_set[(getchar // 3) % 3])
        getchar += 1

    print(content.capitalize())


my_main()
