first_name = input('Digite seu primeiro nome: ')

if first_name:
  name_length = len(first_name)

  if (name_length <= 4):
    print('Seu nome é curto')
  elif (name_length >= 5 and name_length <= 6):
    print('Seu nome é normal')
  elif (name_length > 6):
    print('Seu nome é muito grande')
else:
  print('Desculpe, você deixou campos vazios.')