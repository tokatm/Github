import numpy as np
from sympy import prem
from sympy.abc import x

power1 = int(input('Power1: '))
power2 = int(input('Power2: '))
range1 = int(input('Range1: '))
range2 = int(input('Range2: '))

def primitiveTest():
   
    for i in range(range1,range2):
        
        m = ((prem (x**i + 1, x**power1 + x**power2 + 1, modulus = 2) == 0) and i == 2**power1 - 1)

        if m == True :
 
            print(i)

        else:
            i + 1
            print('Not Primitive')
       

primitiveTest()





