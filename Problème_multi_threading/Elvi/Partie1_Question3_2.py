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
        if 0<self.x<100:
            return (self.x+3)/2 
        else:
            raise ValueNotInRange(number)
    
    def f2(self):
        if 0<self.x<100:  
            return self.x 
        else:
            raise ValueNotInRange(number)
    
    def f3(self):
        if 0<self.x<100:            
            return self.x+5 
        else:
            raise ValueNotInRange(number)
    
    def f4(self):
        if not self.x==0:
            return 100/self.x
        else:
            raise ValueZero(self.x)


  
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
    def __init__(self,number,message="La valeur doit être supérieur à 0 et inférieur à 100"):
        self.number=number
        self.message=message
        super().__init__(self.message)

class ValueZero(Exception):
    def __init__(self,number,message="La valeur ne peut pas être 0"):
        self.number=number
        self.message=message
        super().__init__(self.message)



if __name__=='__main__':

    
    number=int(input("Entrez une valeur: "))

    myFunction=Functions(number)
    f=open('liste_fonctions.txt','r')
    instruction_list=[]
    for lines in f:
        instruction_list.append(lines.strip('\n'))
    f.close()

    my_result=myFunction.random_function(instruction_list)
    print('la fonction et sa valeur sont : ',my_result)




