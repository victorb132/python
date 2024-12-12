while True:
  first_number = input('Digite um número: ')
  second_number = input('Digite outro número: ')
  operator = input('Digite o operador (+ - / *): ')

  valid_numbers = None

  try:
    float_first_number = float(first_number)
    float_second_number = float(second_number)
    valid_numbers = True
  except ValueError:
    valid_numbers = False

  if(valid_numbers is None):
    print('Um ou ambos os números digitados são inválidos.')
    continue

  alloweds_operators = '+-/*'

  if operator not in alloweds_operators:
    print('Operador inválido.')
    continue

  if len(operator) > 1:
    print('Digite apenas um operador.')
    continue

  print('Realizando sua conta. Confira o resultado abaixo:')

  if(operator == '+'):
    print(float_first_number + float_second_number)
  elif(operator == '-'):
    print(float_first_number - float_second_number)
  elif(operator == '/'):
    print(float_first_number / float_second_number)
  elif(operator == '*'):
    print(float_first_number * float_second_number)
  else:
    print('Não deveria cair aqui.')

  logout = input('Quer sair? [s]im: ').lower().startswith('s')

  if(logout):
    break