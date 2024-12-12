import os

secret_word = 'banana'
accepted_words = ''
attemps = 0;

while True:
  os.system('clear')

  word = input('Digite uma letra: ')
  attemps += 1

  if len(word) > 1:
    print('Digite apenas uma letra.')
    continue

  if word in secret_word:
    accepted_words += word

  end_word = ''
  for secret_letter in secret_word:
    if secret_letter in accepted_words:
      end_word += secret_letter
    else:
      end_word += '*'
  print(end_word)

  if end_word == secret_word:
    os.system('clear')
    print('VOCÊ GANHOU!! PARABÉNS!')
    print(f'A palavra era {secret_word}')
    print(f'Tentativas: {attemps}')
    accepted_words = ''
    attemps = 0

