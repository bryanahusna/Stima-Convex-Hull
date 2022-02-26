# Menghitung determinan
# pl dan pr adalah titik acuan, p adalah target
def calculateDeterminan(pl, pr, p):
    return (pl[0]*pr[1] + p[0]*pl[1] + pr[0]*p[1] - p[0]*pr[1] - pr[0]*pl[1] - pl[0]*p[1])
