#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:14:51 2020

@author: elvinagovendasamy
"""


# =============================================================================
# Question 2
# =============================================================================

#https://www.tutorialspoint.com/python/python_multithreading.htm

import time
import threading
import random


class Compte(threading.Thread):
    compte=True


    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        last = -1
        while Compte.compte:
            nb = threading.active_count()
            if last!=nb :
                print(f"{nb} tâche(s) active(s)")
            last = nb
            

class Functions(threading.Thread):

    # création de 2 verrous globaux
    mon_verrou=threading.Lock()
    mon_verrou1=threading.Lock()
    instruction_list=[] # liste globale
    dico={} # dictionnaire global



    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n=n



    def run(self):
        for i in range(len(Functions.instruction_list)):
            Functions.mon_verrou.acquire() # premier verrou
            chosen_function=Functions.instruction_list[i]
            Functions.mon_verrou.release()
            
            #if chosen_function != None: à valider si c'est nécessaire
            try:
                result=eval(chosen_function)
                Functions.mon_verrou1.acquire() # deuxieme verrou
                Functions.dico[chosen_function]=(result,self.n)
                Functions.mon_verrou1.release()
                
            except Exception as e:
                Functions.mon_verrou1.acquire() 
                Functions.dico[chosen_function]=(e,self.n)
                Functions.mon_verrou1.release()

    

if __name__=='__main__':

    count_=Compte()
    count_.start() # on commence par compter le nombre de tâches

    data=open('liste_fonctionsA.txt','r')
    for lines in data:
        Functions.instruction_list.append(lines.strip('\n'))
    data.close()

    threads_active=[]
    n=3
    for i in range(1,n+1):  # QUESTION: je vais de 0 à n?
        f=Functions(i)
        threads_active.append(f) # On ajoute les threads dans une liste
    for thread in threads_active: 
        thread.start()
    for thread in threads_active:
        thread.join()
    
    
    for items in Functions.dico.keys():
        print(f"Résultat de l'expression {items} = {Functions.dico[items][0]}, le numéro du processeur est {Functions.dico[items][1]}, Thread {threading.current_thread().name} a un ID: {threading.current_thread().ident}")

    print(f"Nombre d'instructions évaluées: {len(Functions.dico)}")
    
  

# QUESTIONS:
# 1. Problème : j'affiche le dernier processeur, et le dernier ID voir comment je peux arranger cela.

# AMELIORATION:
# Voir si on met input pour le n
