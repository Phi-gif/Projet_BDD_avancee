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


# page rank abbreviations:
# w0 or P(0) = initial pagerank = 1/total number of nodes in graph
# wj or P(j) = pagerank P of page j
# nj or C(j) = number of pages that cite page j = number of links on page j
# c or alpha = 0.15 based on reference

class PageRank(MRJob):
    
    total_nodes = 0
    dico_nj = {}
    dico_pagerank = {}
    
    #renvoie la page j et la page i qui la cite
    def mapper_adjacent(self, _, line):
        (i, j) = line.split()
        liste_nodes = np.unique(i)
        for identifiant in liste_nodes:
            PageRank.dico_nj.setdefault(identifiant,0)
        PageRank.total_nodes = len(PageRank.dico_nj) #ça marche 
        for page in liste_nodes:
            PageRank.dico_pagerank[page] = 1/PageRank.total_nodes #ça marche
            yield 'in',(j,i)
        yield 'out', (i,j)

    # regroupe les pages j et renvoie la liste d'adjacence des pages i citées par j et le pagerank initial de j
    def reducer_adjacent(self, label , values):
        if label == 'out':
            for val in values:
                i,j = val
                PageRank.dico_nj[i]+=1
        else:
            for val in values:
                j,i = val
                yield j,i# 1/PageRank.total_nodes)
        
    def reducer_adjacent2(self,j,i):
        yield j,(i, 1/PageRank.total_nodes)
        
    
    def mapper_PageRank(self, i, node):
        """ This mapper yield 2 things:
        1. i, node
        2. neighbour, pagerank of the neighbour
        """
        adjacent_list, pagerank = node
    
        yield i, ('node',node) #pour garder la structure de graphe

        for j in adjacent_list: # yields each neighbour l, and the page rank w(j)
            p = PageRank.dico_pagerank[j]/PageRank.dico_nj[j]
            yield j, ('pagerank', p) # Pass PageRank mass to neighbors, p is float
                    
        
    def reducer_PageRank(self, n_id , values):    
            """ yield 2 things:
            1. n_id
            2. node
            """
            c = 0.15 # provided
            sum_p = 0
            node = ([],sum_p)
            
                
            for val in values:
                label, content = val

                # If it's a node, save the node
                if label == 'node':
                    node = content
#                    nom = nid
                
                # If it's a pagerank, sum the pagerank
                elif label == 'pagerank':
                    sum_p += content

            #update the pagerank
            new_pagerank = c/PageRank.total_nodes + (1-c)*sum_p

            #Update the node with the new pagerank
            node = (node[0] ,new_pagerank)
                
            #mettre à jour les pageranks dans dico
            PageRank.dico_pagerank[n_id] = new_pagerank

            yield(n_id, node)   


    def steps(self):
        N=10 # nombre d'itérations : QUESTION: OU UTILISER?
        return [MRStep(mapper=self.mapper_adjacent,
                       reducer=self.reducer_adjacent),
                MRStep(reducer=self.reducer_adjacent2),
                MRStep(mapper=self.mapper_PageRank,
                       reducer=self.reducer_PageRank),
                MRStep(mapper=self.mapper_PageRank,
                       reducer=self.reducer_PageRank)
        ]
        

if __name__ == '__main__':
    PageRank.run()  
    #print(PageRank.dico_nj['2227'])
