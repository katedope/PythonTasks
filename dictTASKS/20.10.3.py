"""
Напишите функцию которая принимает 2 числа и выводит все числа между ними которые делятся на 3.
Напишите декоратор который выводит фразу:
"Данная функция выводит все числа между Число А и Число Б"(сюда подставьте числа что принимает функция)
и оберните функцию чтобы данная фраза выводилась перед ее выполнением
"""
def meg(add):
    def dekor(arg1,arg2):
        add(arg1,arg2)
        ma = max(arg1, arg2)
        mi = min(arg1, arg2)
        for i in range(mi, ma):
            if i % 3 == 0:
                print(i)
    return dekor

def typ(a, b):
    print('Данная функция выводит все числа между Число', a ,'и Число', b)

dekot = meg(typ)
dekot(20,2)


