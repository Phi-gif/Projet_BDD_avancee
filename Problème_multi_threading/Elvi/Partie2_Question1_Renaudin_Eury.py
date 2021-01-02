#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:14:51 2020

@author: elvinagovendasamy
"""


# =============================================================================
# Question 1
# =============================================================================

import time
import threading
import random




class Functions(threading.Thread):

    # création de 2 verrous globaux
    mon_verrou=threading.Lock()
    mon_verrou1=threading.Lock()
    instruction_list=[] # liste globale
    dico={} # dictionnaire global

    def __init__(self,numero_processeur):
        threading.Thread.__init__(self)
        self.numero_processeur=numero_processeur

    def run(self):
        for i in range(len(Functions.instruction_list)):
            Functions.mon_verrou.acquire() # premier verrou
            if len(Functions.instruction_list)!=0:
                chosen_function=Functions.instruction_list[i]
                #print(chosen_function)
            Functions.mon_verrou.release()
            
            if chosen_function != None:
                try:
                    result=eval(chosen_function)
                    Functions.mon_verrou1.acquire() # deuxieme verrou
                    Functions.dico[chosen_function]=(result,self.numero_processeur)
                    print(f"Thread {threading.current_thread().name} a un ID: {threading.current_thread().ident}")
                    #print(Functions.dico.keys())
                    Functions.mon_verrou1.release()
                
                except Exception as e:
                    Functions.dico[chosen_function]=(e,self.numero_processeur)
            
    

if __name__=='__main__':

    data=open('liste_fonctions.txt','r')
    for lines in data:
        Functions.instruction_list.append(lines.strip('\n'))
    data.close()

    threads_active=[]
    n=8
    for i in range(1,n+1):  
        f=Functions(i)
        threads_active.append(f) # On ajoute les threads dans une liste
    for thread in threads_active: 
        thread.start()
    for thread in threads_active:
        thread.join()
    
    
    for items in Functions.dico.keys():
        print(f"Résultat de l'expression {items} = {Functions.dico[items][0]}, le numéro du processeur est {Functions.dico[items][1]}")


    print(f"Nombre d'instructions évaluées: {len(Functions.dico)}")
    print('End')
    
