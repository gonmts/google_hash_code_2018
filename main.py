#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:20:40 2018

@author: RitaRamos
"""

import read_pizza
import pseudo_boolean
#from pycryptosat import Solver


class Main:
    def __init__(self):
        
    def constraint_minL():
        cnf_tomato=[]
        cnf_mushroom=[]
        for s in range(self.par_slice):
            for i in range(self.rows):
                for j in range(self.col):
                    if(self.pizza[i,j]=="T"):
                        cnf_tomato+=[self.var_dispatcher.pizza_to_cnf(i,j,s)]
                    else:
                        cnf_mushroom+=[self.var_dispatcher.pizza_to_cnf(i,j,par_s)]
        
        cnf_h=cnf_tomato.append(cnf_mushroom)
        s_ij_H=pseudo_boolean.PBConstraintLEQ(cnf_h, [1] * len(cnf_h), self.h , self.solver) 

        s_ij_tomato=pseudo_boolean.PBConstraintGEQ(cnf_tomato, [1] * len(cnf_tomato), self.l , self.solver) 
        s_ij_mushroom=pseudo_boolean.PBConstraintGEQ(cnf_mushroom, [1] * len(cnf_mushroom),  self.l, self.solver)
              
   
     
    def                  

                 
            
        
        
        
        
    
    def main(self, filename):
        self.rows, self.col, self.l, self.h, self.pizza=read_pizza.read_pizza_file(filename)
        self.par_slice=(rows*col)/max_cell
        self.solver=Solver()
        self.var_dispatcher= VarDispatcher(rows, col,par_slice,solver)
    
    
    
    




if __name__ == "__main__":
    
    