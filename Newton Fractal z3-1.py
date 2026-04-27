import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return z**3-1

def df(z):
    return 3*z**2

Z=[]
ReZ=np.linspace(-2,2,100)
ImZ=np.linspace(-2,2,100)
for a in ReZ:
    for b in ImZ:
        Z.append(a+b*1j)

for z in Z:
    z0=z+0
    for i in range(20):
        if df(z)!=0:
            z=z-f(z)/df(z)
        else:
            break

    if abs(z-(1+0j))<0.5*10**(-8):
        plt.scatter(z0.real,z0.imag,s=5,c='red')
        print('Red',"\t",z,"\t \t \t",z0)

    elif abs(z-(-1/2+np.sqrt(3)/2j))<0.5*10**(-8):
        plt.scatter(z0.real,z0.imag,s=5,c='blue')
        print('blue',"\t",z,"\t",z0)

    elif abs(z-(-1/2-np.sqrt(3)/2j))<0.5*10**(-8):
        plt.scatter(z0.real,z0.imag,s=5,c='yellow')
        print('yellow',"\t",z,"\t",z0)

    else:
        plt.scatter(z0.real,z0.imag,s=5,c='black')
        print('black',"\t",z,"\t",z0)

plt.title("Fractal de Newton de f(z)=z^3-1")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.show()