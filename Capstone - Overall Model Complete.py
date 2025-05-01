import pandas as pd
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import math

e_val = math.e

slstrdata = pd.read_excel('Math 464/Homework/Capstone Project/Progress 2/SlipStreamData.xlsx', header=None) 

def matcreator(p):

    timedata = []
    blooddata = []

    rowt = 2*p

    for t in range(1,21):
        ti = slstrdata[t]
        if str(ti[rowt]) != 'nan':
            timedata.append(ti[rowt])
        else:
            pass

    for t in range(1,21):
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

    N=len(blooddata1)

    c_d = np.ones(N)
    c_0 = np.zeros(3)
    c_01 = np.zeros(20-N)
    c = np.concatenate((c_0,c_d,c_01), axis=0)
    avar1=np.ones((N,1))
    avar=avar1
    bvar=np.log(np.array(timedata1).reshape(N,1))
    cvar1=np.array(timedata1)
    cvar=cvar1.reshape(N,1)
    E=np.eye(N)
    A01=np.concatenate((avar,bvar,cvar),axis=1)
    A02=np.concatenate((-avar,-bvar,-cvar),axis=1)
    A0=np.concatenate((A01,A02), axis=0)
    A1=-E
    A2=-E
    A=np.concatenate((A1,A2),axis=0)
    yc=np.log(np.array(blooddata1).reshape(N,1))
    b=np.concatenate((yc,-yc),axis=0)
    Ab = np.concatenate((A,b), axis=1)
    Abmat = pd.DataFrame(Ab)

    bds = np.array(((None,None), )* (N))

    return Abmat, c, A, b, c_d, bds, A0

Overalla = []
Overalla0 = []
Overallc = []
Overallb = []
OverallABC = []

for a00 in range(0,20):
    Overabc=matcreator(a00)[6]
    OverallABC.append(Overabc)


for i in range(0,20):
    Overa = matcreator(i)[2]
    Overalla.append(Overa)

for j in range(0,20):
    Overa0 = np.zeros(np.shape(Overalla[j]))
    Overalla0.append(Overa0)

for o in range(0,20):
    co = matcreator(o)[4]
    Overallc.append(co)

for yb in range(0,20):
    b0 = matcreator(yb)[3] 
    Overallb.append(b0)

