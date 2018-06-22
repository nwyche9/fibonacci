# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:45:45 2018

@author: natew
"""

def fib_sequence(n):

    a = 1
    b = 1

    for x in range(n):
	    yield a 
	    a,b = b, a+b

print(list(fib_sequence(40)))








    
    

