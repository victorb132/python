first_value = input('Digite um valor: ')
second_value = input('Digite outro valor: ')

if (first_value > second_value):
    print(f'O primeiro valor: {first_value} é maior que o segundo valor: {second_value}')
elif (first_value < second_value):
    print(f'O segundo valor: {second_value} é maior que o primeiro valor: {first_value}')
else:
    print('Os valores são iguais')