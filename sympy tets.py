import sympy as sp
from sympy import *


global x,y,z
x,y,z = symbols('x y z')

#Variables
def Variables():
    eq = x+(2*y)
    print(eq)
    print(x+eq)

    expand_eq=expand(x*eq)
    print(expand_eq)

#Derivitives
def Derivs():
    deriv=diff(sin(x)*exp(x),x) #differentiating with respect to x
    print(deriv)
    f = Function('f')
    derivsol=dsolve(Eq(f(x).diff(x,x)-f(x),exp(f)),f(x))
    print(derivsol)

#Integrals
def Intgrls():
    intg=integrate(sin(x**2),(x, -oo,oo)) #double o makes infinity
    print(intg)

#Limits
def Lims():
    limit(1/x,x,oo)

#Solving Equations
def Solve():
    sol=solve(x**2+2,x) #Solves for x in (x**2)+2=0
    print(sol)

#Eigenvalues
def Eigen():
    M=Matrix([[1,2],[3,4]])#Each imbedded list is a row
    print(M.eigenvals())
#r.r.e
def RRE():
    M=Matrix([[2,5],[1,3]])
    print(M.rref())
# Variables()
# Derivs()
# Intgrls()
# Lims()
# Solve()
# Eigen()
RRE()