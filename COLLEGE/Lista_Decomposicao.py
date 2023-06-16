#Imports
import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

#1

A = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype = float)

B = np.array([[3,1,2],[6,3,4],[3,1,5]], dtype = float)

P,L,U  = lu(A)

print(P)
print('\n')
print(L)
print('\n')
print(U)
print('\n')
print('\n')

P,L,U  = lu(B)

print(P)
print('\n')
print(L)
print('\n')
print(U)
print('\n')
print('\n')

#2
A = np.array([[2,1,-1],[4,6,-2],[-2,7,2]], dtype = float)

B = np.array([[1,2,1],[2,1,3],[1,1,2]], dtype = float)

r1 = np.array([3,7,5], dtype = float)
r2 = np.array([5,8,6], dtype = float)

lu = lu_factor(A)
print(lu)
print('\n')
x2 = lu_solve(lu,r2)
print(x2)
print('\n')
print('\n')

#3

A = np.array([[2,1,-1],[4,6,2],[-2,7,2]], dtype = float)

B = np.array([[1,3,1],[1,1,2],[2,3,4]], dtype = float)

lu = lu_factor(A)
print(lu)
print('\n')

lu = lu_factor(B)
print(lu)
print('\n')
print('\n')

#4

A = np.array([[2,3,4],[4,2,3],[3,4,2]], dtype = float)

t1 = np.array([150,180,210], dtype = float)
t2 = np.array([200,220,240], dtype = float)
t3 = np.array([250,260,270], dtype = float)

lu = lu_factor(A)
x3 = lu_solve(lu,t1)
print(x3)
print('\n')

x4 = lu_solve(lu,t2)
print(x4)
print('\n')

x5 = lu_solve(lu,t3)
print(x5)
print('\n')
print('\n')

#5

A = np.array([[3,2,4],[5,4,3],[4,5,2]], dtype = float)

r1 = np.array([200,300,400], dtype = float)
r2 = np.array([250,350,450], dtype = float)
r3 = np.array([300,400,500], dtype = float)

lu = lu_factor(A)
print(lu)

x6 = lu_solve(lu,r1)
print(x6)

x7 = lu_solve(lu,r2)
print(x7)

x8 = lu_solve(lu,r3)
print(x8)
print('\n')
print('\n')

#6
A = np.array([[4,6,2],[5,3,4],[6,4,3]], dtype = float)

lu = lu_factor(A)
print(lu)

r1 = np.array([3000,2500,2700], dtype = float)
r2 = np.array([2800,2400,2600], dtype = float) 
r3 = np.array([3200,2600,2800], dtype = float)

x9 = lu_solve(lu,r1)
print(x9)
print('\n')
x10 =lu_solve(lu,r2)
print(x10)
print('\n')
x11 = lu_solve(lu,r3)
print(x11)