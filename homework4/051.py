score = int(input('Введите количество бутылок ')) #вводим количество бутылок
print('There are', score, 'green bottles hanging on the wall.', score,
             'green bottles hanging on the wall,  and if 1 green bottle should accidentally fall.') #выводим на экран условие
print('how many green bottles will be hanging on the wall?') #
answer = int(input('Введите ответ ')) #просим ввести пользователя ответ на заданое условие
while answer != score - 1: # задаем цикл при котром ответ не верный
    if answer != score - 1:  #задаем условие в этом цикле
        print('no, try again')  #выводим  на экран что ответ неверный
        answer = int(input('Попробуйте еще раз ')) # просим ввести ответ еще раз
while answer == score - 1 !=0:  # задаем цикл в котором ответ правильный. но не равен нулю
    if answer == score -1 !=0:  #задаем условие
        print('There will be', answer, 'green bottles hanging on the wall') #выводим на экран правильный ответ
    break
while answer == 0: # задаем цикл что ответ равен нулю
    if answer == 0: #задаем условие
        print('there are no more green hanging on the wall') #выводим на экран что бутылок на стене больше нет
    break
