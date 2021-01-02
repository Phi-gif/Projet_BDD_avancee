#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:14:51 2020

@author: elvinagovendasamy
"""

# =============================================================================
# Question 3
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
        dico={}
        instruction_list=Functions.read_file(self)
        # Ici nous faisons à nouveau un shuffle mais pas nécessaire
        random.shuffle(instruction_list)
       
        n=len(instruction_list)
        for i in range(n):
            chosen_function=instruction_list[i]
            try:
                dico[chosen_function]=eval(chosen_function)
            except Exception as e:
                dico[chosen_function]=e

        return dico
            



if __name__=='__main__':

    f=Functions()
    result=f.run_functions()

    print(result)




