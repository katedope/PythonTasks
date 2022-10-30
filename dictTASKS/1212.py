def a(*c):
    for i in range(0, len(c)):
        if c[i]=='p' and c[i+1]=='а' and c[i+2]=='с' and c[i+3]=='п':
            print('расписание секции')
        if c[i]=='т' and c[i+1]=='р' and c[i+2]=='е' and c[i+3]=='н':
            print('контактные данные тренера')
        if c[i] == 'о' and c[i + 1] == 'п' and c[i + 2] == 'л' and c[i + 3] == 'а':
            print('сумма оплаты 199999$')
        if c[i] == 'к' and c[i + 1] == 'а' and c[i + 2] == 'т' and c[i + 3] == 'я':
            print('поставить 5')
        if c[i] == 'п' and c[i + 1] == 'и' and c[i + 2] == 'т' and c[i + 3] == 'о':
            print('поставить Кати 5')


a()