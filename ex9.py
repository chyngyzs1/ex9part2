num = input('Введите 10 чисел через пробел ... ')
type_num = list(num.split(' '))
result = 0
for i in type_num:
    result += int(i)
print(result)