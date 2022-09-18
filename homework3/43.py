frequency = float(input('Введите частоту звука '))
if frequency >= 260.63 and frequency <= 262.63:
    print('C4')
elif frequency >= 292.66 and frequency <= 294.66:
    print('D4')
elif frequency >= 328.63 and frequency <= 330.63:
    print('E4')
elif frequency >= 348.23 and frequency <= 350.23:
    print('F4')
elif frequency >= 391.00 and frequency <= 393.00:
    print('G4')
elif frequency >= 439.00 and frequency <= 441.00:
    print('А4')
elif frequency >= 492.88 and frequency <= 494.88:
    print('B4')
else:
    print('Ноты соответствующей частоте не существует')