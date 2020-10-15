#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:14:51 2020

@author: elvinagovendasamy
"""

# =============================================================================
# Question 2
# =============================================================================
import time
import threading
import random



class Functions(threading.Thread):
    mon_verrou=threading.Lock()
    
    def __init__(self):
        threading.Thread.__init__(self)

       
        
    def read_file(self):
        f=open('liste_fonctionsA.txt','r')
        instruction_list=[]
        for lines in f:
            instruction_list.append(lines.strip('\n'))
        f.close()
        return instruction_list
        
  
    
    def run(self):
        dico={}
        instruction_list=Functions.read_file(self)
        
        
        n=len(instruction_list)

        
        with Functions.mon_verrou:
            print('verrou mis')
            for i in range(n):
                #time.sleep(0.01)
                chosen_function=instruction_list[i]
                dico[chosen_function]=eval(chosen_function)
        return(dico)


if __name__=='__main__':
    
    
    f=Functions()
    instruct=f.read_file()
    
    threads=[]
    
    # on ajoute les threads dans une liste
    for items in instruct:
        t=threading.Thread(target=f.run)
        t.start()
        #print(f'nombre de tâches actives : {threading.active_count}')

        threads.append(t)
    

    for thread in threads:
        thread.join()

    print(f"resultat : {f.run()}")
    
   

