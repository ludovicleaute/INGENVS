# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:05:05 2016

@author: ludovic
"""

import py2neo as gp
from py2neo.ogm import *
import sys

ID = sys.argv[1]
password = sys.argv[2]

gp.authenticate("localhost:7474",ID,password)
graph = gp.Graph()

class Gene(GraphObject):
    __primarykey__ = 'entrezId'
    
    entrezId = Property()
        
fic = open("./prototype/datasets/genes.csv")
geneNodes = []
for line in fic.readlines():
    geneNodes.append(line.rstrip())
    

for gene in geneNodes:
    tx = graph.begin()
    g = Gene()
    g.entrezId= gene
    graph.create(g)
    tx.commit()

