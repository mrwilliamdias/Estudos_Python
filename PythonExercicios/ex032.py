from datetime import date

year = int(input('Digite qual ano deseja analisar. Digite 0 para o ano atual: '))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} é bissesto!'.format(year))
else:
    print('{} NÃO é bissesto!'.format(year))
