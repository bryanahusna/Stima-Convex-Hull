from math import fabs


class ConvexHull:
    # vertices adalah list of point (x, y)
    vertices = []
    simplices = []
    def __init__(self, vertices):
        self.vertices = vertices.copy()
        self.convexHullInitial()
    
    def convexHullInitial(self):
        self.vertices.sort(key=lambda k: [k[0], k[1]], reverse=False)
        left = []
        right = []
        n = len(self.vertices)
        for i in range(1, n-1):
            det = self.calculateDeterminan(0, n-1, i)
            if(det > 0):
                left.append(self.vertices[i])
            elif(det < 0):
                right.append(self.vertices[i])
            # Jika det == 0, tidak diolah karena jelas bukan titik convex hull
        self.convexHull(left, 0, n-1, True)
        self.convexHull(right, 0, n-1, False)
    
    def convexHull(self, arr, leftIdx, rightIdx, isUpSide):
        if(len(arr) == 0):
            return
        if(len(arr) == 1):
            self.simplices.append(arr[0])
        elif(len(arr) > 1):
            # t = farthest point

            # leftIdx1 = leftIdx
            # rightIdx1 = t

            # leftIdx2 = t
            # rightIdx2 = rightIdx
            # for i.x < t.x, calculateDeterminan if positif add to left
            # for i > t.idx, calculateDeterminan if positif add to right
            # rekurse

            left = []
            right = []
            #self.convexHull(left)
            #self.convexHull(right)

    # Menghitung determinan (x1, y1), (x2, y2), (x3, y3)
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

