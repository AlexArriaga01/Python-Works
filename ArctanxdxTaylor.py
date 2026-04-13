import pandas as pd

MS=0
LS=[0]
Le=[1]
for i in range(5):
    MS=MS+(((-1)**i)*(-0.25)**(2*i))
    LS.append(MS)
    e=(LS[i+1]-LS[i])/(LS[i+1])
    Le.append(e)
D={
    "f(-0.25)":LS,
    "Error":Le
}
df=pd.DataFrame(D)
print(df.iloc[1:5][:])