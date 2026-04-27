import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from sympy import sympify,GoldenRatio

def S():
    expr_a=ent_a.get()
    alpha=float(sympify(expr_a, locals={"phi": GoldenRatio}))
    n=1024

    X=np.linspace(0,n,n+1)
    Y=np.linspace(0,n,n+1)

    Xn=X*np.cos(2*np.pi*X*alpha)
    Yn=Y*np.sin(2*np.pi*Y*alpha)

    plt.scatter(Xn,Yn,s=8)
    plt.grid()
    plt.show()

def clear_S():
    plt.clf()
    plt.grid()
    plt.show()

def slider(event=None):
    clear_S()
    sli_val=sli_var.get()
    ent_a.delete(0,tk.END)
    ent_a.insert(0,f"{sli_val:.3f}")
    S()

window=tk.Tk()
window.title("Generador de espirales")

lab=tk.Label(window,text="Ingrese el ángulo en radianes. \n La entrada admite: 'pi', 'phi', '*', '/'")
lab.pack()

ent_a=tk.Entry()
ent_a.pack()

bu_S=tk.Button(window,text="Generar espiral",command=S)
bu_S.pack()

sli_frame=tk.Frame(window)
sli_frame.pack()

sli_var=tk.DoubleVar(value=1.0)
min_val=-2*np.pi
max_val=2*np.pi
sli=tk.Scale(
    sli_frame,
    from_=min_val,
    to=max_val,
    resolution=0.001,
    orient=tk.HORIZONTAL,
    variable=sli_var,
    length=500,
    command=slider,
)
sli.pack()

bu_clf=tk.Button(window,text="Limpiar plano",command=clear_S)
bu_clf.pack()

plt.figure(figsize=(8,6))
plt.ion()
plt.show()

window.mainloop()