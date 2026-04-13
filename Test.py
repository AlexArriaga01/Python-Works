import pandas as holi
import numpy as uwu

LMA={
    "Nombre":['Aleksandra','Alejandro','Reanata','David'],
    "Edad":[20,18,23,30],
    "Valor absoluto":[-1,0,1,1],
    "Francia":[False,True,True,False]
}
DF_LMA=holi.DataFrame(LMA)
DF_LMA.index=['A','Al','Re','Da']

for i,j in DF_LMA.iterrows():
    print(i,j)
    DF_LMA.loc[i,"NOMBRE"]=DF_LMA.loc[i,"Nombre"].upper()
print(DF_LMA)

DF_LMA["nombre"]=DF_LMA["NOMBRE"].apply(str.lower)

print(DF_LMA)
print(DF_LMA.loc["A",:], type(DF_LMA.loc["A",:]))
print(DF_LMA.loc["A",:].iloc[2])
print(DF_LMA.loc[["A"],:], type(DF_LMA.loc[["A"],:]))
