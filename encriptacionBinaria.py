# -*- coding= UTF-8 -*-


def cypher(mensaje):
    mensajeEncrip = ""
    for i in mensaje:
        binario = bin(ord(i))
        mensajeEncrip += binario + ":"

    return mensajeEncrip[:-1]


def decipher(mensaje):
    mensajeDesifrado = ""
    caracteres = mensaje.split(":")
    for i in range(0, len(caracteres)):
        mensajeDesifrado += chr(int(caracteres[i], 2))

    return mensajeDesifrado


def run():

    while True:
        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?
            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            print('cifrar')
            message = str(input('Escribe tu mensaje a encriptar :'))
            cypher_mensaje = cypher(message)
            print(cypher_mensaje)
        elif command == 'd':
            print('decifrar')
            message = str(input('Escribe tu mensaje a desencriptar:'))
            decipher_mensaje = decipher(message)
            print(decipher_mensaje)
        elif command == 's':
            print('salir')
            exit()
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
