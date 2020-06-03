def run():
    counter = 0
    with open("aleph.txt", 'r', encoding='UTF8') as fichero:
        for line in fichero:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()
