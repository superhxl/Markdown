#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Bruce Han <superhxl@gmail.com>
#
# Distributed under terms of the MIT license.
"""
Python docplex
"""
from docplex.mp.model import Model
from sys import stdout

Supply = (60, 55, 51, 43, 41, 52)
Demand = (35, 37, 22, 32, 41, 32, 43, 38)
Cost = ((6, 2, 6, 7, 4, 2, 9, 5), (4, 9, 5, 3, 8, 5, 8, 2),
        (5, 2, 1, 9, 7, 4, 3, 3), (7, 6, 7, 3, 9, 2, 7, 1),
        (2, 3, 9, 5, 7, 2, 6, 5), (5, 5, 2, 2, 8, 1, 4, 8))

model = Model("transport")
x = model.continuous_var_matrix(keys1=range(len(Supply)),
                                keys2=range(len(Demand)),
                                name="x")
model.minimize(model.sum(Cost[i][j] * x[(i,j)] for i in range(len(Supply)) for
                         j in range(len(Demand))))

for j, d in enumerate(Demand):
    model.add_constraint(model.sum(x[(i, j)] for i in range(len(Supply))) == d,
                         ctname="Demand%s" % j)

for i, s in enumerate(Supply):
    model.add_constraint(model.sum(x[(i, j)] for j in range(len(Demand))) <= s,
                         ctname="Supply%s" % i)

model.export_as_lp("tranport.lp")

solution = model.solve()
if solution:
    print("The objective value is: %6.3f" % solution.objective_value)
    stdout.write("Solution:\n")
    for i in range(len(Supply)):
        for j in range(len(Demand)):
            stdout.write("  %6.2f" % (solution[x[(i,j)]],))
        stdout.write("\n")
else:
    stdout.write("Solve status:" + solution.get_solve_status() + "\n")
