#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:54:41 2018

@author: RitaRamos
"""

import var_despatcher

def PBConstraintLEQ(my_vars,weights, k):
    s_ij={} 
    literals =[]
    vars_size=len(my_vars)
    
    for i in range(vars_size):
        for j in range (1, k + 1):
            s_ij[(i,j)]= var_despatcher.gen_aux() #GONCALLOOOO
        
    auxVars=[]
    auxWeights=[]
    
    for i in range(my_vars):
        if weights[i]>k:
            _SATSolver.add_clause([-my_vars[i]])
        else:
            auxVars+=my_vars[i]
            auxWeights+=weights[i]
    my_vars=auxVars
    weights=auxWeights
    
    
    for j in range(1, weights[0] +1):
        _SATSolver.add_clause([-my_vars[0], s_ij[(0,j)] ])
    
    for j in range(weights[0]+1, k +1):
        _SATSolver.add_clause([-s_ij[(0,j)] ])
    
    for i in range(1, len(my_vars)):
        for j in range(1, weights[i]):
            _SATSolver.add_clause( [-my_vars[i], s_ij[(i,j)] ])
            
    for j in range(1, k+1):
        _SATSolver.add_clause( [ s_ij[(i-1,j)]    , s_ij[(i,j)] ])
        
    for j in range(1, k- weights[i]+ 1):
        _SATSolver.add_clause( [ -my_vars[i], s_ij[(i-1,j)]    , s_ij[(i,j +weights[i])] ])
    
    _SATSolver.add_clause( [-my_vars[i], s_ij[(i-1, k+1-weights[i] )] ])
    
    return s_ij


def PBConstraintGEQ(my_vars, weights,  k):
    newK = 0
    
    for i in range(len(weights)):
        my_vars[i] = -my_vars[i]
        newK += weights[i]

    newK -= k

    return PBConstraintLEQ(my_vars, weights, newK)       
            
            
