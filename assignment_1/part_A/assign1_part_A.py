
# Originally found: https://github.com/DEAP/deap/blob/master/examples/gp/symbreg.py
# Modified by Tim Ribaric for COSC 5P71 Assignment #1
# tr13ry@brocku.ca
# This file will generate all of the GP data

import operator
import math
import random
import sys
import ConfigParser
import numpy
import time

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

if __name__ == "__main__":

	# param_file - set of general parameters for the GP run
	# points_file - randomly chosen points on the polynomial we are trying to fit
	if len(sys.argv) != 4:
		print "Usage: python " + sys.argv[0] + " param_file" + " points_file" + " seed"
		sys.exit()
	
	#initialize values from input parameter file
	param_config = ConfigParser.ConfigParser()
	param_config.read(sys.argv[1])

	#Seed from input file and set it here
	seed = int(sys.argv[3])
	random.seed(seed)

	#GP parameters
	numberGens = int(param_config.get("GeneticProgramParams","numberGens"))
	popSize = int(param_config.get("GeneticProgramParams","popSize"))
	probCross = float(param_config.get("GeneticProgramParams","probCross"))
	probMutate = float(param_config.get("GeneticProgramParams","probMutate"))
	tSize = int(param_config.get("GeneticProgramParams","tournamentSize"))
	
	#load function points in from file on command line
	p_file = open(sys.argv[2],"r")
	input_points = []
	for p in p_file:
		input_points.append([float(p.split(',')[0].rstrip("\n")), float(p.split(',')[1].rstrip("\n"))])
	
	#shuffle the points a bit so they are not sequential along the x axis
	#not specifically necessary but I was testing to see if this slowed down
	#finding an optimal solution
	random.shuffle(input_points)
	
	# GP Function Definition
	# Protected division, will just retun 1 if divsion by 0
	def protectedDiv(left, right):
		try:
			return left / right
		except ZeroDivisionError:
			return 1
	pset = gp.PrimitiveSet("MAIN", 1)
	pset.addPrimitive(operator.add, 2)
	pset.addPrimitive(operator.sub, 2)
	pset.addPrimitive(operator.mul, 2)
	pset.addPrimitive(protectedDiv, 2)
	pset.addPrimitive(operator.neg, 1)
	
	#GP Terminal Set
	pset.renameArguments(ARG0='x')
	
	#Other Initializations required for the GP to run. tree depth etc.
	creator.create("FitnessMin", base.Fitness, weights=(-1.0,)) #tell it to minimize fitness function score
	creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)
	toolbox = base.Toolbox()
	toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
	toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	toolbox.register("compile", gp.compile, pset=pset)

	#Fitness Function
	#Basically Mean Squared Error from the points passed in from the input file
	#versus the GP evaluated at those points
	#try to minimize this value
	def evalSymbReg(individual):
		func = toolbox.compile(expr=individual)
		running = []
		for point in input_points:
			running.append((point[1] - func(point[0])) ** 2)
		return math.fsum(running) / len (input_points),
		
	#Register GP toolbox object, maintains basic parameters of run
	toolbox.register("evaluate", evalSymbReg)
	toolbox.register("select", tools.selTournament, tournsize=tSize)
	toolbox.register("mate", gp.cxOnePoint)
	toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
	toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
	toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
	toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

	#Set final parameter before run
	pop = toolbox.population(n=popSize)
	hof = tools.HallOfFame(1) #to keep best solution found each run, useful for analysis
	#use built-in tools to do the stats work
	stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
	stats_size = tools.Statistics(len)
	mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
	mstats.register("avg", numpy.mean)
	mstats.register("std", numpy.std)
	mstats.register("min", numpy.min)
	mstats.register("max", numpy.max)
	#Conduct 1 Run
	pop, log = algorithms.eaSimple(pop, toolbox, probCross, probMutate, numberGens, stats=mstats,
                                   halloffame=hof, verbose=False)
	
	#hof object is best GP individual found by the system. write that out with some other data
	bhof = open("best_sols.txt","a")
	bhof.write("params: "+ str(sys.argv[1]) + " seed: " + str(seed) + " fitness: "+  str(hof[0].fitness) + "\n\n" + str(hof[0])+"\n\n")
		
	#write out logbooks of run, those contain detailed information about run
	if len(str(seed)) == 1:
		f = open("logs/"+str(sys.argv[1]) + "_0" + str(seed) + ".txt","w")
		f.write(str(log))
		f.close()
	else:
		f = open("logs/"+str(sys.argv[1]) + "_" + str(seed) + ".txt","w")
		f.write(str(log))
		f.close()
	