def colcreate():
    fullb=np.concatenate((Overallb[0],Overallb[1],Overallb[2],Overallb[3],Overallb[4],Overallb[5],Overallb[6],Overallb[7],Overallb[8],
                          Overallb[9],Overallb[10],Overallb[11],Overallb[12],Overallb[13],Overallb[14],Overallb[15],Overallb[16],Overallb[17],
                          Overallb[18],Overallb[19]), axis=0)

    col1 = np.concatenate((Overalla[0],np.zeros((2*len(Overalla0[0][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[2][0]))), np.zeros((2*len(Overalla0[0][0]),len(Overalla0[3][0]))), 
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[0][0]),len(Overalla0[5][0]))), 
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[0][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[0][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[0][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[12][0]))),np.zeros((2*len(Overalla0[0][0]),len(Overalla0[13][0]))),
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[14][0]))),np.zeros((2*len(Overalla0[0][0]),len(Overalla0[15][0]))),
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[16][0]))),np.zeros((2*len(Overalla0[0][0]),len(Overalla0[17][0]))),
    np.zeros((2*len(Overalla0[0][0]),len(Overalla0[18][0]))),np.zeros((2*len(Overalla0[0][0]),len(Overalla0[19][0])))), axis=1) 


    col2 = np.concatenate((np.zeros((2*len(Overalla0[1][0]),len(Overalla0[0][0]))), Overalla[1],
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[4][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[6][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[8][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[12][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[13][0]))),
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[14][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[15][0]))),
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[16][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[17][0]))),
    np.zeros((2*len(Overalla0[1][0]),len(Overalla0[18][0]))),np.zeros((2*len(Overalla0[1][0]),len(Overalla0[19][0])))), axis=1) 

    col3 = np.concatenate((np.zeros((2*len(Overalla0[2][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[2][0]),len(Overalla0[1][0]))),
    Overalla[2],np.zeros((2*len(Overalla0[2][0]),len(Overalla0[3][0]))),np.zeros((2*len(Overalla0[2][0]),len(Overalla0[4][0]))), 
    np.zeros((2*len(Overalla0[2][0]),len(Overalla0[5][0]))),np.zeros((2*len(Overalla0[2][0]),len(Overalla0[6][0]))),
    np.zeros((2*len(Overalla0[2][0]),len(Overalla0[7][0]))), np.zeros((2*len(Overalla0[2][0]),len(Overalla0[8][0]))),
    np.zeros((2*len(Overalla0[2][0]),len(Overalla0[9][0]))), np.zeros((2*len(Overalla0[2][0]),len(Overalla0[10][0]))),
    np.zeros((2*len(Overalla0[2][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[2][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[2][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[2][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[2][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[2][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[2][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[2][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[2][0]),len(Overalla0[19][0])))), axis=1) 

    col4 = np.concatenate((np.zeros((2*len(Overalla0[3][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[3][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[2][0]))),Overalla[3],np.zeros((2*len(Overalla0[3][0]),len(Overalla0[4][0]))), 
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[5][0]))),np.zeros((2*len(Overalla0[3][0]),len(Overalla0[6][0]))),
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[7][0]))), np.zeros((2*len(Overalla0[3][0]),len(Overalla0[8][0]))),
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[9][0]))), np.zeros((2*len(Overalla0[3][0]),len(Overalla0[10][0]))),
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[3][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[3][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[3][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[3][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[3][0]),len(Overalla0[19][0])))), axis=1) 

    col5 = np.concatenate((np.zeros((2*len(Overalla0[4][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[4][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[4][0]),len(Overalla0[3][0]))), Overalla[4], 
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[5][0]))),np.zeros((2*len(Overalla0[4][0]),len(Overalla0[6][0]))),
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[7][0]))), np.zeros((2*len(Overalla0[4][0]),len(Overalla0[8][0]))),
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[9][0]))), np.zeros((2*len(Overalla0[4][0]),len(Overalla0[10][0]))),
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[4][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[4][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[4][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[4][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[4][0]),len(Overalla0[19][0])))), axis=1)   

    col6 = np.concatenate((np.zeros((2*len(Overalla0[5][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[5][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[5][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[4][0]))), Overalla[5], np.zeros((2*len(Overalla0[5][0]),len(Overalla0[6][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[7][0]))), np.zeros((2*len(Overalla0[5][0]),len(Overalla0[8][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[9][0]))), np.zeros((2*len(Overalla0[5][0]),len(Overalla0[10][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[5][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[5][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[5][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[5][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[5][0]),len(Overalla0[19][0])))), axis=1)    

    col7 = np.concatenate((np.zeros((2*len(Overalla0[6][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[6][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[6][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[6][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[6][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[6][0]),len(Overalla0[5][0]))),
    Overalla[6], np.zeros((2*len(Overalla0[6][0]),len(Overalla0[7][0]))),np.zeros((2*len(Overalla0[6][0]),len(Overalla0[8][0]))),
    np.zeros((2*len(Overalla0[6][0]),len(Overalla0[9][0]))), np.zeros((2*len(Overalla0[6][0]),len(Overalla0[10][0]))),
    np.zeros((2*len(Overalla0[6][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[6][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[6][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[6][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[6][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[6][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[6][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[6][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[6][0]),len(Overalla0[19][0])))), axis=1)    

    col8 = np.concatenate((np.zeros((2*len(Overalla0[7][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[7][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[7][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[7][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[6][0]))),Overalla[7], np.zeros((2*len(Overalla0[7][0]),len(Overalla0[8][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[9][0]))),np.zeros((2*len(Overalla0[7][0]),len(Overalla0[10][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[7][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[7][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[7][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[7][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[7][0]),len(Overalla0[19][0])))), axis=1)

    col9 = np.concatenate((np.zeros((2*len(Overalla0[8][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[8][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[8][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[8][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[8][0]),len(Overalla0[7][0]))),Overalla[8],
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[9][0]))), np.zeros((2*len(Overalla0[8][0]),len(Overalla0[10][0]))),
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[8][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[8][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[8][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[8][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[8][0]),len(Overalla0[19][0])))), axis=1)

    col10 = np.concatenate((np.zeros((2*len(Overalla0[9][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[9][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[9][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[9][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[9][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[8][0]))),Overalla[9], np.zeros((2*len(Overalla0[9][0]),len(Overalla0[10][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[9][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[9][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[9][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[9][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[9][0]),len(Overalla0[19][0])))), axis=1) 

    col11 = np.concatenate((np.zeros((2*len(Overalla0[10][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[10][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[10][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[10][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[10][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[10][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[10][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[10][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[10][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[10][0]),len(Overalla0[9][0]))),
    Overalla[10],np.zeros((2*len(Overalla0[10][0]),len(Overalla0[11][0]))),np.zeros((2*len(Overalla0[10][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[10][0]),len(Overalla0[13][0]))),np.zeros((2*len(Overalla0[10][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[10][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[10][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[10][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[10][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[10][0]),len(Overalla0[19][0])))), axis=1)   

    col12 = np.concatenate((np.zeros((2*len(Overalla0[11][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[11][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[11][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[11][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[11][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[11][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[10][0]))),Overalla[11], np.zeros((2*len(Overalla0[11][0]),len(Overalla0[12][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[13][0]))), np.zeros((2*len(Overalla0[11][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[11][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[11][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[11][0]),len(Overalla0[19][0])))), axis=1)

    col13 = np.concatenate((np.zeros((2*len(Overalla0[12][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[12][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[12][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[12][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[12][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[12][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[12][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[12][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[12][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[12][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[12][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[12][0]),len(Overalla0[11][0]))),
    Overalla[12],np.zeros((2*len(Overalla0[12][0]),len(Overalla0[13][0]))), np.zeros((2*len(Overalla0[12][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[12][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[12][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[12][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[12][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[12][0]),len(Overalla0[19][0])))), axis=1)

    col14 = np.concatenate((np.zeros((2*len(Overalla0[13][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[13][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[13][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[13][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[13][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[13][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[13][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[12][0]))),Overalla[13], np.zeros((2*len(Overalla0[13][0]),len(Overalla0[14][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[13][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[13][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[13][0]),len(Overalla0[19][0])))), axis=1)

    col15 = np.concatenate((np.zeros((2*len(Overalla0[14][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[14][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[14][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[14][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[14][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[14][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[14][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[14][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[14][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[14][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[14][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[14][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[14][0]),len(Overalla0[12][0]))),np.zeros((2*len(Overalla0[14][0]),len(Overalla0[13][0]))),
    Overalla[14],np.zeros((2*len(Overalla0[14][0]),len(Overalla0[15][0]))),np.zeros((2*len(Overalla0[14][0]),len(Overalla0[16][0]))),
    np.zeros((2*len(Overalla0[14][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[14][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[14][0]),len(Overalla0[19][0])))), axis=1)

    col16 = np.concatenate((np.zeros((2*len(Overalla0[15][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[15][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[15][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[15][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[15][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[15][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[15][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[12][0]))),np.zeros((2*len(Overalla0[15][0]),len(Overalla0[13][0]))),
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[14][0]))),Overalla[15],
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[16][0]))),np.zeros((2*len(Overalla0[15][0]),len(Overalla0[17][0]))),
    np.zeros((2*len(Overalla0[15][0]),len(Overalla0[18][0]))),np.zeros((2*len(Overalla0[15][0]),len(Overalla0[19][0])))), axis=1)

    col17 = np.concatenate((np.zeros((2*len(Overalla0[16][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[16][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[16][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[16][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[16][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[16][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[16][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[16][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[16][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[16][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[16][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[16][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[16][0]),len(Overalla0[12][0]))),np.zeros((2*len(Overalla0[16][0]),len(Overalla0[13][0]))),
    np.zeros((2*len(Overalla0[16][0]),len(Overalla0[14][0]))),np.zeros((2*len(Overalla0[16][0]),len(Overalla0[15][0]))),
    Overalla[16],np.zeros((2*len(Overalla0[16][0]),len(Overalla0[17][0]))),np.zeros((2*len(Overalla0[16][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[16][0]),len(Overalla0[19][0])))), axis=1) 

    col18 = np.concatenate((np.zeros((2*len(Overalla0[17][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[17][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[17][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[17][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[17][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[17][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[17][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[12][0]))),np.zeros((2*len(Overalla0[17][0]),len(Overalla0[13][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[14][0]))),np.zeros((2*len(Overalla0[17][0]),len(Overalla0[15][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[16][0]))),Overalla[17],np.zeros((2*len(Overalla0[17][0]),len(Overalla0[18][0]))),
    np.zeros((2*len(Overalla0[17][0]),len(Overalla0[19][0])))), axis=1) 

    col19 = np.concatenate((np.zeros((2*len(Overalla0[18][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[18][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[18][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[18][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[18][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[18][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[18][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[18][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[18][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[18][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[18][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[18][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[18][0]),len(Overalla0[12][0]))),np.zeros((2*len(Overalla0[18][0]),len(Overalla0[13][0]))),
    np.zeros((2*len(Overalla0[18][0]),len(Overalla0[14][0]))),np.zeros((2*len(Overalla0[18][0]),len(Overalla0[15][0]))),
    np.zeros((2*len(Overalla0[18][0]),len(Overalla0[16][0]))),np.zeros((2*len(Overalla0[18][0]),len(Overalla0[17][0]))),
    Overalla[18],np.zeros((2*len(Overalla0[18][0]),len(Overalla0[19][0])))), axis=1) 

    col20 = np.concatenate((np.zeros((2*len(Overalla0[19][0]),len(Overalla0[0][0]))),np.zeros((2*len(Overalla0[19][0]),len(Overalla0[1][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[2][0]))),np.zeros((2*len(Overalla0[19][0]),len(Overalla0[3][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[4][0]))), np.zeros((2*len(Overalla0[19][0]),len(Overalla0[5][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[6][0]))), np.zeros((2*len(Overalla0[19][0]),len(Overalla0[7][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[8][0]))), np.zeros((2*len(Overalla0[19][0]),len(Overalla0[9][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[10][0]))),np.zeros((2*len(Overalla0[19][0]),len(Overalla0[11][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[12][0]))),np.zeros((2*len(Overalla0[19][0]),len(Overalla0[13][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[14][0]))),np.zeros((2*len(Overalla0[19][0]),len(Overalla0[15][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[16][0]))),np.zeros((2*len(Overalla0[19][0]),len(Overalla0[17][0]))),
    np.zeros((2*len(Overalla0[19][0]),len(Overalla0[18][0]))),Overalla[19]), axis=1)

    fullr1=np.concatenate((OverallABC[0],col1), axis=1)

    fullr2=np.concatenate((OverallABC[1],col2), axis=1)

    fullr3=np.concatenate((OverallABC[2],col3), axis=1)

    fullr4=np.concatenate((OverallABC[3],col4), axis=1)

    fullr5=np.concatenate((OverallABC[4],col5), axis=1)

    fullr6=np.concatenate((OverallABC[5],col6), axis=1)

    fullr7=np.concatenate((OverallABC[6],col7), axis=1)

    fullr8=np.concatenate((OverallABC[7],col8), axis=1)

    fullr9=np.concatenate((OverallABC[8],col9), axis=1)
    
    fullr10=np.concatenate((OverallABC[9],col10), axis=1)

    fullr11=np.concatenate((OverallABC[10],col11), axis=1)

    fullr12=np.concatenate((OverallABC[11],col12), axis=1)

    fullr13=np.concatenate((OverallABC[12],col13), axis=1)

    fullr14=np.concatenate((OverallABC[13],col14), axis=1)

    fullr15=np.concatenate((OverallABC[14],col15), axis=1)

    fullr16=np.concatenate((OverallABC[15],col16), axis=1)

    fullr17=np.concatenate((OverallABC[16],col17), axis=1)

    fullr18=np.concatenate((OverallABC[17],col18), axis=1)

    fullr19=np.concatenate((OverallABC[18],col19), axis=1)

    fullr20=np.concatenate((OverallABC[19],col20), axis=1)

    FullAmatrix = np.concatenate((fullr1, fullr2, fullr3, fullr4, fullr5, fullr6, fullr7, fullr8, fullr9, fullr10, fullr11, fullr12, 
                                  fullr13, fullr14, fullr15, fullr16, fullr17, fullr18, fullr19, fullr20), axis=0)

    return FullAmatrix, fullb

print(np.shape(colcreate()[0]))

FullAMatrix = colcreate()[0]

FullN=np.shape(colcreate()[0])
Fullbounds=[]

for fb in range(0,FullN[1]):
    fullbnd = (None, None)
    Fullbounds.append(fullbnd)

FullB=colcreate()[1]

FullBounds=np.array(Fullbounds)
#FullAMatrix=colcreate()[0]

#print(np.shape(FullAMatrix))

cfabc=np.zeros(3)
cdlta=np.ones(FullN[1]-3)
cfull=np.concatenate((cfabc,cdlta),axis=0)

print(np.shape(cfull))

res=opt.linprog(cfull,A_ub=FullAMatrix,b_ub=FullB, A_eq=None, b_eq=None, bounds=FullBounds, integrality=0)

print(res['fun'])
print(res['status'])
print(res['x'])

print(res['fun']/(len(res['x'])-3))

print(len(res['x']))

a1 = res['x'][0]
b1 = res['x'][1]
c1 = res['x'][2]

def datapoint(n):
    rowt=2*n
    timedata2=[]
    blooddata2=[]
    for t in range(1,21):
        ti = slstrdata[t]
        if str(ti[rowt]) != 'nan':
            timedata2.append(ti[rowt])
        else:
            pass

    for t in range(1,21):
        ti = slstrdata[t]
        if str(ti[rowt+1]) != 'nan':
            blooddata2.append(ti[rowt+1])
        else:
            pass
    return timedata2, blooddata2

def f(x1):
    return (pow(e_val,a1))*(pow(x1,b1))*pow(e_val,(x1*c1))

x1 = np.linspace(0,275)

Calculationdata = []


plt.title("Patient Data Function Comparison")
plt.plot(x1,f(x1),color='green')
plt.scatter(datapoint(0)[0], datapoint(0)[1])
plt.scatter(datapoint(4)[0], datapoint(4)[1])
plt.scatter(datapoint(9)[0], datapoint(9)[1])
plt.scatter(datapoint(14)[0], datapoint(14)[1])
plt.scatter(datapoint(19)[0], datapoint(19)[1])
#plt.scatter(timedata1,blooddata1)
plt.xlabel("Time (t)")
plt.ylabel("Blood Concentration")
plt.legend(["Function","Patient 1 Data","Patient 5 Data","Patient 10 Data","Patient 15 Data","Patient 20 Data"])
plt.show()