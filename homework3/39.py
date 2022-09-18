month = str(input('Введите название месяца '))
if month == 'april' or month == 'june' or month == 'september' or month == 'november':
    print('30 days in a month')
elif month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
   print('31 days in a month')
elif month == 'february':
    print('28 or 29 days in a month')
else:
    print('error')