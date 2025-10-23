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
#User inputs for desired random matrix
        self.n = int(input("What nxn matrix would you like?\n"))
        self.min = int(input("What is the lower bound for the elements value?\n"))
        self.max = int(input("What is the upper bound for the elements value?\n"))
#Sends to internal function to get total of runs
        self.NumOfTests()
        c=self.runs
#Opens MtrxPrt class
        P=MtrxPrt()
#Runs through the set amount of runs
        while c != 0:
#Calss function to create random matrix
            P.RndMtrx(self.n,self.min,self.max)
#Checks if the matrix has a non-zero determinant and adds 1 to the counter
            if P.CheckDet() == True:
                P.Tally()
            c-=1
#Final result
        print("Total invertable matrices = ",P.GetTally(),"\nout of a total of ",self.runs,""
        "\n giving a total percentage of invertable ",self.n,"*",self.n," matrices ranging from ",self.min,"-",self.max," ",
        (P.GetTally()/float(self.runs))*100,"%")
#Loops back to beggning
        self.Start()
    
    def NumOfTests(self):
#Gets the range of different available values
        rng=Abs(self.max-self.min)+1
#Gets total of different possible matrices
        ttl=(rng)**((self.n)**2)
#Limits the amount of runs
        if ttl>=10000:
            self.runs = math.ceil(0.1*ttl)
        elif ttl>=1000:
            self.runs = math.ceil(0.5*ttl)
        else:
            self.runs = ttl

class MtrxPrt():
    def __init__(self):
        self.count = 0
        self.mtrx = None
        self.invrtmtrx = None
        self.lstOFmtrx = []
#Checks if the determinant is zero
    def CheckDet(self):
        if self.mtrx.det() != 0:
            return(True)
        else:
            return(False)
#Returns the determinant value
    def Det(self):
        return(self.mtrx.det())
#Produces inverted matrix
    def Invrt(self):
        if self.CheckDet() == True:
            self.invrtmtrx=self.mtrx.inv()
        else:
            self.invrtmtrx="Not invertable"
#Returns eigenvalues
    def Eignvls(self):
        return(self.mtrx.eigenvals())
#Adds one to the tally count    
    def Tally(self):
        self.count+=1
#Returns the tally count
    def GetTally(self):
        return(self.count)

    def RndMtrx(self,n,a,b):
#Produces random matrix based on user inputs
        mtrx=Matrix([[random.randint(a,b) for i in range(n)] for j in range(n)])
#Checks if the random matrix has already be tested
        if mtrx in self.lstOFmtrx:
            self.RndMtrx(n,a,b)
        else:
#Adds matrix to list of tested matrices
            self.lstOFmtrx.append(mtrx)
            self.mtrx=mtrx

    def CrtMtrx(self,n):
#Allows creation of personal matrix
        mtrx=Matrix([[int(input("Row entry "+str(i)+" Column entry "+str(j)+"\n")) for i in range(n)] for j in range(n)])
        self.mtrx=mtrx
        min=None
        max=None
#Finds minimum entry in matrix
        for i in mtrx:
            if min==None:
                min=i
            elif i<min:
                min=i
            else:
                min=min
#Finds maximum entry in matrix
        for i in mtrx:
            if max==None:
                max=i
            elif i>max:
                max=i
            else:
                max=max
        return(min,max)
#Returns the matrix
    def GetMtrx(self):
        return(self.mtrx)
#Returns the inverse matrix
    def GetInvrtMtrx(self):
        return(self.invrtmtrx)

class Graph():
    def __init__(self):
        None
    
    

Main().Start()


