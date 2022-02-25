# Class Line merepresentasikan garis ax + by + c = 0
# gradien m = -a/b
from cv2 import convexHull
from sympy import true


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
    
    # Mereturn jarak titik ke garis ini
    def pointToLineDistance(self, p0):
        if(not self.isTwoPoint):
            return abs(self.a*p0[0] + self.b*p0[1] + self.c) / (self.a**2 + self.b**2)**0.5
        else:
            # Jika direpresentasikan dua titik,
            # a = m, b = -1, c = y1 - mx1; tetapi untuk menjaga kepresisian dihitung langsung tidak dengan m yang telah dihitung sebelumnya
            if(self.p2[0] - self.p1[0] == 0):   # Jika garis vertikal, jaraknya abs(x1 - x0)
                return abs(self.p2[0] - p0[0])
            return abs(p0[0]*(self.p2[1] - self.p1[1])/(self.p2[0] - self.p1[0]) - p0[1] + self.c) / (1 + (self.p2[1] - self.p1[1])**2 / (self.p2[0] - self.p1[0]) ** 2)**0.5

class ConvexHull:
    # vertices adalah list of point (x, y)
    vertices = []
    simplices = []
    def __init__(self, vertices):
        self.vertices = vertices.copy()
        self.convexHullInitial()
    
    def convexHullInitial(self):
        self.vertices.sort(key=lambda k: [k[0], k[1]], reverse=False)
        leftArr = []
        rightArr = []
        n = len(self.vertices)
        for i in range(1, n-1):
            det = self.calculateDeterminan(0, n-1, i)
            if(det > 0):
                leftArr.append(self.vertices[i])
            elif(det < 0):
                rightArr.append(self.vertices[i])
            # Jika det == 0, tidak diolah karena jelas bukan titik convex hull
        self.convexHull(leftArr, self.vertices[0], self.vertices[n-1], True)
        self.convexHull(rightArr, self.vertices[0], self.vertices[n-1], False)
    
    def convexHull(self, arr, leftPoint, rightPoint, isUpSide):
        if(len(arr) == 0):
            return
        if(len(arr) == 1):
            self.simplices.append(arr[0])
        elif(len(arr) > 1):
            line = Line()
            line.setTwoPoints(leftPoint, rightPoint)
            # t = farthest point
            t = arr[0]
            tidx = 0
            tdist = line.pointToLineDistance(t)
            currdist = tdist
            n = len(arr)
            for i in range(1, n):
                currdist = line.pointToLineDistance(arr[i])
                if(currdist > tdist):
                    tdist = currdist
                    tidx = i
            t = arr[tidx]
            self.simplices.append(t)

            leftArr = []
            for i in range(tidx):
                det = calculateDeterminan(leftPoint, t, arr[i])
                if(det > 0):
                    leftArr.append(arr[i])
            rightArr = []
            for i in range(tidx+1, n):
                det = calculateDeterminan(t, rightPoint, arr[i])
                if(det > 0):
                    rightArr.append(arr[i])
            
            self.convexHull(leftArr, leftPoint, t, isUpSide)
            self.convexHull(rightArr, t, rightPoint, isUpSide)
            # leftIdx1 = leftIdx
            # rightIdx1 = t
            # leftIdx2 = t
            # rightIdx2 = rightIdx
            # for i.x < t.x, calculateDeterminan if positif add to left
            # for i > t.idx, calculateDeterminan if positif add to right
            # rekurse

    # Menghitung determinan (x1, y1), (x2, y2), (x3, y3) dengan OOP
    # Positif berarti titik 3 di atas atau kiri garis titik 1 dan 2
    # leftIdx mewakili indeks titik 1, rightIdx titik 2, dan checkIdx titik 3 pada self.vertices
    # rumus: x1y2 + x3y1 + x2y3 - x3y2 - x2y1 - x1y3
    def calculateDeterminan(self, leftIdx, rightIdx, checkIdx):
        return (self.vertices[leftIdx][0]*self.vertices[rightIdx][1]
            + self.vertices[checkIdx][0]*self.vertices[leftIdx][1]
            + self.vertices[rightIdx][0]*self.vertices[checkIdx][1]
            - self.vertices[checkIdx][0]*self.vertices[rightIdx][1]
            - self.vertices[rightIdx][0]*self.vertices[leftIdx][1]
            - self.vertices[leftIdx][0]*self.vertices[checkIdx][1])

# Menghitung determinan dengan fungsi klasik
def calculateDeterminan(pl, pr, p):
    return (pl[0]*pr[1] + p[0]*pl[1] + pr[0]*p[1] - p[0]*pr[1] - pr[0]*pl[1] - pl[0]*p[1])
