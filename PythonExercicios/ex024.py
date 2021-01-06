city = str(input('Digite o nome de uma cidade: ')).strip()

split_city = city.split()

# print(city[:5] == 'Santo')
print('O primeiro nome da cidade é "Santo"?', 'Santo' in split_city[0].capitalize())
