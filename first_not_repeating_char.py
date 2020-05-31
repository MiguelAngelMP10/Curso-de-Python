'''
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
'''


def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (
                seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letter = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letter.append((key, value[0]))

    not_repeated_letters = sorted(final_letter, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


def first_not_repeating_char_2(char_sequence):
    print(list(char_sequence))

    letter_count = {}
    for letter in char_sequence:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter, valor in letter_count.items():
        if (valor == 1):
            return letter

    return '_'


def first_not_repeating_char_3(char_sequence):

    mensaje = list(char_sequence)

    for i in mensaje:
        print(i)

    # letter_count = {}
    # for letter in char_sequence:
    #     if letter in letter_count:
    #         letter_count[letter] += 1
    #     else:
    #         letter_count[letter] = 1

    # for letter, valor in letter_count.items():
    #     if (valor == 1):
    #         return letter

    # return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))
    result = first_not_repeating_char_3(char_sequence)

# result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
