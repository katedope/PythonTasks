class Avtomobil:
    def __init__(self,x,y, ygol, km):
        self.x = x
        self.y = y
        self.ygol = ygol
        self.km = km
    def move(self):
        if self.ygol == 'prav':
            self.x = self.km
        if self.ygol == 'verx':
            self.y = self.km
        if self.ygol == 'levo':
            self.x = -(self.km)
        if self.ygol == 'vniz':
            self.y = -(self.km)



class Avtobus(Avtomobil):
    def __init__(self, polya, dengi, x, y, vsego):
        super().__init__(kor, x, y)
        self.polya = polya
        self.dengi = dengi
        self.vsego = vsego

    def voiti(self):
        self.polya += 1
        self.vsego += 1
    def yhol(self):
        self.polya -= 1

    def move(self):
        self.dengi = 100 * self.vsego





