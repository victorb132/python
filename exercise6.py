hour = input('Digite a hora atual: ')

try:
  hour = float(hour)
  if hour >= 0 and hour <= 11.59:
    print('Bom dia!')
  elif hour >= 12 and hour <= 17.59:
    print('Boa tarde!')
  elif hour >= 18 and hour <= 23.59:
    print('Boa noite!')
  else:
    print('Hora inválida.')
except ValueError:
  print('Você não digitou um número.')