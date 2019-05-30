from datetime import datetime, date, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')


today = date.today()
print('Сегодняшняя дата', today.strftime('%d.%m.%Y' ' ''г.'))
delta = timedelta(days=1)
yesterday = today - delta
print('Вчерашняя дата', yesterday.strftime('%d.%m.%Y' ' ''г.'))
delta2 = timedelta(days=30) # что если в месяце не 30 дней а 28 или 31? Не пойму как можно еще решить данную задачу, более точно.
month_ago = today - delta2
print('Месяц назад', month_ago.strftime('%d.%m.%Y' ' ''г.'))


date_string = "01/01/17 12:10:03.234567"
string_datetime = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')