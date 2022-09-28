"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""
n = int(input())
t = set()
yt = set()
s = n
while s > 0:
    k = int(input())
    s = s - k
    h = set()
    for i in range(1, k+1):
        m1 = input()
        h.add(m1)
    if len(t) == 0:
        t = t|h
    else:
        t.intersection_update(h)
    yt = yt|h
print(t, yt)


