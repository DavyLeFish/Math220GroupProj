import sympy as sp
from sympy import *
import random
import math
import itertools

class Main():
    def __init__(self):
        self.n = 0
        self.min = 0
        self.max = 0
        self.rng = 0
        self.ttl = 0
        self.runs = 0

    def Start(self):
        choice = int(input("Enter 1 for specific matrix, 2 for random matrix:\n"))
        if choice == 1:
            self.SpcfcMtrx()
        elif choice == 2:
            self.RndMtrx()
        else:
            self.Start()

#Sepcific Matrix options
    def SpcfcMtrx(self):
        mtrx = [[int(input("Row entry "+str(i)+" Column entry "+str(j)+"\n")) for i in range(self.n)] for j in range(self.n)]
        choice = int(input("Enter 1"))
        
#Random Martrix options
    def RndMtrx(self):
        choice = int(input("Enter 0 to return to start, 1 for total invertable matrices, 2 for total eigenvalues, :\n"))
        if choice == 0:
            self.Start()
        elif choice == 1:
            self.NumOfInvrts()
        elif choice == 2:
            self.DstnctEignvls()
        else:
            self.RndMtrx()

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
#Runs through the set amount of runs
        c=self.runs
        while c != 0:
            print("Runs left: ",c)
#Calls function to create random matrix and checks it hasn't already been tested
            P.RndMtrx(self.n,self.min,self.max)
            while P.CheckMtrx() == False:
                P.RndMtrx(self.n,self.min,self.max)
    #Checks if the matrix has a non-zero determinant and adds 1 to the counter
            if P.CheckDet() == True:
                P.Tally(1)
            c-=1
#Final result
        print("Total invertable matrices = ",P.GetTally(),"\nout of a total of ",self.runs,""
        "\n giving a total percentage of invertable ",self.n,"*",self.n," matrices ranging from ",self.min,"-",self.max," ",
        (P.GetTally()/float(self.runs))*100,"%")
#Loops back to beggning
        self.RndMtrx()

#Finds total matrices which have distinct eigenvalues
    def DstnctEignvls(self):
        P = MtrxPrt()
#User inputs for desired random matrix
        self.n = int(input("What nxn matrix would you like?\n"))
        self.min = int(input("What is the lower bound for the elements value?\n"))
        self.max = int(input("What is the upper bound for the elements value?\n"))
        self.NumOfTests()

        for i in range(self.runs):
            P.RndMtrx(self.n,self.min,self.max)
            while P.CheckMtrx() == False:
                P.RndMtrx(self.n,self.min,self.max)
            P.SetMtrx(False)
        matrices = P.GetTested()
        checked = 0
        failures = 0

        for mat in matrices:
            try:
                eigenvals = mat.eigenvals()
            except Exception:
                failures += 1
                continue
            if len(set(eigenvals)) == self.n:
                P.Tally(1)
            checked += 1
            if checked % 5000 == 0 and self.n > 1:
                print(f"Checked {checked} matrices for n={self.n}")

        if checked == 0:
            proportion = float('nan')
        else:
            proportion = P.GetTally() / checked
        print(f"n={self.n}: {P.GetTally()} matrices with {self.n} distinct eigenvalues out of {checked} checked ({proportion:.6f})")
        if failures > 0:
            print(f"Warning: {failures} matrices could not be processed due to eigenvalue computation failures.")
        print('-' * 40)
        
        self.RndMtrx()

    def NumOfTests(self):
#Gets the range of different available values
        self.rng=Abs(self.max-self.min)+1
#Gets total of different possible matrices
        self.ttl=(self.rng)**((self.n)**2)
#Limits the amount of runs
        if self.ttl>=10000:
            self.runs = 10000
        else:
            self.runs = self.ttl

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
    def CheckMtrx(self):
        if self.mtrx in self.lstOFmtrx:
            return False
        else:
            return True
#Adds matrix to the tested list
    def SetMtrx(self,t):
#if t is true then it also includes the transpose of the matrix
            if t == False:
                self.lstOFmtrx.append(self.mtrx)
            elif t == True:
                self.lstOFmtrx.append(self.mtrx.transpose())
#Returns the matrix
    def GetMtrx(self):
        return(self.mtrx)
#Returns tested matrices
    def GetTested(self):
        return(self.lstOFmtrx)
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
        for i in self.mtrx:
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


