import numpy as np
from numpy import random as rn
import pandas as pd
import matplotlib.pyplot as pl
#Definicón de variables
n=int(input("Número de tiros:"))
m=int(input("Numero de juegos:"))
#Tirada de dos dados n veces
def D(n):
    Dado1=[]
    Dado2=[]
    for i in range(n):
        Dado1.append(rn.randint(1,7))
        Dado2.append(rn.randint(1,7))
    a_Dado1=np.array(Dado1)
    a_Dado2=np.array(Dado2)
    a_DadoSum=a_Dado1+a_Dado2

    Table=pd.DataFrame({
        "Dado 1":a_Dado1,
        "Dado 2":a_Dado2,
        "Suma":a_DadoSum })

    print("Table:\n",Table,"\n")
    return Table
#Generación de m juegos
LTable=[]
LPasos=[]
for j in range(m):
    Table=D(n)
    LTable.append(Table)
    Pasos=[0]
    paso=0
    for i in range(n):
        if Table["Suma"][i]<=4 or Table["Suma"][i]>=10:
            if paso==0:
                paso=paso
            else:
                paso=paso-1
        else:
            paso=paso+1
        if rn.rand()<=0.01:
            paso=0
        Pasos.append(paso)
    LPasos.append(Pasos)
#Display del histograma del la suma de los dados
for Table in LTable:
    pl.hist(Table["Suma"],bins=22)
    pl.xticks([2,3,4,5,6,7,8,9,10,11,12])
    pl.grid(True)
pl.show()
pl.clf()
#Display de los graficos de los juegos
for Pasos in LPasos:
    pl.plot(Pasos)
    pl.grid(True)
pl.show()
