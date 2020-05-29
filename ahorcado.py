# -*- coding: utf-8 -*-
import random


mensajeFelicidads = '''
oooooooooooo           oooo   o8o             o8o        .o8                  .o8
`888'     `8           `888   `"'             `"'       "888                 "888
888          .ooooo.   888  oooo   .ooooo.  oooo   .oooo888   .oooo.    .oooo888   .ooooo.   .oooo.o
888oooo8    d88' `88b  888  `888  d88' `"Y8 `888  d88' `888  `P  )88b  d88' `888  d88' `88b d88(  "8
888    "    888ooo888  888   888  888        888  888   888   .oP"888  888   888  888ooo888 `"Y88b.
888         888    .o  888   888  888   .o8  888  888   888  d8(888  888   888  888    .o o.)88b
o888o        `Y8bod8P' o888o o888o `Y8bod8P' o888o `Y8bod88P" `Y888""8o `Y8bod88P" `Y8bod8P' 8""888P'
'''

mensajeGameOver = '''
 #####                                                      
#     #   ##   #    # ######     ####  #    # ###### #####  
#        #  #  ##  ## #         #    # #    # #      #    # 
#  #### #    # # ## # #####     #    # #    # #####  #    # 
#     # ###### #    # #         #    # #    # #      #####  
#     # #    # #    # #         #    #  #  #  #      #   #  
 #####  #    # #    # ######     ####    ##   ###### #    # 
'''


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'javascript',
    'sofa',
    'ropa',
    'nodejs',
    'Ayiz',
    'computadora',
    'teclado'
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('----- * ------- * ------- * ------- * ------- * ------- ')


def run():
    word = random_word()
    hidden_word = ['_'] * len(word)
    tries = 0
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print(mensajeGameOver)
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                break

        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('_')
        except ValueError:
            print(mensajeFelicidads)
            print('La palabra es =>{}'.format(word))


if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()
