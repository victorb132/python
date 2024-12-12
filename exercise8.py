name = 'Victor Novais'

index = 0

new_name = ''

while index < len(name):
  print(name[index])
  new_name += f'{name[index]}*'
  index += 1

print(new_name)