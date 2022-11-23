# Plotting-in-Discrete-Heisenberg-Group

This is a simple Python program to plot N-fold sums of finite subsets of the discrete Heisenberg group under matrix multiplication. Vectors [x,y,t] in the program are identified with the Heisenberg matrices {{1,a,c}{0,1,b}{0,0,1}} under the transformation x = a, y = b, and t = 4c-2ab, giving the addition definition seen in the program. Scalar mutliplication is also defined by k[x,t,t] = [kx,ky,(k^2)t]. These graphs demonstrate a theorem of A.G. Khovanskii for finite subsets of integers if rotated to view a projection onto the XY axis, and were used to extend this theorem to a discrete, nonabelian group. 

The program requires itertools, openGL, and PyQtGraph.
