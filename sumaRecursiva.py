# -*- coding= UTF-8 -*-
def suma(number):
    if number == 0:
        return 0
    return number + suma(number - 1)

if __name__ == '__main__':
    number = int(input('Escribe un número:'))
    result = suma(number)
    print(result)