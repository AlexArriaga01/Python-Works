import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(0,2,100)
T=np.array([0])
for n in range(1,17):
    T=T+((-1)**(n+1)*(X-1)**n)/n
    if (n&(n-1))==0:
        plt.plot(X,T,label=f"Grado {n}")
Ln=np.log(X)

plt.plot(X,Ln,label="ln(x)",linewidth=3)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("ln(x) Taylor series")
plt.legend(
    loc='best',
    fontsize=10,
    frameon=True,
    title='Curvas'
)
plt.grid()

plt.show()