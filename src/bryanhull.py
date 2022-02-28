from line import Line
from utils import *

# Class untuk menemukan convex hull
# Hasil langsung dihitung ketika constructor dipanggil, disimpan di atribut simplices
class ConvexHull:
    # vertices adalah list of point (x, y)
    #vertices = []
    #convexhullpoints = []
    #simplices = []
    def __init__(self, vertices):
        self.vertices = []
        self.convexhullpoints = []
        self.simplices = []
        i = 0
        for vertex in vertices:
            self.vertices.append(vertex.copy() + [i])
            i += 1
        
        self.convexHullInitial()
    
    def convexHullInitial(self):
        # Mengecek kasus khusus
        if(len(self.vertices) == 0):
            return
        elif(len(self.vertices) == 1):
            self.convexhullpoints.append(self.vertices[0])
            return

        self.vertices.sort(key=lambda k: [k[0], k[1]], reverse=False)   # Mengurutkan berdasarkan x menaik
        upIdxArr = []
        downIdxArr = []
        n = len(self.vertices)

        # Titik paling kiri (0) dan kanan (n-1) termasuk dalam convex hull
        self.convexhullpoints.append(self.vertices[0])
        self.convexhullpoints.append(self.vertices[n-1])

        # Menambahkan titik-titik ke atas atau bawah
        for i in range(1, n-1):
            det = calculateDeterminan(self.vertices[0], self.vertices[n-1], self.vertices[i])
            if(det > 0):
                upIdxArr.append(i)
            elif(det < 0):
                downIdxArr.append(i)
            # Jika det == 0, tidak diolah karena jelas bukan titik convex hull
        
        # Penentuan titik convex hull bagian atas
        if(len(upIdxArr) == 0):
            self.simplices.append([0, n-1])
        else:
            self.convexHull(upIdxArr, 0, n-1)
        # Penentuan titik convex hull bagian bawah
        # array bagian bawah dibalik karena bagian bawah dapat dihitung memakai kode yang sama dengan bagian atas, tetapi dibalik
        if(len(downIdxArr) == 0):
            self.simplices.append([n-1, 0])
        else:
            downIdxArr.reverse()
            self.convexHull(downIdxArr, n-1, 0)
        
        for i in range(len(self.simplices)):
            self.simplices[i] = [self.vertices[self.simplices[i][0]][2], self.vertices[self.simplices[i][1]][2]]
    
    def convexHull(self, idxArr, leftPointIdx, rightPointIdx):
        if(len(idxArr) == 0):
            return
        if(len(idxArr) == 1):  # Kalau tersisa satu titik, titik tersebut masuk convex hull
            self.convexhullpoints.append(self.vertices[idxArr[0]])
            self.simplices.append([leftPointIdx, idxArr[0]])
            self.simplices.append([idxArr[0], rightPointIdx])
        elif(len(idxArr) > 1):
            leftPoint = self.vertices[leftPointIdx]
            rightPoint = self.vertices[rightPointIdx]
            # Menentukan titik terjauh
            line = Line()
            line.setTwoPoints(leftPoint, rightPoint)    # Membuat garis antara titik kiri dan kanan, untuk pengukuran jarak
            t = self.vertices[idxArr[0]]  # titik terjauh saat ini
            tidx = 0
            tdist = line.pointToLineDistance(t)
            currdist = tdist
            n = len(idxArr)
            for i in range(1, n):
                currdist = line.pointToLineDistance(self.vertices[idxArr[i]])
                if(currdist > tdist):
                    tdist = currdist
                    tidx = i
            t = self.vertices[idxArr[tidx]]
            self.convexhullpoints.append(t)    # Titik terjauh masuk convex hull

            # Pembuatan daftar titik selanjutnya yang akan direkursi
            leftArr = []
            for i in range(tidx):
                det = calculateDeterminan(leftPoint, t, self.vertices[idxArr[i]])
                if(det > 0):
                    leftArr.append(idxArr[i])
            rightArr = []
            for i in range(tidx+1, n):
                det = calculateDeterminan(t, rightPoint, self.vertices[idxArr[i]])
                if(det > 0):
                    rightArr.append(idxArr[i])
            
            # Solve subproblem
            if(len(leftArr) == 0):
                self.simplices.append([leftPointIdx, idxArr[tidx]])
            else:
                self.convexHull(leftArr, leftPointIdx, idxArr[tidx])

            if(len(rightArr) == 0):
                self.simplices.append([idxArr[tidx], rightPointIdx])
            else:
                self.convexHull(rightArr, idxArr[tidx], rightPointIdx)
