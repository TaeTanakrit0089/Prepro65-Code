'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    encrypted = input()
    decrypted = [input().upper() for i in range(3)]
    ans = []

    for i in decrypted:
        char_num = 0
        for j in i.upper():
            char_num += ord(j) - 65
        ans.append(char_num % 26)

    final_temp = 0
    final_ans = ''
    for i in encrypted:
        if i == ' ':
            final_ans += ' '
            continue
        final_ans += convert_to_word(i.upper(), ans[(final_temp // 3) % 3])
        final_temp += 1

    print(final_ans.capitalize())


def convert_to_word(gusfring, lospollos):
    '''Saul Goodman'''
    if gusfring.isupper():
        return chr((ord(gusfring) - lospollos - 65) % 26 + 65).lower()


main()
