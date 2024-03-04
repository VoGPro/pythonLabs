import re
# Вариант 6. Реализовать функцию, которая будет проверять, является ли
# введенная строка номером кредитной карты, возвращаемое значение True или
# False. Дополнительно реализовать функцию, которая выбрасывает исключение
# о некорректном аргументе, иначе возвращает номер кредитной карты.

def detectCardType(card_number):
    card_types = [
        ('American Express', r'^3[47]\d{13}$'),
        ('Dankort', r'^5019\d{12}$'),
        ('Diners Club', r'^3(0[0-5]|[68]\d)\d{11,16}$'),
        ('Discover', r'^6(011(0[0-9]|[2-4]\d|74|7[7-9]|8[6-9]|9[0-9])|4[4-9]\d{3}|5\d{4})\d{10}$'),
        ('Elo', r'^(4[035]|5[0]|6[235])(6[7263]|9[90]|1[2416]|7[736]|8[9]|0[04579]|5[0])([0-9])([0-9])\d{10}$'),
        ('Forbrugsforeningen', r'^600722\d{10}$'),
        ('JCB', r'^35\d{14}$'),
        ('Mada', r'^(4(0(0861|1757|3024|6136|6996|7(197|395)|9201)|1(2565|0621|0685|7633|9593)|2(0132|1141|281(7|8|9)|689700|8(331|67(1|2|3)))|3(1361|2328|4107|9954)|4(0(533|647|795)|5564|6(393|404|672))|5(5(036|708)|7865|7997|8456)|6(2220|854(0|1|2|3))|7(4491)|8(301(0|1|2)|4783|609(4|5|6)|931(7|8|9))|93428)|5(0(4300|6968|8160)|13213|2(0058|1076|4(130|514)|9(415|741))|3(0(060|906)|1(095|196)|2013|5(825|989)|6023|7767|9931)|4(3(085|357)|9760)|5(4180|7606|8563|8848)|8(5265|8(8(4(5|6|7|8|9)|5(0|1))|98(2|3))|9(005|206)))|6(0(4906|5141)|36120)|9682(0(1|2|3|4|5|6|7|8|9)|1(0|1)))\d{10}$'),
        ('Maestro', r'^(?:5[06789]\d\d|(?!6011[0234])(?!60117[4789])(?!60118[6789])(?!60119)(?!64[456789])(?!65)6\d{3})\d{8,15}$'),
        ('Mastercard', r'^(5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)\d{12}$'),
        ('Meeza', r'^5078(03|09|10|11)\d{10}$'),
        ('Mir', r'^220[0-4]\d{12}$'),
        ('Troy', r'^9792\d{12}$'),
        ('UATP', r'^1\d{14}$'),
        ('UnionPay', r'^62[0-5]\d{13,16}$'),
        ('Visa', r'^4\d{12}(\d{3}|\d{6})?$')
    ]
    for type in card_types:
        if bool(re.match(type[1], str(card_number))):
            return type[0]
    else:
        return ''

def cardValidator(card_number, date, cvv):
    digit_date = date.replace('/', '')
    if not card_number.isdigit() or not digit_date.isdigit() or not cvv.isdigit() or not date.__contains__('/'):
        raise NotDigitException()
    card_type = detectCardType(card_number)
    date_pattern = r'(0[1-9]|1[0-2])/([0-9]{2})'
    cvv_pattern = r'[0-9]{3}'
    date_match = bool(re.match(date_pattern, str(date)))
    cvv_match = bool(re.match(cvv_pattern, str(cvv)))
    if card_type and date_match and cvv_match:
        return f'Valid\nCard type: {card_type}'
    else:
        return 'Not valid'

class NotDigitException(Exception):
    def __str__(self):
        return 'Invalid card value'


cards = [
    ('4263982640269299', '04/2026', '738'),
    ('426398264069299', '04/2026', '738'),
    ('2200050800717554', '08/25', '539'),
    ('5425233430109903', '04/2026', '234'),
    ('374245455400126', '05/2026', '925'),
    ('3566000020000410', '02/2026', '123'),
    ('63621270000457013', '8/2026', '634')
]
try:
    for card in cards:
        print()
        print(card[0], card[1], card[2])
        print(cardValidator(card[0], card[1], card[2]))
except NotDigitException as e:
    print(e)