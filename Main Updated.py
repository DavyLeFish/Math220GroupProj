import sympy as sp
from sympy import *
import random
import math

class Main():
    def __init__(self):
        self.n = 0
        self.min = 0
        self.max = 0
        self.rng = 0
        self.runs = 0

    def Start(self):
        choice = int(input("Enter 1 for specific matrix, 2 for random matrix:\n")
        if choice == 1:
            self.SpcfcMtrx()
        elif choice == 2:
            self.RndMtrx()
        else:
            self.Start()

#Sepcific Matrix options
    def SpcfcMtrx(self):
        mtrx = [[int(input("Row entry "+str(i)+" Column entry "+str(j)+"\n")) for i in range(n)] for j in range(n)]
        choice = int(input("Enter 1"))
        
#Random Martrix options
    def RndMtrx(self):
        choice = int(input("Enter 0 to return to start, 1 for total invertable matrices, 2 for total eigenvalues, :\n"))
        if choice == 0:
            self.Start()
        elif choice == 1:
            self.NumOfInvrts()
        else:
            Self.RndMtrx()

#Finds how many invertable matrices exist within the givin parameters
#To make it more optimised, finds symetries that will have determinate of zero
    def NumOfInvrts(self):
#Opens MtrxPrt class
        P=MtrxPrt()
#User inputs for desired random matrix
        self.n = int(input("What nxn matrix would you like?\n"))
        self.min = int(input("What is the lower bound for the elements value?\n"))
        self.max = int(input("What is the upper bound for the elements value?\n"))

#Sends to internal function to get total of runs
        self.NumOfTests()
#Finds how many have zero rows and doubles to include zero columns
        zrwscls=2*((self.rng)**((self.n)**2))-((self.rng)**((self.n-1)**n)))
#Finds how many have zero diagonal
        zdgnl=(self.rng)**(((self.n)**2)-self.n)
#Produces affirmentioned matrices if the total of combinations is small enough where the amount of zero rows and columns would be likely to be tested in the random selection
#using a boundary of 5% of the total
        if (zrwscls+zdgnl)/(ttl)<=0.95:
            for j in range(n):
                for i in range((self.rng)**(((self.n)**2)-self.n)):
                    P.RndMtrx()
                    mtrx=P.GetMtrx()
#Runs through the set amount of runs
        c=self.runs
        while c != 0:
#Calls function to create random matrix and checks it hasn't already been tested
            P.RndMtrx(self.n,self.min,self.max)
        while P.CheckMtrx(True) == False:
            P.RndMtrx(self.n,self.min,self.max)
#Checks if the matrix has a non-zero determinant and adds 1 to the counter
            if P.CheckDet() == True:
                P.Tally(2)
            c-=1
#Final result
        print("Total invertable matrices = ",P.GetTally(),"\nout of a total of ",self.runs,""
        "\n giving a total percentage of invertable ",self.n,"*",self.n," matrices ranging from ",self.min,"-",self.max," ",
        (P.GetTally()/float(self.runs))*100,"%")
#Loops back to beggning
        self.RndMtrx()        

    
    def NumOfTests(self):
#Gets the range of different available values
        self.rng=Abs(self.max-self.min)+1
#Gets total of different possible matrices
        ttl=(self.rng)**((self.n)**2)
#Limits the amount of runs
        if ttl>=10000:
            self.runs = 10000
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
    def Tally(self,n):
        self.count+=n
#Returns the tally count
    def GetTally(self):
        return(self.count)
#Allows creation of personal matrix
    def CrtMtrx(self,n,mtrx):
        self.mtrx=Matrix(mtrx)
#Produces random matrix based on user inputs
    def RndMtrx(self,n,a,b):
        self.mtrx=Matrix([[random.randint(a,b) for i in range(n)] for j in range(n)])
#Checks if the random matrix has already be tested
    def CheckMtrx(self,t):
        if self.mtrx in self.lstOFmtrx:
            return False
        else:
#Adds matrix to list of tested matrices
#if t is true then it also includes the transpose of the matrix
            if t == False
                self.lstOFmtrx.append(mtrx)
                self.mtrx=self.mtrx
            elif t == True:
                self.lstOFmtrx.append(self.mtrx.transpose())
            return True

#Returns the matrix
    def GetMtrx(self):
        return(self.mtrx)
#Returns the inverse matrix
    def GetInvrtMtrx(self):
        return(self.invrtmtrx)
#Returns min value of matrix
    def MinMtrx(self):
        for i in self.mtrx:
            if min==None:
                min=i
            elif i<min:
                min=i
            else:
                min=min
#Finds maximum in matrix
    def MaxMtrx(self):
        for i in mtrx:
            if max==None:
                max=i
            elif i>max:
                max=i
            else:
                max=max
        return(min,max)

class Graph():
    def __init__(self):
        None
    
    

Main().Start()



