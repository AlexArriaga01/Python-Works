import numpy as np
import matplotlib.pyplot as plt

def F(X):
    return np.array([X[0]**3-1])

def DF(X):
    return np.array([[3*X[0]**2]])

L_X=[]
ReX=np.linspace(-2,2,100)
ImX=np.linspace(-2,2,100)
for a in ReX:
    for b in ImX:
        L_X.append(np.array([a+b*1j]))

for X in L_X:
    X0=X[:]
    for i in range(20):
        if np.linalg.det(DF(X))!=0:
            delta=np.linalg.solve(DF(X),F(X))
            X=X-delta
        else:
            break

    if abs(X[0]-(1+0j))<0.5*10**(-8):
        plt.scatter(X0[0].real,X0[0].imag,s=2,c='red')
        print('Red',"\t",X,"\t",X0)

    elif abs(X[0]-(-1/2+np.sqrt(3)/2j))<0.5*10**(-8):
        plt.scatter(X0[0].real,X0[0].imag,s=2,c='blue')
        print('Red',"\t",X,"\t",X0)

    elif abs(X[0]-(-1/2-np.sqrt(3)/2j))<0.5*10**(-8):
        plt.scatter(X0[0].real,X0[0].imag,s=2,c='yellow')
        print('Red',"\t",X,"\t",X0)
    
    else:
        plt.scatter(X0[0].real,X0[0],s=5,c='black')
        print('black',"\t",X,"\t",X0)

plt.title("Fractal de Newton de f(z)=z^3-1")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()