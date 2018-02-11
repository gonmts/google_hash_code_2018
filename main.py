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
        for i in range(self.par_slice):
            for i in range(self.rows):
                for j in range(self.col):
                    if(self.pizza[i,j]=="T"):
                        cnf_tomato+=self.var_dispatcher.pizza_to_cnf(i,j,par_slice)
                    else:
                        cnf_mushroom+=self.var_dispatcher.pizza_to_cnf(i,j,par_slice)

        #cnf_tomato.append()

        s_ij_tomato=pseudo_boolean.PBConstraintGEQ(cnf_tomato, [1] * len(cnf_tomato), self.l , self.solver)
        s_ij_mushroom=pseudo_boolean.PBConstraintGEQ(cnf_tomato, [1] * len(cnf_tomato),  self.l, self.solver)

    def contraint_maxCell():
        var = []
        for i in range(self.rows):
            for j in range(self.col):
                for s in range(self.par_slice):
                    var += [self.var_dispatcher.pizza_to_cnf(i, j, s)]
                s_ij_cenas=pseudo_boolean.PBConstraintLEQ(var, [1] * len(var), 1, self.solver)









    def main(self, filename):
        self.rows, self.col, self.l, self.h, self.pizza=read_pizza.read_pizza_file(filename)
        self.par_slice=(rows*col)/max_cell
        self.solver=Solver()
        self.var_dispatcher= VarDispatcher(rows, col,par_slice,solver)








if __name__ == "__main__":
