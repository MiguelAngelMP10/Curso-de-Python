def foreign_exchange_calculator(ammount):
    COP_to_MXN=float(input('Ingrese el valor actual de la divisa  '))

    return COP_to_MXN*ammount

def foreign_exchange_calculator2(ammount):
    MXN_to_COP=float(input('Ingrese el valor actual de la divisa  '))

    return MXN_to_COP*ammount

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos colombianos a pesos mexicanos')
    print('')
    print('1. Para convertir de COP a MXN')
    print('2. Para convertir de MXN a COP')

    choose=int(input('Ingresa una opción '))

    if choose==1:
        
        ammount=float(input('Ingrese la cantidad de pesos mexicanos  '))
        result=foreign_exchange_calculator(ammount)
        print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))
        print('')
              
    elif choose==2:
              
        ammount=float(input('Ingrese la cantidad de pesos colombianos  '))
        result=foreign_exchange_calculator2(ammount)
        print('${} pesos colombianos son ${} pesos mexicanos'.format(ammount,result))
        print('')

if __name__ == '__main__':
    run()