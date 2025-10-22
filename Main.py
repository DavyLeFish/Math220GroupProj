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
        choice = int(input("1 for set matrix. 2 for random matrix\n"))
        self.n = int(input("What nxn matrix would you like?\n"))
        if choice == 1:
            self.min,self.max=MtrxPrt().CrtMtrx(self.n)
        elif choice == 2:
            self.min = int(input("What is the lower bound for the elements value?\n"))
            self.max = int(input("What is the upper bound for the elements value?\n"))
        else:
            self.Start()
        self.NumOfTests()
        c=self.runs
        while c != 0:
            P=MtrxPrt()
            P.RndMtrx(self.n,self.min,self.max)
            if P.CheckDet() == True:
                P.Tally()
            c-=1
        print("Total invertable matrices = ",P.GetTally(),"\nout of a total of ",self.runs,""
        "\n giving a total percentage of invertable ",self.n,"*",self.n," matrices ranging from ",self.min,"-",self.max," ",
        (P.GetTally()/self.runs),"%")
    
    def NumOfTests(self):
        rng=Abs(self.max-self.min)+1
        ttl=(rng)**((self.n)**2)
        if ttl>= 1000:
            self.runs = math.ceil(0.1*ttl)
        elif ttl>=30:
            self.runs = math.ceil(0.5*ttl)
        else:
            self.runs = ttl

class MtrxPrt():
    def __init__(self):
        self.count = 0
        self.mtrx = None
        self.invrtmtrx = None

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


Main().Start()

