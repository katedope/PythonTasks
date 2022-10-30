import PythonTasks
from PythonTasks.dictTASKS import analy
a = input('Здравствуйте, какой у вас вопрос?')
if 'аспи' in a:
    analy.a(a)
    analy.zap(a)
elif 'онта' in a or 'мер' in a:
    analy.kont(a)
    analy.zap(a)
elif 'плат' in a or 'сум' in a or 'день' in a:
    analy.opl(a)
    analy.otz(a)
elif "оце" in a or "рей" in a or 'топ' in a:
    analy.oqenki(a)



