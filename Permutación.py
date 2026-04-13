import pandas as pd
import numpy as np

n=int(input("Ingrese el número de participantes:"))

L=np.array([])
Indices=[]
D={}
for i in range(n):
    p=str(input(f"Paricipante {i+1}:"))
    L=np.append(L,p)
    Indices.append(p)
    D[p]=""

for i in range(n):
    L0=L.copy()
    for j in range(i+1):
        L0[i-j]=""
    D[L[i]]=L0
df_D=pd.DataFrame(D)
df_D.index=Indices
df_D_T=df_D.transpose()

for i in range(n):
    for j in range(n):
        if df_D_T.iloc[i,j]!="":
            df_D_T.iloc[i,j]=df_D_T.index[i]+" vs "+df_D_T.columns[j]

print(df_D_T)