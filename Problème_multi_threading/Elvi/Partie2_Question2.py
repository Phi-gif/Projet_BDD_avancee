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



class Functions(threading.Thread):
    mon_verrou=threading.Lock()
    count=0
    
    def __init__(self):
        threading.Thread.__init__(self)

       
        
    def read_file(self):
        f=open('liste_fonctions.txt','r')
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
            #print('verrou mis')
            for i in range(n):
                #time.sleep(0.01)
                chosen_function=instruction_list[i]
                try:
                    dico[chosen_function]=eval(chosen_function)
                except Exception as e:
                    dico[chosen_function]=e
                Functions.count+=1
                print(f'{Functions.count}: Thread {threading.current_thread().name} has ID: {threading.current_thread().ident} ')
                
                
        return dico


if __name__=='__main__':
    
    
    f=Functions()
    instruct=f.read_file()
    
    threads=[]
    
    # on ajoute les threads dans une liste
    for items in range(20):
        t=threading.Thread(target=f.run)
        # to return number of threads that are active
        print(f'nombre de tâches actives : {threading.active_count()}') #
        threads.append(t)
        t.start()
        

    for thread in threads:
        thread.join()

    print(f"resultat : {f.run()}")
    print ("fin")
   

