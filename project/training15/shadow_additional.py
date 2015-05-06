
# Orignally found: https://github.com/DEAP/deap/blob/master/examples/gp/symbreg.py
# Modified by Tim Ribaric for COSC 5P71 Final Project
# Just uses the operators outlined in Truscott, 2011

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

#from scoop import futures

# param_file - set of general parameters for the GP run
# shadow_data_file - the provide shadow data
if len(sys.argv) != 4:
	print "Usage: python " + sys.argv[0] + " param_file" + " shadow_data_file" + " seed"
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
	for t in wd.split("\t"):
		tlist.append(float(t))
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


def sqrt_t(op):
	return math.sqrt(operator.abs(op))

def abs_t(op):
	return operator.abs(op)

pset = gp.PrimitiveSet("MAIN", 18)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(operator.neg, 1)
pset.addPrimitive(protectedDiv, 2)
pset.addEphemeralConstant("randFloat", lambda: random.uniform(-1, 1))

pset.addPrimitive(sqrt_t, 1)
pset.addPrimitive(abs_t, 1)

##GP Terminal Set
pset.renameArguments(ARG0='URBAN_PER') 
pset.renameArguments(ARG1='URBAN_POP')
pset.renameArguments(ARG2='LABOR_PARTICIPATION')
pset.renameArguments(ARG3='BIRTH_RATE')
pset.renameArguments(ARG4='ELEC_PER_CAP')
pset.renameArguments(ARG5='ENERGY')
pset.renameArguments(ARG6='CO2')
pset.renameArguments(ARG7='PHONES')
pset.renameArguments(ARG8='NET_IMPORTS')
pset.renameArguments(ARG9='POPULATION')
pset.renameArguments(ARG10='POPDENS')
pset.renameArguments(ARG11='ARABLE_PER_AG')
pset.renameArguments(ARG12='AGLAND_PER')
pset.renameArguments(ARG13='ARABLE_PER')
pset.renameArguments(ARG14='AREA')
pset.renameArguments(ARG15='COMSTHREE')
pset.renameArguments(ARG16='COMSTWO')
pset.renameArguments(ARG17='GDP_PPP')
##Other Initializations required for the GP to run. tree depth etc.
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=treeMin, max_=treeMax)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)
#toolbox.register("map",futures.map)

##Fitness Function

def evalSymbReg(individual):
	func = toolbox.compile(expr=individual)	
	accumScore = 0.0
	for sdp in wine_data[0:threshold]:
		actShadowPer = sdp[18]
		gp_score = func(sdp[0],
					sdp[1],
					sdp[2],
					sdp[3],
					sdp[4],
					sdp[5],
					sdp[6],
					sdp[7],
					sdp[8],	
					sdp[9],
					sdp[10],
					sdp[11],
					sdp[12],
					sdp[13],
					sdp[14],
					sdp[15],
					sdp[16],
					sdp[17])
		foundShadowPer = round((gp_score / sdp[17]) * 100,2)
		accumScore += (foundShadowPer - actShadowPer) ** 2

			
	return accumScore,
	
##Register GP toolbox object, maintains basic paramaters of run
toolbox.register("evaluate", evalSymbReg)
toolbox.register("select", tools.selTournament, tournsize=tSize)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("mutate", gp.mutNodeReplacement, pset=pset)
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

def main():

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
	
	#Write out the Best GPs Found
	bhof = open("logs/best_gp.txt","a")
	bhof.write("params: "+ str(sys.argv[1]) + " seed: " + str(seed) + " fitness: "+  str(hof[0].fitness) + "\n\n" + str(hof[0])+"\n\n")
	#Write out finesss score of Best GP found
	score = open("logs/gp_best_fitness_scores.csv","a")
	score.write(str(hof[0].fitness).split(",")[0].strip("(")+"\n")
	#write out logbooks of run
	if len(str(seed)) == 1:
		seed_label = "0" + str(seed)
	else:
		seed_label = str(seed)
	f = open("logs/genlog_" + seed_label + ".txt","w")
	f.write(str(log))
	f.close()
	
	
	##Evaluate Training
	trainDataFile = open("./logs/training_seed_"+str(seed)+".csv","w")
	func = toolbox.compile(expr=hof[0])	
	for sdp in wine_data[:threshold]:
		actShadowPer = sdp[18]
		gp_score = func(sdp[0],
				sdp[1],
				sdp[2],
				sdp[3],
				sdp[4],
				sdp[5],
				sdp[6],
				sdp[7],
				sdp[8],
				sdp[9],
				sdp[10],
				sdp[11],
				sdp[12],
				sdp[13],
				sdp[14],
				sdp[15],
				sdp[16],
				sdp[17])
		foundShadowPer = round((gp_score / sdp[17]) * 100,2)
		diffPer = foundShadowPer - actShadowPer
		#print str(actShadowPer) + "  :  " + str(foundShadowPer) + "  :  " + str(diffPer)
		trainDataFile.write(str(actShadowPer) + "," + str(foundShadowPer) + "," + str(diffPer)+ "\n")

	testDataFile = open("./logs/testing_seed_"+str(seed)+".csv","w")
	for sdp in wine_data[threshold:]:
		actShadowPer = sdp[18]
		gp_score = func(sdp[0],
				sdp[1],
				sdp[2],
				sdp[3],
				sdp[4],
				sdp[5],
				sdp[6],
				sdp[7],
				sdp[8],
				sdp[9],
				sdp[10],
				sdp[11],
				sdp[12],
				sdp[13],
				sdp[14],
				sdp[15],
				sdp[16],
				sdp[17])
		foundShadowPer = round((gp_score / sdp[17]) * 100,2)
		diffPer = foundShadowPer - actShadowPer
		#print str(actShadowPer) + "  :  " + str(foundShadowPer) + "  :  " + str(diffPer)
		testDataFile.write(str(actShadowPer) + "," + str(foundShadowPer) + "," + str(diffPer)+ "\n")

if __name__ == "__main__":
	main()
