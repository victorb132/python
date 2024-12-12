list_names = ['Maria', 'Helena', 'Luiz']
list_names.append('Victor')

names = range(len(list_names))

for index in names:
  print(index, list_names[index], type(list_names[index]))