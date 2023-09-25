print('Укажите ваше имя: ')
name = str(input())
print('Укажите ваш возраст: ')
age = int(input())
print('Укажите город проживания: ')
city = str(input())
print('Укажите страну проживания: ')
country = str(input())

print(f'Уважаемый {name}! \n'
      f'На сегодняшний день Вы проживаете в стране {country}, в городе {city}, и вы родились в {2023-age}')