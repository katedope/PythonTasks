"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.
Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""
def k():
    i = input()
    n = int(input())
    while n>0:
         n = n-1
        if i == 'стоп':
            break
        else:
            h = int(input())
        p = h+p
    print('Итоговый счёт:', p)
    return p
a = k()
def g():
    if a >80:
        print( 'Наградить дипломом.')
    elif a > 50 and a <=80:
        print('Наградить похвальной грамотой.')
    else: print('Выдать грамоту об участии.')




