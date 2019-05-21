# -*- coding: utf-8 -*-

import numpy as np
m= np.matrix([[0,1],[1,1]])

def matrixExp(n,mod): 
    if n==1:
        return m
    
    elif n%2==0:
        result= matrixExp(n/2,mod)
        result=result%mod
        return result**2
    
    else:
        return matrixExp(n-1,mod)*m%mod

     
print("mod:",matrixExp(10**10,4)[0,1])