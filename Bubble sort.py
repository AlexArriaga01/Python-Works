import pandas as pd
import random

def ConjuntoRandom(n):
    X=[]
    for i in range(0,n):
        R=random.randint(0,9)
        X.append(R)
    print(X)
    return X

def ConjuntoManual(n):
    X=[]
    for i in range(0,n):
        x=int(input(f"X_{i+1}>>"))
        X.append(x)
    print(X)
    return X

def BuenOrden(X,Y):
    I=0
    for i in range(len(X)):
        for j in range(1,len(X)-i):
            if X[j-1]>X[j]:
                X[j-1],X[j]=X[j],X[j-1]
                Y[j-1],Y[j]=Y[j],Y[j-1]
            I=I+1
            print(f"Iteración {I}:")
            print(f"{X[j-1]},{X[j]}>>{X[j]},{X[j-1]}")
            print(X)
    print("La lista bien ordenada es:")
    print(X)
    return X,Y

print("Ingrese:")
print("0 Para generar un conjunto random")
print("1 Para generar un conjunto manualmente")
print("2 Para modificar un .xlsx")
selec=int(input(">>"))

if selec==0:
    n=int(input("Ingrese la cardinalidad del conjunto >>"))
    Y=[]
    for i in range(n):
        Y.append("")
    BuenOrden(ConjuntoRandom(n),Y)
elif selec==1:
    n=int(input("Ingrese la cardinalidad del conjunto >>"))
    Y=[]
    for i in range(n):
        Y.append("")
    BuenOrden(ConjuntoManual(n),Y)
elif selec==2:
    df = pd.read_excel('Bubble.xlsx')
    col1 = df['Indice'].astype(str).tolist()
    col2 = df['Ponderacion'].astype(str).tolist()
    BuenOrden(col2,col1)
    col2,col1=BuenOrden(col2,col1)
    new_df = pd.DataFrame({
    'Indice': col1,
    'Ponderacion': col2
    })
    new_df.to_excel('Bubble_new.xlsx', index=False)
else:
    print("Selección inválida")

print("Trivial")