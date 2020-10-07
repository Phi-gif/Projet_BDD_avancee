#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:14:51 2020

@author: elvinagovendasamy
"""

# =============================================================================
# Question 2
# =============================================================================
import random


class Functions():
    def __init__(self):
        pass
        
    def read_file(self):
        f=open('liste_fonctions.txt','r')
        instruction_list=[]
        for lines in f:
            instruction_list.append(lines.strip('\n'))
        f.close()
        return instruction_list
        
  
    def run_functions(self):
        
        chosen_function=random.choice(Functions.read_file(self))
        value=eval(chosen_function)
        return (chosen_function,value)
        
                    


if __name__=='__main__':
    

#    instruction_list=['1+2','2+10','3**2','4+500','3/30']
    
    f=Functions()
    result=f.run_functions()
    print(result)
    


