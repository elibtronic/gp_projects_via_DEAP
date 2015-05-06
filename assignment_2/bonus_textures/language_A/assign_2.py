####
####
###
## This program will:
#	- load all the precalulated data from pregenerate_data.py
#	- Evolve a GP based on what texture it is told to discriminate
#	- save all logs generated as text
#	- save all GP programs generated as text and pickles
#

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
from scipy.misc import imread,imsave
from filter_functions import *

import ConfigParser
import operator
import math
import random
import sys
import time
import math
import pickle

import numpy as np


def main():

	# param_file - set of general parameters for the GP run
	# texture_to_find - which of the 4 textures are we treating as positive
	if len(sys.argv) != 4:
		print "Usage: python " + sys.argv[0] + " param_file" + " texture_to_find" + " seed"
		sys.exit()

	#initialize values from input parameter file
	param_config = ConfigParser.ConfigParser()
	param_config.read(sys.argv[1])


	#load textures in
	t1n = str(param_config.get("textureFiles","texture1"))
	t2n = str(param_config.get("textureFiles","texture2"))
	t3n = str(param_config.get("textureFiles","texture3"))
	t4n = str(param_config.get("textureFiles","texture4"))

	t1 = imread(t1n)
	t2 = imread(t2n)
	t3 = imread(t3n)
	t4 = imread(t4n)


	# Retrieve these values from the pickles	
	print "Intializing pre-calculated filter data"

	#Load Pre Calculated Testing Points
	q1 = pickle.load(open("training_points/q1.pkl","rb"))
	q2 = pickle.load(open("training_points/q2.pkl","rb"))
	q3 = pickle.load(open("training_points/q3.pkl","rb"))
	q4 = pickle.load(open("training_points/q4.pkl","rb"))

	texToFind = int(sys.argv[2])
	
	# Pre Calculated AVG3 scores
	q1_avg3 = pickle.load(open( "filter_values/q1_avg3.pkl", "rb" ))
	q2_avg3 = pickle.load(open( "filter_values/q2_avg3.pkl", "rb" ))
	q3_avg3 = pickle.load(open( "filter_values/q3_avg3.pkl", "rb" ))
	q4_avg3 = pickle.load(open( "filter_values/q4_avg3.pkl", "rb" ))
	
	# Pre Calculated STD3 scores
	q1_std3 = pickle.load(open( "filter_values/q1_std3.pkl", "rb" ))
	q2_std3 = pickle.load(open( "filter_values/q2_std3.pkl", "rb" ))
	q3_std3 = pickle.load(open( "filter_values/q3_std3.pkl", "rb" ))
	q4_std3 = pickle.load(open( "filter_values/q4_std3.pkl", "rb" ))
	
	# Pre Calculated MIN3 scores
	q1_min3 = pickle.load(open( "filter_values/q1_min3.pkl", "rb" ))
	q2_min3 = pickle.load(open( "filter_values/q2_min3.pkl", "rb" ))
	q3_min3 = pickle.load(open( "filter_values/q3_std3.pkl", "rb" ))
	q4_min3 = pickle.load(open( "filter_values/q4_std3.pkl", "rb" ))
	
	# Pre Calculated MAX3 scores
	q1_max3 = pickle.load(open( "filter_values/q1_max3.pkl", "rb" ))
	q2_max3 = pickle.load(open( "filter_values/q2_max3.pkl", "rb" ))
	q3_max3 = pickle.load(open( "filter_values/q3_max3.pkl", "rb" ))
	q4_max3 = pickle.load(open( "filter_values/q4_max3.pkl", "rb" ))

	#Pre Calculate AVG5 scores
	q1_avg5 = pickle.load(open( "filter_values/q1_avg5.pkl", "rb" ))
	q2_avg5 = pickle.load(open( "filter_values/q2_avg5.pkl", "rb" ))
	q3_avg5 = pickle.load(open( "filter_values/q3_avg5.pkl", "rb" ))
	q4_avg5 = pickle.load(open( "filter_values/q4_avg5.pkl", "rb" ))
	
	#Pre Calculate STD5 scores
	q1_std5 = pickle.load(open( "filter_values/q1_std5.pkl", "rb" ))
	q2_std5 = pickle.load(open( "filter_values/q2_std5.pkl", "rb" ))
	q3_std5 = pickle.load(open( "filter_values/q3_std5.pkl", "rb" ))
	q4_std5 = pickle.load(open( "filter_values/q4_std5.pkl", "rb" ))
	
	#Pre Calculate MIN5 scores
	q1_min5 = pickle.load(open( "filter_values/q1_min5.pkl", "rb" ))
	q2_min5 = pickle.load(open( "filter_values/q2_min5.pkl", "rb" ))
	q3_min5 = pickle.load(open( "filter_values/q3_min5.pkl", "rb" ))
	q4_min5 = pickle.load(open( "filter_values/q4_min5.pkl", "rb" ))
	
	#Pre Calculate MAX5 scores
	q1_max5 = pickle.load(open( "filter_values/q1_max5.pkl", "rb" ))
	q2_max5 = pickle.load(open( "filter_values/q2_max5.pkl", "rb" ))
	q3_max5 = pickle.load(open( "filter_values/q3_max5.pkl", "rb" ))
	q4_max5 = pickle.load(open( "filter_values/q4_max5.pkl", "rb" ))

	#Pre Calculate AVG7 scores
	q1_avg7 = pickle.load(open( "filter_values/q1_avg7.pkl", "rb" ))
	q2_avg7 = pickle.load(open( "filter_values/q2_avg7.pkl", "rb" ))
	q3_avg7 = pickle.load(open( "filter_values/q3_avg7.pkl", "rb" ))
	q4_avg7 = pickle.load(open( "filter_values/q4_avg7.pkl", "rb" ))
	
	#Pre Calculate STD7 scores
	q1_std7 = pickle.load(open( "filter_values/q1_std7.pkl", "rb" ))
	q2_std7 = pickle.load(open( "filter_values/q2_std7.pkl", "rb" ))
	q3_std7 = pickle.load(open( "filter_values/q3_std7.pkl", "rb" ))
	q4_std7 = pickle.load(open( "filter_values/q4_std7.pkl", "rb" ))
	
	#Pre Calculate MIN7 scores
	q1_min7 = pickle.load(open( "filter_values/q1_min7.pkl", "rb" ))
	q2_min7 = pickle.load(open( "filter_values/q2_min7.pkl", "rb" ))
	q3_min7 = pickle.load(open( "filter_values/q3_min7.pkl", "rb" ))
	q4_min7 = pickle.load(open( "filter_values/q4_min7.pkl", "rb" ))

	#Pre Calculate MAX7 scores
	q1_max7 = pickle.load(open( "filter_values/q1_max7.pkl", "rb" ))
	q2_max7 = pickle.load(open( "filter_values/q2_max7.pkl", "rb" ))
	q3_max7 = pickle.load(open( "filter_values/q3_max7.pkl", "rb" ))
	q4_max7 = pickle.load(open( "filter_values/q4_max7.pkl", "rb" ))

	#Pre Calculate AVG9 scores
	q1_avg9 = pickle.load(open( "filter_values/q1_avg9.pkl", "rb" ))
	q2_avg9 = pickle.load(open( "filter_values/q2_avg9.pkl", "rb" ))
	q3_avg9 = pickle.load(open( "filter_values/q3_avg9.pkl", "rb" ))
	q4_avg9 = pickle.load(open( "filter_values/q4_avg9.pkl", "rb" ))
	
	#Pre Calculate STD9 scores
	q1_std9 = pickle.load(open( "filter_values/q1_std9.pkl", "rb" ))
	q2_std9 = pickle.load(open( "filter_values/q2_std9.pkl", "rb" ))
	q3_std9 = pickle.load(open( "filter_values/q3_std9.pkl", "rb" ))
	q4_std9 = pickle.load(open( "filter_values/q4_std9.pkl", "rb" ))

	#Pre Calculate MIN9 scores
	q1_min9 = pickle.load(open( "filter_values/q1_min9.pkl", "rb" ))
	q2_min9 = pickle.load(open( "filter_values/q2_min9.pkl", "rb" ))
	q3_min9 = pickle.load(open( "filter_values/q3_min9.pkl", "rb" ))
	q4_min9 = pickle.load(open( "filter_values/q4_min9.pkl", "rb" ))

	#Pre Calculate MAX9 scores
	q1_max9 = pickle.load(open( "filter_values/q1_max9.pkl", "rb" ))
	q2_max9 = pickle.load(open( "filter_values/q2_max9.pkl", "rb" ))
	q3_max9 = pickle.load(open( "filter_values/q3_max9.pkl", "rb" ))
	q4_max9 = pickle.load(open( "filter_values/q4_max9.pkl", "rb" ))
	
	#Pre Calculate AVG11 scores
	q1_avg11 = pickle.load(open( "filter_values/q1_avg11.pkl", "rb" ))
	q2_avg11 = pickle.load(open( "filter_values/q2_avg11.pkl", "rb" ))
	q3_avg11 = pickle.load(open( "filter_values/q3_avg11.pkl", "rb" ))
	q4_avg11 = pickle.load(open( "filter_values/q4_avg11.pkl", "rb" ))
	
	#Pre Calculate STD11 scores
	q1_std11 = pickle.load(open( "filter_values/q1_std11.pkl", "rb" ))
	q2_std11 = pickle.load(open( "filter_values/q2_std11.pkl", "rb" ))
	q3_std11 = pickle.load(open( "filter_values/q3_std11.pkl", "rb" ))
	q4_std11 = pickle.load(open( "filter_values/q4_std11.pkl", "rb" ))

	#Pre Calculate MIN11 scores
	q1_min11 = pickle.load(open( "filter_values/q1_min11.pkl", "rb" ))
	q2_min11 = pickle.load(open( "filter_values/q2_min11.pkl", "rb" ))
	q3_min11 = pickle.load(open( "filter_values/q3_min11.pkl", "rb" ))
	q4_min11 = pickle.load(open( "filter_values/q4_min11.pkl", "rb" ))

	#Pre Calculate MAX11 scores
	q1_max11 = pickle.load(open( "filter_values/q1_max11.pkl", "rb" ))
	q2_max11 = pickle.load(open( "filter_values/q2_max11.pkl", "rb" ))
	q3_max11 = pickle.load(open( "filter_values/q3_max11.pkl", "rb" ))
	q4_max11 = pickle.load(open( "filter_values/q4_max11.pkl", "rb" ))

	print "Begining GP Evolution"
	#GP parameters
	numberGens = int(param_config.get("GeneticProgramParams","numberGens"))
	popSize = int(param_config.get("GeneticProgramParams","popSize"))
	probCross = float(param_config.get("GeneticProgramParams","probCross"))
	probMutate = float(param_config.get("GeneticProgramParams","probMutate"))
	tSize = int(param_config.get("GeneticProgramParams","tournamentSize"))
	
	#Seed from input file and set it here
	seed = int(sys.argv[3])
	random.seed(seed)
	
	# GP Function Definition
	# Protected division, will just retun 1 if divsion by 0
	def protectedDiv(left, right):
		try:
			return left / right
		except ZeroDivisionError:
			return 1
	#MAX according to Poli 1996
	def maxFValue(left,right):
		if left >= right:
			return left
		else:
			return right
	#MIN according to Poli 1996
	def minFValue(left,right):
		if left <= right:
			return left
		else:
			return right
	
	
	pset = gp.PrimitiveSet("MAIN", 20)
	pset.addPrimitive(operator.add, 2)
	pset.addPrimitive(operator.sub, 2)
	pset.addPrimitive(operator.mul, 2)
	pset.addPrimitive(protectedDiv, 2)
	pset.addPrimitive(maxFValue, 2)
	pset.addPrimitive(minFValue, 2)
	
	#pset.addPrimitive(operator.neg, 1)	
	#pset.addEphemeralConstant("randFloat", lambda: random.uniform(-1, 1))
	
	#GP Terminal Set
	# 3 x 3 grids
	pset.renameArguments(ARG0='avg3')
	pset.renameArguments(ARG1='std3')
	pset.renameArguments(ARG2='min3')
	pset.renameArguments(ARG3='max3')
	
	#5 x 5 grids
	pset.renameArguments(ARG4='avg5')
	pset.renameArguments(ARG5='std5')
	pset.renameArguments(ARG6='min5')
	pset.renameArguments(ARG7='max5')

	#7 x 7 grids
	pset.renameArguments(ARG8='avg7')
	pset.renameArguments(ARG9='std7')
	pset.renameArguments(ARG10='min7')
	pset.renameArguments(ARG11='max7')
	
	#9 x 9 grids
	pset.renameArguments(ARG12='avg9')
	pset.renameArguments(ARG13='std9')
	pset.renameArguments(ARG14='min9')
	pset.renameArguments(ARG15='max9')
	
	#11 x 11 grids
	pset.renameArguments(ARG16='avg11')
	pset.renameArguments(ARG17='std11')
	pset.renameArguments(ARG18='min11')
	pset.renameArguments(ARG19='max11')
	
	#Other Initializations required for the GP to run. tree depth etc.
	creator.create("FitnessMin", base.Fitness, weights=(-1.0,)) #tell it to minimize fitness function score
	creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)
	toolbox = base.Toolbox()
	toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
	toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	toolbox.register("compile", gp.compile, pset=pset)

	#Fitness Function
	#this will go through all the test points in all of the 4 textures
	#and return a score based on that
	def evalTexture(individual):
		func = toolbox.compile(expr=individual)
		
		fitness_score = 0.0
		tp_count = 0.0
		tn_count = 0.0
		fp_count = 0.0
		fn_count = 0.0

		q1_scores = list()
		q2_scores = list()
		q3_scores = list()
		q4_scores = list()
		
		#01- avg3	05- avg5	09- avg7	13- avg9	17- avg11
		#02- std3	06- std5	10- std7	14- std9	18- std11
		#03- min3	07- min5	11- min7	15- min9	19- min11
		#04- max3	08- max5	12- max7	16- max9	20- max11
		

		for q in range(len(q1)):
			q1_scores.append(func(q1_avg3[q],
							q1_std3[q],
							q1_min3[q],
							q1_max3[q],
							q1_avg5[q],
							q1_std5[q],
							q1_min5[q],
							q1_max5[q],
							q1_avg7[q],
							q1_std7[q],
							q1_min7[q],
							q1_max7[q],
							q1_avg9[q],
							q1_std9[q],
							q1_min9[q],
							q1_max9[q],
							q1_avg11[q],
							q1_std11[q],
							q1_min11[q],
							q1_max11[q]))
		
		for q in range(len(q2)):
			q2_scores.append(func(q2_avg3[q],
							q2_std3[q],
							q2_min3[q],
							q2_max3[q],
							q2_avg5[q],
							q2_std5[q],
							q2_min5[q],
							q2_max5[q],
							q2_avg7[q],
							q2_std7[q],
							q2_min7[q],
							q2_max7[q],
							q2_avg9[q],
							q2_std9[q],
							q2_min9[q],
							q2_max9[q],
							q2_avg11[q],
							q2_std11[q],
							q2_min11[q],
							q2_max11[q]))
						
		for q in range(len(q3)):
			q3_scores.append(func(q3_avg3[q],
							q3_std3[q],
							q3_min3[q],
							q3_max3[q],
							q3_avg5[q],
							q3_std5[q],
							q3_min5[q],
							q3_max5[q],
							q3_avg7[q],
							q3_std7[q],
							q3_min7[q],
							q3_max7[q],
							q3_avg9[q],
							q3_std9[q],
							q3_min9[q],
							q3_max9[q],
							q3_avg11[q],
							q3_std11[q],
							q3_min11[q],
							q3_max11[q]))
		for q in range(len(q4)):
			q4_scores.append(func(q4_avg3[q],
							q4_std3[q],
							q4_min3[q],
							q4_max3[q],
							q4_avg5[q],
							q4_std5[q],
							q4_min5[q],
							q4_max5[q],
							q4_avg7[q],
							q4_std7[q],
							q4_min7[q],
							q4_max7[q],
							q4_avg9[q],
							q4_std9[q],
							q4_min9[q],
							q4_max9[q],
							q4_avg11[q],
							q4_std11[q],
							q4_min11[q],
							q4_max11[q]))

		if texToFind == 1:
			for score in q1_scores:
				if score >= 0:
					tp_count += 1
				else:
					fn_count += 1
			for score in q2_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
			for score in q2_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
			for score in q3_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
		if texToFind == 2:
			for score in q2_scores:
				if score >= 0:
					tp_count += 1
				else:
					fn_count += 1
			for score in q1_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
			for score in q3_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
			for score in q4_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
		
		if texToFind == 3:
			for score in q3_scores:
				if score >= 0:
					tp_count += 1
				else:
					fn_count += 1
			for score in q1_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
			for score in q2_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
			for score in q4_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
		
		if texToFind == 4:
			for score in q4_scores:
				if score >= 0:
					tp_count += 1
				else:
					fn_count += 1
			for score in q1_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
			for score in q2_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1
			for score in q3_scores:
				if score < 0:
					tn_count += 1
				else:
					fp_count += 1		
		
		
		#print "TP:" + str(tp_count) + " TN:" + str(tn_count) + " FN:" + str(fn_count) + " FP:" + str(fp_count)
		#fitness_score = fp_count + (fn_count * math.exp(10  * ((fn_count/(256 * 256)) - 0.6)))
		fitness_score = fp_count + fn_count
		return fitness_score,
		
	#Register GP toolbox object, maintains basic parameters of run
	toolbox.register("evaluate", evalTexture)
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
	mstats.register("avg", np.mean)
	mstats.register("std", np.std)
	mstats.register("min", np.min)
	mstats.register("max", np.max)
	
	#Conduct 1 Run
	print "Evolving 1 Run"
	pop, log = algorithms.eaSimple(pop, toolbox, probCross, probMutate, numberGens, stats=mstats,
                                   halloffame=hof, verbose=False)
	
	#Just print out hof for now
	print str(hof[0])
		
	#hof object is best GP individual found by the system. write that out with some other data
	#write these out as text files
	bhof = open("gp_found/best_seen.txt","a")
	bhof.write("texture: "+ str(texToFind) + " seed: " + str(seed) + " fitness: "+  str(hof[0].fitness) + "\n\n" + str(hof[0])+"\n\n")		
	#Write out HOF as Pickle so that it can be used during the image rendering process
	pickle.dump(hof[0],open("gp_found/tex_"+str(texToFind)+"_seed_"+str(seed)+".pkl" ,"wb"),-1)
		
	#write out logbooks of run, those contain detailed information about run
	if len(str(seed)) == 1:
		f = open("logs/tex_"+str(texToFind)+"_seed_0" + str(seed) + ".txt","w")
		f.write(str(log))
		f.close()
	else:
		f = open("logs/tex_"+str(texToFind)+"_seed_" + str(seed) + ".txt","w")
		f.write(str(log))
		f.close()

	print "Writing out testing data"
	#Write out the testing results testing/tex1
	#1 true positive
	#2 true negative
	#3 false postive
	#4 false negative
	
		#01- avg3	05- avg5	09- avg7	13- avg9	17- avg11
		#02- std3	06- std5	10- std7	14- std9	18- std11
		#03- min3	07- min5	11- min7	15- min9	19- min11
		#04- max3	08- max5	12- max7	16- max9	20- max11
	
	ffunc = toolbox.compile(expr=hof[0])
	t1_test = np.zeros(256 * 256).reshape(256,256)
	t2_test = np.zeros(256 * 256).reshape(256,256)
	t3_test = np.zeros(256 * 256).reshape(256,256)
	t4_test = np.zeros(256 * 256).reshape(256,256)
	
	if texToFind == 1:
		print "Testing Texture 1 (Want this one)"
		for x in range(255):			
			for y in range(255):				
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t1),
							f_min(3,x,y,t1),
							f_max(3,x,y,t1),
							f_avg(5,x,y,t1),
							f_std(5,x,y,t1),
							f_min(5,x,y,t1),
							f_max(5,x,y,t1),
							f_avg(7,x,y,t1),
							f_std(7,x,y,t1),
							f_min(7,x,y,t1),
							f_max(7,x,y,t1),
							f_avg(9,x,y,t1),
							f_std(9,x,y,t1),
							f_min(9,x,y,t1),
							f_max(9,x,y,t1),
							f_avg(11,x,y,t1),
							f_std(11,x,y,t1),
							f_min(11,x,y,t1),
							f_max(11,x,y,t1)) >= 0:
					t1_test[x][y] = 1
				else:
					t1_test[x][y] = 3
		print "Testing Texture 2"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t2),
							f_std(3,x,y,t2),
							f_min(3,x,y,t2),
							f_max(3,x,y,t2),
							f_avg(5,x,y,t2),
							f_std(5,x,y,t2),
							f_min(5,x,y,t2),
							f_max(5,x,y,t2),
							f_avg(7,x,y,t2),
							f_std(7,x,y,t2),
							f_min(7,x,y,t2),
							f_max(7,x,y,t2),
							f_avg(9,x,y,t2),
							f_std(9,x,y,t2),
							f_min(9,x,y,t2),
							f_max(9,x,y,t2),
							f_avg(11,x,y,t2),
							f_std(11,x,y,t2),
							f_min(11,x,y,t2),
							f_max(11,x,y,t2)) < 0:
					t2_test[x][y] = 2
				else:
					t2_test[x][y] = 4
		print "Testing Texture 3"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t3),
							f_std(3,x,y,t3),
							f_min(3,x,y,t3),
							f_max(3,x,y,t3),
							f_avg(5,x,y,t3),
							f_std(5,x,y,t3),
							f_min(5,x,y,t3),
							f_max(5,x,y,t3),
							f_avg(7,x,y,t3),
							f_std(7,x,y,t3),
							f_min(7,x,y,t3),
							f_max(7,x,y,t3),
							f_avg(9,x,y,t3),
							f_std(9,x,y,t3),
							f_min(9,x,y,t3),
							f_max(9,x,y,t3),
							f_avg(11,x,y,t3),
							f_std(11,x,y,t3),
							f_min(11,x,y,t3),
							f_max(11,x,y,t3)) < 0:
					t3_test[x][y] = 2
				else:
					t3_test[x][y] = 4
		print "Texting Texture 4"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t4),
							f_std(3,x,y,t4),
							f_min(3,x,y,t4),
							f_max(3,x,y,t4),
							f_avg(5,x,y,t4),
							f_std(5,x,y,t4),
							f_min(5,x,y,t4),
							f_max(5,x,y,t4),
							f_avg(7,x,y,t4),
							f_std(7,x,y,t4),
							f_min(7,x,y,t4),
							f_max(7,x,y,t4),
							f_avg(9,x,y,t4),
							f_std(9,x,y,t4),
							f_min(9,x,y,t4),
							f_max(9,x,y,t4),
							f_avg(11,x,y,t4),
							f_std(11,x,y,t4),
							f_min(11,x,y,t4),
							f_max(11,x,y,t4)) < 0:
					t4_test[x][y] = 2
				else:
					t4_test[x][y] = 4

	if texToFind == 2:
		print "Texting Texture 1"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t1),
							f_min(3,x,y,t1),
							f_max(3,x,y,t1),
							f_avg(5,x,y,t1),
							f_std(5,x,y,t1),
							f_min(5,x,y,t1),
							f_max(5,x,y,t1),
							f_avg(7,x,y,t1),
							f_std(7,x,y,t1),
							f_min(7,x,y,t1),
							f_max(7,x,y,t1),
							f_avg(9,x,y,t1),
							f_std(9,x,y,t1),
							f_min(9,x,y,t1),
							f_max(9,x,y,t1),
							f_avg(11,x,y,t1),
							f_std(11,x,y,t1),
							f_min(11,x,y,t1),
							f_max(11,x,y,t1)) < 0:
					t1_test[x][y] = 2
				else:
					t1_test[x][y] = 4
		print "Testing Texture 2 (Want this one)"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t2),
							f_std(3,x,y,t2),
							f_min(3,x,y,t2),
							f_max(3,x,y,t2),
							f_avg(5,x,y,t2),
							f_std(5,x,y,t2),
							f_min(5,x,y,t2),
							f_max(5,x,y,t2),
							f_avg(7,x,y,t2),
							f_std(7,x,y,t2),
							f_min(7,x,y,t2),
							f_max(7,x,y,t2),
							f_avg(9,x,y,t2),
							f_std(9,x,y,t2),
							f_min(9,x,y,t2),
							f_max(9,x,y,t2),
							f_avg(11,x,y,t2),
							f_std(11,x,y,t2),
							f_min(11,x,y,t2),
							f_max(11,x,y,t2)) >= 0:
					t2_test[x][y] = 1
				else:
					t2_test[x][y] = 3
		print "Testing Texture 3"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t3),
							f_std(3,x,y,t3),
							f_min(3,x,y,t3),
							f_max(3,x,y,t3),
							f_avg(5,x,y,t3),
							f_std(5,x,y,t3),
							f_min(5,x,y,t3),
							f_max(5,x,y,t3),
							f_avg(7,x,y,t3),
							f_std(7,x,y,t3),
							f_min(7,x,y,t3),
							f_max(7,x,y,t3),
							f_avg(9,x,y,t3),
							f_std(9,x,y,t3),
							f_min(9,x,y,t3),
							f_max(9,x,y,t3),
							f_avg(11,x,y,t3),
							f_std(11,x,y,t3),
							f_min(11,x,y,t3),
							f_max(11,x,y,t3)) < 0:
					t3_test[x][y] = 2
				else:
					t3_test[x][y] = 4
					
		print "Testing Texture 4"				
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t4),
							f_std(3,x,y,t4),
							f_min(3,x,y,t4),
							f_max(3,x,y,t4),
							f_avg(5,x,y,t4),
							f_std(5,x,y,t4),
							f_min(5,x,y,t4),
							f_max(5,x,y,t4),
							f_avg(7,x,y,t4),
							f_std(7,x,y,t4),
							f_min(7,x,y,t4),
							f_max(7,x,y,t4),
							f_avg(9,x,y,t4),
							f_std(9,x,y,t4),
							f_min(9,x,y,t4),
							f_max(9,x,y,t4),
							f_avg(11,x,y,t4),
							f_std(11,x,y,t4),
							f_min(11,x,y,t4),
							f_max(11,x,y,t4)) < 0:
					t4_test[x][y] = 2
				else:
					t4_test[x][y] = 4

	if texToFind == 3:
		print "Testing Texture 1"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t1),
							f_min(3,x,y,t1),
							f_max(3,x,y,t1),
							f_avg(5,x,y,t1),
							f_std(5,x,y,t1),
							f_min(5,x,y,t1),
							f_max(5,x,y,t1),
							f_avg(7,x,y,t1),
							f_std(7,x,y,t1),
							f_min(7,x,y,t1),
							f_max(7,x,y,t1),
							f_avg(9,x,y,t1),
							f_std(9,x,y,t1),
							f_min(9,x,y,t1),
							f_max(9,x,y,t1),
							f_avg(11,x,y,t1),
							f_std(11,x,y,t1),
							f_min(11,x,y,t1),
							f_max(11,x,y,t1)) < 0:
					t1_test[x][y] = 2
				else:
					t1_test[x][y] = 4
		print "Testing Texture 2"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t2),
							f_min(3,x,y,t2),
							f_max(3,x,y,t2),
							f_avg(5,x,y,t2),
							f_std(5,x,y,t2),
							f_min(5,x,y,t2),
							f_max(5,x,y,t2),
							f_avg(7,x,y,t2),
							f_std(7,x,y,t2),
							f_min(7,x,y,t2),
							f_max(7,x,y,t2),
							f_avg(9,x,y,t2),
							f_std(9,x,y,t2),
							f_min(9,x,y,t2),
							f_max(9,x,y,t2),
							f_avg(11,x,y,t2),
							f_std(11,x,y,t2),
							f_min(11,x,y,t2),
							f_max(11,x,y,t2)) < 0:
					t2_test[x][y] = 2
				else:
					t2_test[x][y] = 4
		print "Testing Texture 3 (Want this one)"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t3),
							f_min(3,x,y,t3),
							f_max(3,x,y,t3),
							f_avg(5,x,y,t3),
							f_std(5,x,y,t3),
							f_min(5,x,y,t3),
							f_max(5,x,y,t3),
							f_avg(7,x,y,t3),
							f_std(7,x,y,t3),
							f_min(7,x,y,t3),
							f_max(7,x,y,t3),
							f_avg(9,x,y,t3),
							f_std(9,x,y,t3),
							f_min(9,x,y,t3),
							f_max(9,x,y,t3),
							f_avg(11,x,y,t3),
							f_std(11,x,y,t3),
							f_min(11,x,y,t3),
							f_max(11,x,y,t3)) >= 0:
					t3_test[x][y] = 1
				else:
					t3_test[x][y] = 3
		print "Testing Texture 4"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t4),
							f_min(3,x,y,t4),
							f_max(3,x,y,t4),
							f_avg(5,x,y,t4),
							f_std(5,x,y,t4),
							f_min(5,x,y,t4),
							f_max(5,x,y,t4),
							f_avg(7,x,y,t4),
							f_std(7,x,y,t4),
							f_min(7,x,y,t4),
							f_max(7,x,y,t4),
							f_avg(9,x,y,t4),
							f_std(9,x,y,t4),
							f_min(9,x,y,t4),
							f_max(9,x,y,t4),
							f_avg(11,x,y,t4),
							f_std(11,x,y,t4),
							f_min(11,x,y,t4),
							f_max(11,x,y,t4)) < 0:
					t4_test[x][y] = 2
				else:
					t4_test[x][y] = 4

	if texToFind == 4:
		print "Testing Texture 4"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t1),
							f_min(3,x,y,t1),
							f_max(3,x,y,t1),
							f_avg(5,x,y,t1),
							f_std(5,x,y,t1),
							f_min(5,x,y,t1),
							f_max(5,x,y,t1),
							f_avg(7,x,y,t1),
							f_std(7,x,y,t1),
							f_min(7,x,y,t1),
							f_max(7,x,y,t1),
							f_avg(9,x,y,t1),
							f_std(9,x,y,t1),
							f_min(9,x,y,t1),
							f_max(9,x,y,t1),
							f_avg(11,x,y,t1),
							f_std(11,x,y,t1),
							f_min(11,x,y,t1),
							f_max(11,x,y,t1)) < 0:
					t1_test[x][y] = 2
				else:
					t1_test[x][y] = 4
		print "Testing Texture 2"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t2),
							f_min(3,x,y,t2),
							f_max(3,x,y,t2),
							f_avg(5,x,y,t2),
							f_std(5,x,y,t2),
							f_min(5,x,y,t2),
							f_max(5,x,y,t2),
							f_avg(7,x,y,t2),
							f_std(7,x,y,t2),
							f_min(7,x,y,t2),
							f_max(7,x,y,t2),
							f_avg(9,x,y,t2),
							f_std(9,x,y,t2),
							f_min(9,x,y,t2),
							f_max(9,x,y,t2),
							f_avg(11,x,y,t2),
							f_std(11,x,y,t2),
							f_min(11,x,y,t2),
							f_max(11,x,y,t2)) < 0:
					t2_test[x][y] = 2
				else:
					t2_test[x][y] = 4
		print "Testing Texture 3"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t3),
							f_min(3,x,y,t3),
							f_max(3,x,y,t3),
							f_avg(5,x,y,t3),
							f_std(5,x,y,t3),
							f_min(5,x,y,t3),
							f_max(5,x,y,t3),
							f_avg(7,x,y,t3),
							f_std(7,x,y,t3),
							f_min(7,x,y,t3),
							f_max(7,x,y,t3),
							f_avg(9,x,y,t3),
							f_std(9,x,y,t3),
							f_min(9,x,y,t3),
							f_max(9,x,y,t3),
							f_avg(11,x,y,t3),
							f_std(11,x,y,t3),
							f_min(11,x,y,t3),
							f_max(11,x,y,t3)) < 0:
					t3_test[x][y] = 2
				else:
					t3_test[x][y] = 4
		print "Testing Texture 4 (Want this one)"
		for x in range(255):			
			for y in range(255):
				if ffunc(f_avg(3,x,y,t1),
							f_std(3,x,y,t4),
							f_min(3,x,y,t4),
							f_max(3,x,y,t4),
							f_avg(5,x,y,t4),
							f_std(5,x,y,t4),
							f_min(5,x,y,t4),
							f_max(5,x,y,t4),
							f_avg(7,x,y,t4),
							f_std(7,x,y,t4),
							f_min(7,x,y,t4),
							f_max(7,x,y,t4),
							f_avg(9,x,y,t4),
							f_std(9,x,y,t4),
							f_min(9,x,y,t4),
							f_max(9,x,y,t4),
							f_avg(11,x,y,t4),
							f_std(11,x,y,t4),
							f_min(11,x,y,t4),
							f_max(11,x,y,t4)) >= 0:
					t4_test[x][y] = 1
				else:
					t4_test[x][y] = 3



	pickle.dump(t1_test, open("testing/tex"+str(texToFind)+"_"+str(seed)+"_q1.pkl","wb"))
	pickle.dump(t2_test, open("testing/tex"+str(texToFind)+"_"+str(seed)+"_q2.pkl","wb"))
	pickle.dump(t3_test, open("testing/tex"+str(texToFind)+"_"+str(seed)+"_q3.pkl","wb"))
	pickle.dump(t4_test, open("testing/tex"+str(texToFind)+"_"+str(seed)+"_q4.pkl","wb"))

if __name__ == "__main__":
	main()
