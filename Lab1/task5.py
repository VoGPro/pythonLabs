import re
# Задание 5. Дана строка. Необходимо найти все даты,
# которые описаны в виде "31 февраля 2007".

sDates = "31 февраля 2007 21ыйл 23 флфы 0207 34 января 2001 мая 20 июля 972 марта 11 июня 2003 7 апреля 1932 0 ноября 9"

def showDates(s):
    dates = re.findall(r'(?:\s[1-9]|[12]\d|3[01])\s(?:декабря|января|февраля|марта|апреля|мая'
                       r'|июня|июля|августа|сентября|октября|ноября)\s(?:[1-9]\d*)', s)
    return dates

print(showDates(sDates))
