notes = str(input('Введите обозначение ноты'))
octave = int(input('Введите номер нотации октавы'))
if notes == 'C': #присваеваем обозначению ноты соответсвующую частоту
    frequency = 263.63
elif notes == 'D':    
    frequency =293.66
elif notes == 'E':
    frequency =329.63
elif notes == 'F':
    frequency =349.23
elif notes == 'G':
    frequency =392.00
elif notes == 'A':
    frequency =440.00
elif notes == 'B':
    frequency =493.88
frequency = frequency/2**(4-octave) #высчитываем частоту по обозначению ноты и  номеру нотации октавы
print(frequency)
