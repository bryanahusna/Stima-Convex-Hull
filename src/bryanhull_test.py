from bryanhull import ConvexHull

# Test for Up Side
t1 = [[0, 0], [2, 2], [4, 0]]
#tr1 = ConvexHull(t1)
#print(tr1.simplices)

t2 = [[0, 0], [2, 2], [4, 0], [2, 3]]
#tr2 = ConvexHull(t2)
#print(tr2.simplices)

t3 = [[0, 0], [2, 2], [4, 0], [2, 3], [0.41, 1.6], [3.61, 1.6]]
#tr3 = ConvexHull(t3)
#print(tr3.simplices)

t4 = [[0, 0], [2, 2], [4, 0], [2, 3], [0.41, 1.6], [3.61, 1.6], [2.85, 1.66]]
#tr4 = ConvexHull(t4)
#print(tr4.simplices)

# Test for Up and Down Side
t5 = [[0, 0], [4, 0], [2, 2], [2, 1], [2, -1], [2, -2]]
#tr5 = ConvexHull(t5)
#print(tr5.simplices)

t6 = [[0, 0], [4, 0], [2, 2], [2, 1], [2, -1], [2, -2], [4, -1], [0.5, -1]]
#tr6 = ConvexHull(t6)
#print(tr6.simplices)

t7 = [[0, 0], [2, 2], [4, 0], [2, 3], [0.41, 1.6], [3.61, 1.6], [2.85, 1.66], [2, -1], [2, -2], [4, -1], [0.5, -1]]
tr7 = ConvexHull(t7)
print(tr7.simplices)
