
# Analyzes the data accumulated for Part A
# Draws two figures, the average and best fitness of each parameter set
# needs the matplotlib package to generate the graphs
# change flag to red for red wine, flag to white for white wine
# Derived from http://deap.gel.ulaval.ca/doc/default/tutorials/basic/part3.html
#

from deap import tools
import matplotlib.pyplot as plt
import sys

flag = "white"

pfitAvg = list( float(l.strip('\n')) for l in open("AVG_"+str(flag)+".txt","r"))
pfitBest = list( float(l.strip('\n')) for l in open("BEST_"+str(flag)+".txt","r"))

#Automatically scales the axes
plt.plot(pfitBest, "g.-", label="Best" )
plt.plot(pfitAvg, "b*-", label="Average")
plt.ylabel("Inverse Logrithmic Fitness")
plt.xlabel("Generation")
plt.axis([0,200,0, 0.5])
plt.legend(loc="upper left")
plt.show()
