number = int(input('Введите число от 10 до 20 '))  #предлагаем пользователю ввести число от 10 до 20
while number<10:  #задаем цикл при котором число меньше 10
    if number < 10: #задаем условие в этом цикле
        print('Too low') #если условие совпадает, выводим на экран что число меньше
        number = int(input('Введите другое число '))  #просим ввести пользователя новое число
while number>20: #задаем цикл при котором число больше 20
    if number> 20:  #задаем условие для этого цикла
        print('Too higt')  #при совпадении условия выводим что число больше заданого
        number = int(input('Введите другое число '))  #просим ввести еще одно число
else:
        print('Thank you') #выводим на экран спасибо при несовпадении предыдущих условиях, т.е. попадания в наш промежуток

