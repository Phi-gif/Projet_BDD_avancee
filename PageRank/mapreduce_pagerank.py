#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:10:28 2020

@author: elvinagovendasamy
"""


# Seeing number of pages linked to one page
from mrjob.job import MRJob
from mrjob.step import MRStep
#import re

#WORD_RE = re.compile(r"[\w]+")

class PageRank(MRJob):
    
    #renvoie la page i et la page j qu'elle cite sur la ligne
    def mapper_adjacent(self, _, line):
        (node, j) = line.split('\t')    
        yield node, j

    # regroupe les pages i et renvoie la liste d'adjacence
    def reducer1(self, node , j):
        yield node, j
        
    #renvoi la page i et son pagerank initial, ainsi que son nb de voisins
    def mapper_poids(self, node, adjacent_list):
        l = len(list(adjacent_list))
        p = 1/l
        yield node, (p,adjacent_list,l)
        
    def steps(self):
        return [
           MRStep(mapper=self.mapper_adjacent,
                  reducer=self.reducer1),
           MRStep(mapper=self.mapper_poids)
         ]
    
if __name__ == '__main__':
    PageRank.run()
    
    
