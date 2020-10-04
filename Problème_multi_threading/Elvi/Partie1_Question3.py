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
    def __init__(self,x):
        self.x=x
        
    def __dir__(self):
        return['f1','f2','f3']
    
    def f1(self):
        return (self.x+3)/2 
    
    
    def f2(self):
        return self.x 
    
    def f3(self):            
        return self.x+5 
    
#    def f4(self):
#        try:
#            result4=100/self.x
#        except ZeroDivisionError:
#            print('Division par zéro! Essayer à nouveau')
#        else:
#            return result4
  
    def random_function(self,instructions):
        
# Working test from list
# =============================================================================
#         my_functs=[self.f1,self.f2]  
#         result=random.choice(my_functs)()
#         return result
# =============================================================================
# Generalization:
        values=[self.f1(),self.f2(),self.f3()]
        keys=[i for i in dir(Functions(self.x)) if not i.startswith("__")] #ok
        init_dico=dict(zip(keys,values))
        
        liste_f=[]
        for item in instructions:
            if item in init_dico:
                liste_f.append([item,init_dico[item]])
                
        return random.choice(liste_f)
            

class ValueNotInRange(Exception):
    """Raised when the input value is too small"""
    def __init__(self,number,message="La valeur doit être supérieur à 0 et inférieur à 100"):
        self.number=number
        self.message=message
        super().__init__(self.message)



if __name__=='__main__':

    
    number=int(input("Entrez une valeur: "))
    
    if not 0<number<100:
        raise ValueNotInRange(number)
    else:
        myFunction=Functions(number)
        f=open('liste_fonctions.txt','r')
        instruction_list=[]
        for lines in f:
            instruction_list.append(lines.strip('\n'))
        f.close()

        my_result=myFunction.random_function(instruction_list)
        print('la fonction et sa valeur sont : ',my_result)
    



