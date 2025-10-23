import sympy as sp
from sympy import *
import random
import math

class Main():
    def __init__(self):
        self.n = 0
        self.min = 0
        self.max = 0
        self.runs = 0

    def Start(self):
        self.n = int(input("What nxn matrix would you like?\n"))
        self.min = int(input("What is the lower bound for the elements value?\n"))
        self.max = int(input("What is the upper bound for the elements value?\n"))
        self.NumOfTests()
        c=self.runs
        P=MtrxPrt()
        while c != 0:
            P.RndMtrx(self.n,self.min,self.max)
            if P.CheckDet() == True:
                P.Tally()
            c-=1
        print("Total invertable matrices = ",P.GetTally(),"\nout of a total of ",self.runs,""
        "\n giving a total percentage of invertable ",self.n,"*",self.n," matrices ranging from ",self.min,"-",self.max," ",
        (P.GetTally()/float(self.runs))*100,"%")
        self.Start()
    
    def NumOfTests(self):
        rng=Abs(self.max-self.min)+1
        ttl=(rng)**((self.n)**2)
        if ttl>=10000:
            self.runs = math.ceil(0.1*ttl)
        elif ttl>=1000:
            self.runs = math.ceil(0.5*ttl)
        else:
            self.runs = ttl
        self.runs = ttl

class MtrxPrt():
    def __init__(self):
        self.count = 0
        self.mtrx = None
        self.invrtmtrx = None
        self.lstOFmtrx = []

    def CheckDet(self):
        if self.mtrx.det() != 0:
            return(True)
        else:
            return(False)
    
    def Det(self):
        return(self.mtrx.det())

    def Invrt(self):
        if self.CheckDet() == True:
            self.invrtmtrx=self.mtrx.inv()
        else:
            self.invrtmtrx="Not invertable"

    def Eignvls(self):
        return(self.mtrx.eigenvals())
    
    def Tally(self):
        self.count+=1
    def GetTally(self):
        return(self.count)

    def RndMtrx(self,n,a,b):
        mtrx=Matrix([[random.randint(a,b) for i in range(n)] for j in range(n)])
        if mtrx in self.lstOFmtrx:
            self.RndMtrx(n,a,b)
        else:
            self.lstOFmtrx.append(mtrx)
            self.mtrx=mtrx
    def CrtMtrx(self,n):
        mtrx=Matrix([[int(input("Row entry "+str(i)+" Column entry "+str(j)+"\n")) for i in range(n)] for j in range(n)])
        self.mtrx=mtrx
        min=None
        max=None
        for i in mtrx:
            if min==None:
                min=i
            elif i<min:
                min=i
            else:
                min=min
        for i in mtrx:
            if max==None:
                max=i
            elif i>max:
                max=i
            else:
                max=max
        return(min,max)
    def GetMtrx(self):
        return(self.mtrx)
    def GetInvrtMtrx(self):
        return(self.invrtmtrx)

class Graph():
    def __init__(self):
        None
    
    

Main().Start()
