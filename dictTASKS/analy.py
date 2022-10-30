pyog = {'8:00':0, '9:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0}
ptyog = {'8:00':0, '9:00':0, '10:00':0, '11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0}
vtpol = {'16:00':0, '17:00':0, '18:00':0}
htpol = {'16:00':0, '17:00':0, '18:00':0}
karsr = {'11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0}
karsb = {'11:00':0, '12:00':0, '13:00':0, '14:00':0, '15:00':0, '16:00':0, '17:00':0}
otzstat = {}
otzoleg = []
otzkir = []
otzsvet = []
knigaotz = {}

def a(c):
    o = input('расписание каких занятий вас интересуе?')
    if "йог" in o:
        print('пн,пт. с 8:00 до 15:00')
    elif 'пол' in o or 'вода' in o:
        print('вт, чт с 16:00 до 18:00')
    elif 'кар' in o:
        print('ср, сб. с 11:00 до 17:00')


def zap(a):
    g = input('хотите записаться?')
    if "да" in g:
        i = input('на какое занятие вы хотите?')
        if 'йог' in i:
            t = input('вам удобнее в понедельник или в пятницу?')
            if 'пн' or 'пон' in t:
                for i in pyog:
                    if pyog[i] < 5:
                        print('есть свободное время в:', i)
                        ee = input('вам подойдет это?')
                        if 'да' in ee:
                            pyog[i] = pyog[i] +1
                            print('запись сделана!')
                            break
            elif 'пт' in t or 'пят' in t:
                for u in ptyog:
                    if ptyog[u] < 5:
                        print('есть свободное время в:', u)
                        oo = input('вам подойдет это?')
                        if 'да' in oo:
                            ptyog[u] = ptyog[u] + 1
                            print('запись сделана!')
                            break
        elif 'пол' in i:
            t = input('вам удобнее во вторник или в четверг?')
            if 'вт' in t:
                for q in vtpol:
                    if vtpol[q] < 5:
                        print('есть свободное время в:', q)
                        zz = input('вам подойдет это?')
                        if 'да' in zz:
                            vtpol[q] = vtpol[q] +1
                            print('запись сделана!')
                            break
            elif 'чт' in t or 'чет' in t:
                for w in htpol:
                    if htpol[w] < 5:
                        print('есть свободное время в:', w)
                        pp = input('вам подойдет это?')
                        if 'да' in pp:
                            htpol[w] = htpol[w] + 1
                            print('запись сделана!')
                            break
        elif 'кар' in i:
            t = input('вам удобнее в среду или в субботу?')
            if 'ср' in t or 'сред' in t:
                for a in karsr:
                    if karsr[a] < 5:
                        print('есть свободное время в:', a)
                        gg = input('вам подойдет это?')
                        if 'да' in gg:
                            karsr[a] = karsr[a] +1
                            print('запись сделана!')
                            break
            elif 'сб' in t or 'суб' in t:
                for s in karsb:
                    if karsb[s] < 5:
                        print('есть свободное время в:', s)
                        dd = input('вам подойдет это?')
                        if 'да' in dd:
                            karsb[s] = karsb[s] + 1
                            print('запись сделана!')
                            break


def kont(a):
    s = input('назовите имя или фамилию тренера')
    if 'лег' in s or 'обч' in s:
        print('89998887766')
    elif 'рил' in s or 'тров' in s:
        print('89997776655')
    elif 'кат' in s or "ура" in s:
        print('89995554433')


def opl(a):
    g = int(input("сколько занятий вы постетили"))
    d = int(input('сколько занятий вы посетили по йоги?'))
    q = int(input('сколько занятий вы посетили по полу?'))
    z = int(input('сколько занятий вы посетили по кардио?'))
    s = 1000 * d + q*900 + z*700
    print('сумма к оплате:', s)



def otz(a):
    op = input('хотите оставить отзыв?')
    if "да" in op:
        d = input('кому вы хотите оставить отзыв?')
        h = input('дата отзыв:')
        pp = input('ваше впечатление:')
        t = input('оценка тренера')
        if 'лег' in d or 'обч' in d:
            otzoleg.append(t)
        elif 'рил' in d or 'тров' in d:
           otzkir.append(t)
        elif 'кат' in d or "ура" in d:
           otzsvet.append(t)
    knigaotz[h] = pp


def oqenki(a):
    print('олег юрьевич', sum(otzoleg)/len(otzoleg))
    print('Екатерина Муратова', sum(otzsvet)/len(otzsvet))
    print('Кирилл петров', sum(otzkir)/len(otzkir))




























