# Class Line merepresentasikan garis ax + by + c = 0
# gradien m = -a/b
class Line:
    isTwoPoint = False  # True jika garis ini direpresentasikan oleh dua titik p1 dan p2, False jika direpresentasikan a, b, c
    # Line mempunyai variabel a, b, c
    # ATAU
    # p1 dan p2
    # Selain a, b, c, p1, dan p2, juga menghitung gradien m

    # Karena Python tidak mendukung banyak konstruktor, setelah konstruksi panggil newLine(...)
    def __init__(self):
        pass

    # Setter dengan masukan parameter a, b, dan c langsung
    def setabc(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.m = -a / b
        self.isTwoPoint = False
    
    # Setter dengan membuat garis dari dua titik
    def setTwoPoints(self, p1, p2):
        # Pada representasi dua titik,
        # a = m, b = -1, c = y1 - mx1
        self.p1 = p1
        self.p2 = p2
        self.m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        self.a = self.m
        self.b = -1
        self.c = p1[1] - p1[0]*(p2[1] - p1[1]) / (p2[0] - p1[0])    # c = y1 - mx1
        self.isTwoPoint = True
    
    # Mereturn jarak titik p0 ke garis ini
    def pointToLineDistance(self, p0):
        if(not self.isTwoPoint):
            return abs(self.a*p0[0] + self.b*p0[1] + self.c) / (self.a**2 + self.b**2)**0.5
        else:
            # Jika direpresentasikan dua titik,
            # a = m, b = -1, c = y1 - mx1; tetapi untuk menjaga kepresisian dihitung langsung tidak dengan m yang telah dihitung sebelumnya
            if(self.p2[0] - self.p1[0] == 0):   # Jika garis vertikal, jaraknya abs(x1 - x0)
                return abs(self.p2[0] - p0[0])
            return abs(p0[0]*(self.p2[1] - self.p1[1])/(self.p2[0] - self.p1[0]) - p0[1] + self.c) / (1 + (self.p2[1] - self.p1[1])**2 / (self.p2[0] - self.p1[0]) ** 2)**0.5