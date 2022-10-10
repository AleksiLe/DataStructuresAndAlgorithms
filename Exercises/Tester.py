import math
from tkinter import Y
from sympy import symbols, solve
def laskuri():

    return
n=45
#print(0.5*n**2)print(22*n)print(10*n*math.log2(n))print(1.3**n)
n = symbols('n')
expr = n*math.log2(n)-1
sol = solve(expr)
sol

