"""
Вася давно мечтает выиграть олимпиаду по информатике.
У него всего три слабых места: циклы, массивы и строки.
Перед сегодняшним турниром Вася провёл интенсивную подготовку, в ходе которой он решил A задач на циклы,
B задач на массивы и C задач на строки.
Впоследствии выяснилось, что из решённых задач D были и на циклы, и на массивы, E – на циклы и на строки,
F – на строки и на массивы. И даже было G задач, которые включали и циклы, и строки, и массивы.
Помогите Васе вычислить, сколько всего различных задач он решил.
Введите результат для всех 3 входных данных
"""
f = "0 0 0 0 0 0 0" #Вывод должен быть 0
s = "1 1 1 0 0 0 0" # Вывод должен быть 3
t = "1 1 1 1 1 1 1" # Вывод должен быть 1
r = f.split()
y = s.split()
k = t.split()

print(int(r[0])+int(r[1])+int(r[2])-(int(r[3])+int(r[4])+int(r[5])-int(r[6])))
print(int(y[0])+int(y[1])+int(y[2])-(int(y[3])+int(y[4])+int(y[5])-int(y[6])))
print(int(k[0])+int(k[1])+int(k[2])-(int(k[3])+int(k[4])+int(k[5])-int(k[6])))