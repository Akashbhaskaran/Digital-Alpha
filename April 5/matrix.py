from typing import re

A = [[3, 5, 6],
     [4, 8, 10],
     [2, 1, 8]]

I = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
   # iterate through columns of Y
   for j in range(len(I[0])):
       # iterate through rows of Y
       for k in range(len(I)):
           result[i][j] += A[i][k] * I[k][j]


print(result)
if(A==result):
    print("A = A.I , proved")
