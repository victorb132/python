import os

list_products = []

while True:
    print('Selecione uma opção')
    option = input('[i]nserir [a]pagar [l]istar: ')

    if option == 'i':
        os.system('clear')
        value = input('Valor: ')
        list_products.append(value)
    elif option == 'a':
        index_string = input(
            'Escolha o índice para apagar: '
        )

        try:
            index = int(index_string)
            del list_products[index]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif option == 'l':
        os.system('clear')

        if len(list_products) == 0:
            print('Nada para listar')

        for i, value in enumerate(list_products):
            print(i, value)
    else:
        print('Por favor, escolha i, a ou l.')