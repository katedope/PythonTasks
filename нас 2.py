"""""
орый к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""


class Fullname:

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"{self.name} гений")


class Name(Fullname):

    def display_info_dop(self):
        print(f"{self.name} гений, но нет")

nastya = Fullname("Даня")
nastya.display_info()

nastya = Name("Даня")
nastya.display_info_dop()