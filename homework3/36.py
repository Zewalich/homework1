person_age = int(input('Введите возраст человека '))
if person_age<=21 and person_age>=0: #задаем условие при котором собачий возраст меньше 2 лет
    print(person_age/10.5) #выводим возраст в переводе на собачий
elif person_age>21: #задаем условие при котором собачий возраст больше 2 лет
    print(2 + (person_age-21)/4) #выводим возраст в переводе на собачий
else:
    print('Ошибка')