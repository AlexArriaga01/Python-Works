import numpy as np
import pandas as pd

n=int(input("Número de variables: "))

M=[]
print("Ingrese la matriz de coeficientes por filas:")
for i in range(1,n+1):
    F=[]
    for j in range(1,n+1):
        x=float(input(f"x_{i},{j}: "))
        F.append(x)
    M.append(F)
arr_M=np.array(M)

R=[]
print("Ingrese la matriz de resultados:")
for i in range(n):
    F=[]
    x=int(input(f"C_{i}: "))
    F.append(x)
    R.append(F)
arr_R=np.array(R)

for i in range(n):
    for j in range(n):
        if i==j and arr_M[i][j]!=0:
            arr_M[i]=arr_M[i]/arr_M[i][j]
            arr_R[i]=arr_R[i]/arr_M[i][j]

    for j in range(n):
        if i!=j:
            arr_M[j]=arr_M[j]-arr_M[j][i]*arr_M[i]
            arr_R[j]=arr_R[j]-arr_M[j][i]*arr_R[i]

print("\n",pd.DataFrame(arr_M).to_string(index=False,header=False))
print("\n"+"="*50+"\n")
print(pd.DataFrame(arr_R).to_string(index=False,header=False))