total = 0
while total <= 50:  # задаем условие что цикл будет работать пока значение будет меньше или равно 50
    if total <= 50:  # задаем что наши значения должны быть меньше либо равны 50
        number = int(input('Введите число '))  # Вводим число для прибовления к тотал при условии что значение меньше или равно 50
        total = total + number  # прибовляем введеное число к присвоеному значению total
        print('The total is', total)  # выводим на экран результат прибовления до завершения цикла
