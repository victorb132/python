import re

cpf_number = input('Digite seu CPF: ')

try:
  cpf_number = re.sub(r'[^0-9]', '',cpf_number)
  first_nine_numbers = cpf_number[:9]
  first_digit_result = 0

  for index, number in enumerate(list(range(10, 1, -1))):
    first_digit_result += int(first_nine_numbers[index]) * number

  first_digit = (first_digit_result * 10) % 11
  first_digit = first_digit if first_digit <= 9 else 0
  print(first_digit)

  second_ten_numbers = first_nine_numbers + str(first_digit)
  second_digit_result = 0

  for index, number in enumerate(list(range(11, 1, -1))):
    second_digit_result += int(second_ten_numbers[index]) * number

  second_digit = (second_digit_result * 10) % 11
  second_digit = second_digit if second_digit <= 9 else 0
  print(second_digit)


except ValueError:
  print('Você não digitou um número inteiro.')