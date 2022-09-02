import random
from itertools import product
import pyqtgraph as pg
import pyqtgraph.opengl as gl

vectors = []
combSet = []

m = 10

#To use predetermined matrices

#a0 = [1,1,-1] #[a,b,c]
#a1 = [-1,1,3]
#a2 = [8,-1,5]
#a3 = [-3,2,1]
#a4= [4,5,2]

#vectors.append(a0)
#vectors.append(a1)
#vectors.append(a2)
#vectors.append(a3)
#vectors.append(a4)


def generateRandomMatrices(n):
    L = []
    for i in range(0, n):
        a = random.randrange(-5,5,1)
        b = random.randrange(-5,5,1)
        c = random.randrange(-5,5,1)
        L.append([a,b,c])
    return L

vectors = generateRandomMatrices(2)

def add(L1, L2):
    a = (L1[0] + L2[0])
    b = (L1[1] + L2[1])
    c = L1[2] + L2[2] + 2*(L1[1]*L2[0] - L1[0]*L2[1])
    L = [a,b,c]
    return L

def mult(L1, k):
    a = float(k*L1[0])
    b = float(k*L1[1])
    c = float(k*k*L1[2])
    L = [a,b,c]
    return L

def removeDuplicates(L):
    T =  set(tuple(i) for i in L)
    T2 = list(T)
    print("Duplicates Removed")
    return T2

def multiComb(arr, m):
    L = list(product('01', repeat = 10))
                    #'0 through m-1', repeat = m
    sumList = []
    for i in range(0, len(L)):
        sum = [0, 0, 0]
        for j in range(0, len(L[i])):
            sum = add(sum, vectors[int(L[i][j])])
        sumList.append(mult(sum, (1/m)))
    combSet = sumList
    print("Combinations Done")
    return combSet

combSet = multiComb(vectors, m)
removeDuplicates(combSet)
print("Plotting...")

pg.mkQApp()
view = gl.GLViewWidget()
xgrid = gl.GLGridItem()
ygrid = gl.GLGridItem()
zgrid = gl.GLGridItem()
view.addItem(xgrid)
view.addItem(ygrid)
view.addItem(zgrid)
xgrid.rotate(90, 0, 1, 0)
ygrid.rotate(90, 1, 0, 0)

points = gl.GLScatterPlotItem(pos=combSet, color=(1,1,1,1), size=0.05, pxMode=False)
initials = gl.GLScatterPlotItem(pos=vectors, color=(.5,1,.5,1), size=1, pxMode=False)

pointSet1 = []
pointSet2 = []
for i in range(0, m+1):
    xCoord = (i/m)*vectors[0][0]+(1-(i/m))*vectors[1][0]
    yCoord = (i/m)*vectors[0][1]+(1-(i/m))*vectors[1][1]
    zCoord = (i/(m*m))*vectors[0][2]+((1-i)/(m*m))*vectors[1][2]+2*((i/m)*(1-(i/m))*((vectors[1][1]*vectors[0][0]) - (vectors[1][0]*vectors[0][1])))
    print(xCoord, " ", yCoord, " ", zCoord)
    pointSet1.append((xCoord, yCoord, zCoord))
for i in range(0, m+1):
    xCoord = (i / m) * vectors[0][0] + (1 - (i / m)) * vectors[1][0]
    yCoord = (i / m) * vectors[0][1] + (1 - (i / m)) * vectors[1][1]
    zCoord = (i / (m * m)) * vectors[0][2] + ((1 - i) / (m * m)) * vectors[1][2] + 2 * (
                (i / m) * (1 - (i / m)) * ((vectors[0][1] * vectors[1][0]) - (vectors[0][0] * vectors[1][1])))
    #zCoord = (1/(m))+(i/(m*m))*vectors[0][2]+((1-i)/(m*m))*vectors[1][2]+2 * ((i / m) * (1 - (i / m)) * ((vectors[0][1] * vectors[1][0]) - (vectors[0][0] * vectors[1][1])))
    pointSet2.append((xCoord, yCoord, zCoord))
sPointsUpper = gl.GLLinePlotItem(pos = pointSet1)
sPointsLower = gl.GLLinePlotItem(pos = pointSet2)
view.addItem(sPointsUpper)
view.addItem(sPointsLower)

view.addItem(points)
#view.addItem(initials)
print(len(combSet))
print(m**3)
view.show()
