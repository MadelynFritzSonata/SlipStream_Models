import pandas as pd
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import math

e_val = math.e

slstrdata = pd.read_excel('Math 464/Homework/Capstone Project/Progress 2/SlipStreamData.xlsx', header=None) 

timedata = []
blooddata = []

rowt = 0

for t in range(1,20):
    ti = slstrdata[t]
    if str(ti[rowt]) != 'nan':
        timedata.append(ti[rowt])
    else:
        pass

for t in range(1,20):
    ti = slstrdata[t]
    if str(ti[rowt+1]) != 'nan':
        blooddata.append(ti[rowt+1])
    else:
        pass

#print("Timedata:", timedata)
#print("Blood Data:", blooddata)



ep = 0
if ep != 0:
    timedata1 = timedata[:-ep]
    blooddata1 = blooddata[:-ep]
else:
    timedata1 = timedata
    blooddata1 = blooddata

print(timedata1)
print(blooddata1)

N=len(blooddata1)

c_d = np.ones(N)
c_0 = np.zeros(3)
c = np.concatenate((c_0,c_d), axis=0)
avar1=np.ones((N,1))
avar=avar1
bvar=np.log(np.array(timedata1).reshape(N,1))
cvar1=np.array(timedata1)
cvar=cvar1.reshape(N,1)
E=np.eye(N)
A1=np.concatenate((avar,bvar,cvar,-E),axis=1)
A2=np.concatenate((-avar,-bvar,-cvar,-E),axis=1)
A=np.concatenate((A1,A2),axis=0)
yc=np.log(np.array(blooddata1).reshape(N,1))
b=np.concatenate((yc,-yc),axis=0)

#print(avar)
#print(bvar)
#print(cvar)
#print(b)

#print(c)

bds1 = np.array([(None,None),(None,None),(None,None)])
bds2 = np.array(((None,None), )* (N))
bds = np.concatenate((bds1,bds2), axis=0)
#print(bds)
Amat = pd.DataFrame(A)
Ab = np.concatenate((A,b), axis=1)
Abmat = pd.DataFrame(Ab)
#print(Abmat)

res=opt.linprog(c,A_ub=A,b_ub=b,A_eq=None, b_eq=None, bounds=bds, integrality=0)

print(res['fun'])
print(res['status'])
print(res['x'])

a1 = res['x'][0]
b1 = res['x'][1]
c1 = res['x'][2]

def f(x1):
    return (pow(e_val,a1))*(pow(x1,b1))*pow(e_val,(x1*c1))

def lf(x2):
    return a1+b1*np.log(x2)+(x2)*(c1)

x1 = np.linspace(0,275)
x2 = np.linspace(0,275)

#print(c1)

avgdistance = res['fun']/(len(res['x'])-3)

print(avgdistance)

plt.title("Patient Data Function Comparison")
plt.plot(x1,f(x1),color='green')
plt.scatter(timedata, blooddata)
plt.scatter(timedata1,blooddata1)
plt.xlabel("Time (t)")
plt.ylabel("Blood Concentration")
plt.legend(["Function","Data", "Calculated Points"])
plt.show()