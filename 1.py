print('Введите число a: ')
a = int(input())
print('Введите число b: ')
b = int(input())

print('Сумма: ', a + b)
print('Разность: ', a - b)
print('Произведение: ', a * b)
print('Среднее арифметическое: ', (a + b) / 2)
print('Разность максимального и минимального модуля: ', max(abs(a), abs(b)) - min(abs(a), abs(b)))
if b == 0:
    print('На ноль делить нельзя!')
else:
    print('Частное чисел: ', format(a / b, '.2g'))
