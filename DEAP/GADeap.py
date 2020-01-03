#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Bruce Han <superhxl@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Deap examples
"""

from deap import creator
from deap import base
from deap import tools

import random
import math

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

IND_SIZE = 33
toolbox = base.Toolbox()
toolbox.register("attribute", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual,
        toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def decode(ind):
    x1 = int("".join(map(str,ind[:18])),2)
    x1 = -3.0 + x1 * (12.1 + 3.0)/ (2**18 - 1) 
    x2 = int("".join(map(str,ind[18:])),2)
    x2= 4.1 + x2 * (5.8 - 4.1)/ (2**15 - 1) 

    return x1, x2

def evaluate(ind):
    x1,x2 = decode(ind)

    return 21.5+x1*math.sin(4*math.pi*x1)+x2*math.sin(20*math.pi*x2),

toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.01)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

def main():
    pop = toolbox.population(n=100)
    CXPB, MUTPUB, NGEN = 0.25, 0.01,500 

    # Evaluate the entire population
    fitnesses =list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))


        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPUB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = list(map(toolbox.evaluate, invalid_ind))
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

    print("-- End of evolution --")
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %f, %f" % decode(best_ind))
    print("  best objetive is %f" % best_ind.fitness.values)
if __name__ == "__main__":
    main()
