"""
Напишите список функций по требованию. Пользователь вводит имя. Если имя заканчивается на А,Я,Г,М, то программа добавляет
к имени "Гений". Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""
f = input()
q = ' гений'
s = 'Сверхразум'
w = 'Просто'

h = (lambda a: q if a[-1] == 'я' or a[-1] == 'г' or a[-1] == 'а' or a[-1] == 'м' s elif a[-1] == 'о' )