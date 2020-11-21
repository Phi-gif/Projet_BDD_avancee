#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:10:28 2020

@author: elvinagovendasamy
"""


# Seeing number of pages linked to one page
from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np

import re

WORD_RE = re.compile(r"[\w]+")
(node, adjacent_list) = line.split('\t') 
total_nodes=len(node)

# page rank definitions:
# w0 or P(0) = initial pagerank = 1/total number of nodes in graph
# wj or P(j) = pagerank P of page j
# nj or C(j) = number of pages that cite page j = number of links on page j
# c or alpha = 0.15 based on reference

class PageRank(MRJob):

    #def comptage(self):
        """ returns total number of nodes"""
        #(node, adjacent_list) = line.split('\t') 
        #total_nodes=len(node)
        #return total_nodes
    
"""QUESTION: PEUT-ON UTILISER LE COMPTAGE DE CETTE FACON"""


    def mapper(self, _, line):
        """ This mapper yield 2 things:
        1. neighbour, pagerank
        2. node, adjacent_list (list of neighbours)
        """
        (node, adjacent_list) = line.split('\t') # ok

        total_neighbours=len(adjacent_list) 

        #total_nodes=self.PageRank.comptage(self,node)

        initial_pagerank=1/total_nodes # N.PageRank
        p=initial_pagerank/total_neighbours # N.PageRank/|N.AdjacencyList|

        for l in adjacent_list: # yields each neighbour l, and the page rank w(j) 
            yield l, p # Pass PageRank mass to neighbors
            # p est un float
            
        yield node,adjacent_list#  Pass along graph structure
        # adjacent_list est une liste
    

    def reducer(self, node ,p ): 
        """ yield 2 things:
        1. neighbour, pagerank of neighbour
        2. node, it's pagerank
        """
        c = 0.15 # provided
        
        #total_nodes=self.PageRank.comptage(self,node)
        list_p=list(p)
        list_neighbours=[]
        list_pageranks=[] # all the pageranks of each node
        for items in list_pagerank:
            if isinstance(items,list): #si nous avons adjacent_list - la liste des neighbours
                list_neighbours.append(items) # ATTENTION LISTE 2D - LISTE DE LISTE - A CONVERTIR EN 1D?
            if isinstance(items, float): # si nous avons un float, alors c'est p, c'est le pagerank de notre noeud/site. Recover graph structure.
                list_pageranks.append(items) # 1D list 
                # rappel: chq pagerank = N.PageRank/|N.AdjacencyList|
        
        # from list of lists (2D) to list (1D):
        flat_list_neighbours=[]
        for sublist in list_neighbours:
            for item in sublist:
                flat_list_neighbours.append(item)

        # somme de N.PageRank/|N.AdjacencyList| ou wkj/nj
        for pageranks in list_pageranks:
            s=np.sum(pageranks)
        
        # Finding w(k+1)j :
        """ --- QUESTION: sum(counts)"""
        new_pagerank=c/total_nodes+ (1-c)*s
        #for n in flat_list_neighbours:
            #yield n, new_pagerank/len(flat_list_neighbours) # number of pageranks for each neighbour
        yield node, new_pagerank # yielding nodes and their pageranks



    def steps(self):
        N=10 # nombre d'itérations
        return [MRStep(mapper=self.mapper,
        reducer=self.reducer)]

        

if __name__ == '__main__':
    PageRank.run()
    
    
