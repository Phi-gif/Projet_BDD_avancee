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



class Count(threading.Thread):
    count=True

    def __init__(self):
        threading.Thread.__init__(self)

    # pris de ce qui a été fait en classe
    # on utilise cette fonction pour connaitre le nombre de pages active
    def run_count(self):
        last = -1
        while Count.count:
            nb = threading.active_count()
        if last!=nb :
            print(f"{nb} tâche(s) active(s)")
            last = nb


class Functions(threading.Thread):

    # création de 2 verrous globaux
    verrou1=threading.Lock()
    verrou2=threading.Lock()

    instruction_list=[] # liste globale
    dico={} # dictionnaire global

    def __init__(self,num_processeur):
        threading.Thread.__init__(self)
        self.num_processeur=num_processeur # pour connaitre le nombre de processeurs


    def run(self):
        n=len(Functions.instruction_list)
        for i in range(n):
            chosen_function=Functions.instruction_list[i]

            try: 
                Functions.verrou2.acquire()
                Functions.dico[chosen_function]=(eval(chosen_function),self.num_processeur)
                Functions.verrou2.release()
            except Exception as e:
                Functions.verrou2.acquire()
                Functions.dico[chosen_function]=(f"{e.__class__.__name__} : {e}",self.num_processeur)
                Functions.verrou2.release()


    # def run(self):
    #     f=open('liste_fonctions.txt','r')
    #     instruction_list=[]
    #     for lines in f:
    #         instruction_list.append(lines.strip('\n'))
    #     f.close()

    #     dico={}

    #     n=len(instruction_list)
        
    #     for i in range(n):

    #         chosen_function=instruction_list[i]

    
    #         try:
    #             Functions.mon_verrou2.acquire() # je met mon evaluation dans la fonction
    #             dico[chosen_function]=eval(chosen_function)
    #             print('numero_processeur : ', self.num_processeur)
    #             Functions.mon_verrou2.release()
    #         except Exception as e:
    #             Functions.mon_verrou2.acquire()
    #             dico[chosen_function]=e
    #             Functions.mon_verrou2.release()
    #         Functions.count+=1
    #         print(f'{Functions.count}: Thread {threading.current_thread().name} has ID: {threading.current_thread().ident} ')
   
    #    return dico


if __name__=='__main__':
    
    data=open('liste_fonctions.txt','r')
    for lines in data:
        Functions.instruction_list.append(lines.strip('\n'))
    data.close()

    threads_active=[]
    n=5
    # on ajoute les threads dans une liste
    for i in range(n):
        f=Functions(i)
        #t=threading.Thread(target=f.run)
        threads_active.append(f)
   
    for thread in threads_active:
        thread.start()

    for thread in threads_active:
        thread.join()

    print(f"resultat : {f.run()}")
    print ("fin")
   

    for instruct in Functions.dico.keys():
        print(f"eval({instruct})={Functions.dico[instruct][0]}, processeur = ")

    
    print(Functions.dico.items())