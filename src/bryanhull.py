from line import Line
from utils import *

# Class untuk menemukan convex hull
# Hasil langsung dihitung ketika constructor dipanggil, disimpan di atribut simplices
class ConvexHull:
    # vertices adalah list of point (x, y)
    vertices = []
    simplices = []
    def __init__(self, vertices):
        self.vertices = vertices.copy()
        self.convexHullInitial()
    
    def convexHullInitial(self):
        # Mengecek kasus khusus
        if(len(self.vertices) == 0):
            return
        elif(len(self.vertices) == 1):
            self.simplices.append(self.vertices[0])
            return

        self.vertices.sort(key=lambda k: [k[0], k[1]], reverse=False)   # Mengurutkan berdasarkan x menaik
        upArr = []
        downArr = []
        n = len(self.vertices)

        # Titik paling kiri (0) dan kanan (n-1) termasuk dalam convex hull
        self.simplices.append(self.vertices[0])
        self.simplices.append(self.vertices[n-1])

        # Menambahkan titik-titik ke atas atau bawah
        for i in range(1, n-1):
            det = calculateDeterminan(self.vertices[0], self.vertices[n-1], self.vertices[i])
            if(det > 0):
                upArr.append(self.vertices[i])
            elif(det < 0):
                downArr.append(self.vertices[i])
            # Jika det == 0, tidak diolah karena jelas bukan titik convex hull
        
        # Penentuan titik convex hull bagian atas
        self.convexHull(upArr, self.vertices[0], self.vertices[n-1])
        # Penentuan titik convex hull bagian bawah
        # array bagian bawah dibalik karena bagian bawah dapat dihitung memakai kode yang sama dengan bagian atas, tetapi dibalik
        downArr.reverse()
        self.convexHull(downArr, self.vertices[n-1], self.vertices[0])
    
    def convexHull(self, arr, leftPoint, rightPoint):
        if(len(arr) == 0):
            return
        if(len(arr) == 1):  # Kalau tersisa satu titik, titik tersebut masuk convex hull
            self.simplices.append(arr[0])
        elif(len(arr) > 1):
            # Menentukan titik terjauh
            line = Line()
            line.setTwoPoints(leftPoint, rightPoint)    # Membuat garis antara titik kiri dan kanan, untuk pengukuran jarak
            t = arr[0]  # titik terjauh saat ini
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
            self.simplices.append(t)    # Titik terjauh masuk convex hull

            # Pembuatan daftar titik selanjutnya yang akan direkursi
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
            
            # Solve subproblem
            self.convexHull(leftArr, leftPoint, t)
            self.convexHull(rightArr, t, rightPoint)
