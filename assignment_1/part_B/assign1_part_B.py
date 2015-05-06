
# Orignally found: https://github.com/DEAP/deap/blob/master/examples/gp/symbreg.py
# Modified by Tim Ribaric for COSC 5P71 Assignment #1, Part B
# When called with the paramSet file wine data file and seed will compute
# a whole evolution

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
	# wine_data_file - Wine Data Set from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
	if len(sys.argv) != 4:
		print "Usage: python " + sys.argv[0] + " param_file" + " wine_data_file" + " seed"
		sys.exit()
	
	#initialize values from input parameter file
	param_config = ConfigParser.ConfigParser()
	param_config.read(sys.argv[1])
	seed = int(sys.argv[3])
	random.seed(seed)
	numberGens = int(param_config.get("GeneticProgramParams","numberGens"))
	popSize = int(param_config.get("GeneticProgramParams","popSize"))
	probCross = float(param_config.get("GeneticProgramParams","probCross"))
	probMutate = float(param_config.get("GeneticProgramParams","probMutate"))
	tSize = int(param_config.get("GeneticProgramParams","tournamentSize"))
	treeMin = int(param_config.get("GeneticProgramParams","treeMin"))
	treeMax =  int(param_config.get("GeneticProgramParams","treeMax"))
	
	#What % of the data set to devote to training
	#Testing is 100% - this number
	training_percent = float(param_config.get("GeneticProgramParams","training_percent"))
	
	#Load input from file
	wine_file = open(sys.argv[2],"r")
	wine_data = []
	wine_file.readline()
	for wd in wine_file:
		tlist = list()
		for t in wd.split(";"):
			tlist.append(float(t.rstrip("\n")))
		wine_data.append(tlist)
	#shuffle the dataset, seed as been set already
	random.shuffle(wine_data)
	#this is the last index into wine_data that separates training/testing
	#training: for wscore in wine_data[threshold]
	#testing: for wscore in wine_data[threshold:]:
	threshold = int(training_percent * len(wine_data) / 100)


	# GP Function Definition
	def protectedDiv(left, right):
		try:
			return left / right
		except ZeroDivisionError:
			return 1
	pset = gp.PrimitiveSet("MAIN", 11)
	pset.addPrimitive(operator.add, 2)
	pset.addPrimitive(operator.sub, 2)
	pset.addPrimitive(operator.mul, 2)
	pset.addPrimitive(protectedDiv, 2)
	pset.addPrimitive(operator.neg, 1)
	#Includes some trig functions
	pset.addPrimitive(math.cos, 1)
	pset.addPrimitive(math.sin, 1)
	#EphemeralConstant that will take the value of -1, 0, 1
	#combines will with trig functions
	pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))
		
	##GP Terminal Set
	pset.renameArguments(ARG0='faci')	#1 - fixed acidity 			- faci
	pset.renameArguments(ARG1='vaci')	#2 - volatile acidity		- vaci
	pset.renameArguments(ARG2='caci')	#3 - citric acid			- caci
	pset.renameArguments(ARG3='rsug')	#4 - residual sugar			- rsug
	pset.renameArguments(ARG4='chol')	#5 - chlorides				- chol
	pset.renameArguments(ARG5='fsdi')	#6 - free sulfur dioxide	- fsdi
	pset.renameArguments(ARG6='tsdi')	#7 - total sulfur dioxide	- tsdi
	pset.renameArguments(ARG7='dens')	#8 - density				- dens
	pset.renameArguments(ARG8='pphh')	#9 - pH						- pphh
	pset.renameArguments(ARG9='sulp')	#10 - sulphates				- sulp
	pset.renameArguments(ARG10='alco')	#11 - alcohol				- alco
		
	##Other Initializations required for the GP to run. tree depth etc.
	creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
	creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)
	toolbox = base.Toolbox()
	toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=treeMin, max_=treeMax)
	toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	toolbox.register("compile", gp.compile, pset=pset)

	##Fitness Function
	#Basically a cumulative Mean Square minimization
	#evaluates GP individual along 11 dimensions of data
	#takes the difference from the assigned value and squares it
	#evolution will then try to minimize this value across the
	#whole training set
	
	def evalSymbReg(individual):
		func = toolbox.compile(expr=individual)	
		accumScore = 0.0
		
		for wdp in wine_data[0:threshold]:
			dim1 = wdp[0]	#1 - fixed acidity 			- faci
			dim2 = wdp[1]	#2 - volatile acidity		- vaci
			dim3 = wdp[2]	#3 - citric acid			- caci
			dim4 = wdp[3]	#4 - residual sugar			- rsug
			dim5 = wdp[4]	#5 - chlorides				- chol
			dim6 = wdp[5]	#6 - free sulfur dioxide	- fsdi
			dim7 = wdp[6]	#7 - total sulfur dioxide	- tsdi
			dim8 = wdp[7]	#8 - density				- dens
			dim9 = wdp[8]	#9 - pH						- pphh
			dim10 = wdp[9]	#10 - sulphates				- sulp
			dim11 = wdp[10]	#11 - alcohol				- alco
			actualScore = wdp[11] #Actual Assigned Score
			accumScore += (func(dim1,dim2,dim3,dim4,dim5,dim6,dim7,dim8,dim9,dim10,dim11) - actualScore) ** 2

		return accumScore,
		
	##Register GP toolbox object, maintains basic paramaters of run
	toolbox.register("evaluate", evalSymbReg)
	toolbox.register("select", tools.selTournament, tournsize=tSize)
	toolbox.register("mate", gp.cxOnePoint)
	toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
	toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
	toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
	toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

	##Set final paramater before run
	pop = toolbox.population(n=popSize)
	hof = tools.HallOfFame(1)
	stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
	stats_size = tools.Statistics(len)
	mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
	mstats.register("avg", numpy.mean)
	mstats.register("std", numpy.std)
	mstats.register("min", numpy.min)
	mstats.register("max", numpy.max)
	
	##Conduct 1 Run
	pop, log = algorithms.eaSimple(pop, toolbox, probCross, probMutate, numberGens, stats=mstats,
                                   halloffame=hof, verbose=True)
	
	#hof object is best GP individual found by the system. write that out with some other data
	bhof = open("best_sols.txt","a")
	bhof.write("params: "+ str(sys.argv[1]) + " seed: " + str(seed) + " fitness: "+  str(hof[0].fitness) + "\n\n" + str(hof[0])+"\n\n")
	
	#write out logbooks of run
	if len(str(seed)) == 1:
		f = open("logs/"+str(sys.argv[1]) + "_0" + str(seed) + ".txt","w")
		f.write(str(log))
		f.close()
	else:
		f = open("logs/"+str(sys.argv[1]) + "_" + str(seed) + ".txt","w")
		f.write(str(log))
		f.close()
		
	#Start the testing
	testDataFile = open("./data/testing/testing_seed_"+str(seed)+".txt","w")
	func = toolbox.compile(expr=hof[0])	
	for wdp in wine_data[threshold:]:
		dim1 = wdp[0]	#1 - fixed acidity 			- faci
		dim2 = wdp[1]	#2 - volatile acidity		- vaci
		dim3 = wdp[2]	#3 - citric acid			- caci
		dim4 = wdp[3]	#4 - residual sugar			- rsug
		dim5 = wdp[4]	#5 - chlorides				- chol
		dim6 = wdp[5]	#6 - free sulfur dioxide	- fsdi
		dim7 = wdp[6]	#7 - total sulfur dioxide	- tsdi
		dim8 = wdp[7]	#8 - density				- dens
		dim9 = wdp[8]	#9 - pH						- pphh
		dim10 = wdp[9]	#10 - sulphates				- sulp
		dim11 = wdp[10]	#11 - alcohol				- alco
		estScore = str(float(func(dim1,dim2,dim3,dim4,dim5,dim6,dim7,dim8,dim9,dim10,dim11)))
		actScore = str(float(wdp[11]))
		
		testDataFile.write(estScore + "," + actScore + "\n")

	# Write out the training data
	testDataFile = open("./data/training/training_seed_"+str(seed)+".txt","w")
	func = toolbox.compile(expr=hof[0])
	#This is the big change, here we calculate across training data and write out the results	
	for wdp in wine_data[0:threshold]:
		dim1 = wdp[0]	#1 - fixed acidity 			- faci
		dim2 = wdp[1]	#2 - volatile acidity		- vaci
		dim3 = wdp[2]	#3 - citric acid			- caci
		dim4 = wdp[3]	#4 - residual sugar			- rsug
		dim5 = wdp[4]	#5 - chlorides				- chol
		dim6 = wdp[5]	#6 - free sulfur dioxide	- fsdi
		dim7 = wdp[6]	#7 - total sulfur dioxide	- tsdi
		dim8 = wdp[7]	#8 - density				- dens
		dim9 = wdp[8]	#9 - pH						- pphh
		dim10 = wdp[9]	#10 - sulphates				- sulp
		dim11 = wdp[10]	#11 - alcohol				- alco
		estScore = str(float(func(dim1,dim2,dim3,dim4,dim5,dim6,dim7,dim8,dim9,dim10,dim11)))
		actScore = str(float(wdp[11]))
		
		testDataFile.write(estScore + "," + actScore + "\n")

	testDataFile.close()
