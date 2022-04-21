# Plotting-in-Discrete-Heisenberg-Group

This is a simple Python program to plot N-fold sums in the discrete Heisenberg group under matrix multiplication. Vectors [x,y,t] in the program are identified with the Heisenberg matrices {{1,a,c}{0,1,b}{0,0,1}} by x = a, y = b, and t = 4c-2ab, giving the addition definition seen in the program. Scalar mutliplication is also defined by k[x,t,t] = [kx,ky,(k^2)t]. These graphs demonstrate some theorems of A.G. Khovanskii directly if rotated to view a projection onto the XY axis, and possibly demonstrate the extension of these theorems to a discrete, nonabelian group. 

The program uses itertools, openGL, and PyQtGraph.
