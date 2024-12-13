import random

for _ in range(100):
  first_nine_numbers = ''
  for _ in range(9):
    first_nine_numbers += str(random.randint(0, 9))

  first_digit_result = 0

  for index, number in enumerate(list(range(10, 1, -1))):
    first_digit_result += int(first_nine_numbers[index]) * number

  first_digit = (first_digit_result * 10) % 11
  first_digit = first_digit if first_digit <= 9 else 0

  second_ten_numbers = first_nine_numbers + str(first_digit)
  second_digit_result = 0

  for index, number in enumerate(list(range(11, 1, -1))):
    second_digit_result += int(second_ten_numbers[index]) * number

  second_digit = (second_digit_result * 10) % 11
  second_digit = second_digit if second_digit <= 9 else 0

  generated_cpf = f'{first_nine_numbers}{first_digit}{second_digit}'
  print(generated_cpf)