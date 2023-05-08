import numpy as np

#
array1 = np.array([[1,1,1],
                  [4,4,2],
                  [2,1,-1]],dtype= float)

array2 = np.array([1,2,0], dtype=float)

x = np.linalg.solve(array1,array2)
print(x)

np.dot(array1,x)

#
array3 = np.array([[0,2,3], #quando não tiver a mesma quantidade de indices, o x1 é zero
           [4,6,7],
           [2,3,6]], dtype = float)

array4 = np.array([8,-3,5], dtype=float)

x2 =np.linalg.solve(array3,array4)
print(x2)

np.dot(array3,x2)

#
array5 = np.array([[0,10,-1,-2],
                   [-1,11,-1,3],
                   [2,-1,10,-1],
                   [0,3,-1,8]],dtype = float)

array6 = np.array([6,25,-11,15],dtype = float)

x3 = np.linalg.solve(array5,array6)
print(x3)

np.dot(array5,x3)


#
array7= np.array([[3,7,13],
                  [12,3,5],
                  [1,5,3]], dtype = float)

array8 = np.array([-76,1,28], dtype = float)

x4 = np.linalg.solve(array7,array8)
print(x4)

np.dot(array7,x4)

#
array9 = np.array([[20,35,40],
                   [15,50,60],
                   [30,40,50]], dtype = float)

array10 = np.array([3150,3600,4450], dtype = float)

x5 = np.linalg.solve(array9,array10)
print(x5)

np.dot(array9, x5)

#
array11 = np.array([[5,25,35],
           [20,40,30],
           [30,20,25]],dtype = float)

array12 = np.array([1800,2450,1950], dtype = float)

x6 = np.linalg.solve(array11,array12)

np.dot(array11,x6)

#
array13 = np.array([[1, -2, 0],
                    [0.5, 0, 0],
                    [3, 2, 4]],dtype = float)

array14 = np.array([3, 2, 4], dtype = float)

x7 = np.linalg.solve(array13,array14)

np.dot(array14,x7)

#
array15 = np.array([[1,0,-4,4],
                    [1,0,3,2],
                    [1,0,-3,3],
                    [3,3,4,4]], dtype = float)

array16 = np.array([3, 3, 4,4], dtype = float)

x8 = np.linalg.solve(array15,array16)

np.dot(array16,x8)

#
array17 = np.array([[1,-3,0,0],
              [0,0,-0.5,1],
              [2,0,0,-1],
              [1,1,1,1]], dtype = float)

array18 = np.array([0,0,0,1000])

x9 = np.linalg.solve(array17,array18)

print("Pontos de ataque de Alice:", x9[0])
print("Pontos de ataque de Bob:", x9[1])
print("Pontos de ataque de Carlos:", x9[2])
print("Pontos de ataque de Diana:", x9[3])

#
array19 = np.array([[1, 1, 1, 0, 0, 0],
              [0, 0, -1, 1, 0, 0],
              [0, 0, 0, -1, 1, 0],
              [0, -1, 0, 0, -1, 1],
              [0, 10, -10, -5, -15, 0],
              [5, -10, 0, 0, 0, -20]], dtype = float)

array20 = np.array([0, 0, 0, 0, 0, 200])

x10 = np.linalg.solve(array19, array20)

print("i12 =", round(x10[0], 4))
print("i52 =", round(x10[1], 4))
print("i32 =", round(x10[2], 4))
print("i43 =", round(x10[3], 4))
print("i54 =", round(x10[4], 4))
print("i65 =", round(x10[5], 5))