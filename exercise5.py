number = input('Digite um número inteiro: ')

try:
    number = int(number)

    if number % 2 == 0:
        print(f'O número {number} é par.')
    else:
        print(f'O número {number} é ímpar.')

except ValueError:
    print('Você não digitou um número inteiro.')