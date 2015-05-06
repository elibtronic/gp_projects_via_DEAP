
# Analyzes the data accumulated for Part A
# Draws two figures, the average and best fitness of each parameter set
# needs the matplotlib package to generate the graphs
# change flag 1 or 2 depending on which paramSet you want to plot
# Derived from http://deap.gel.ulaval.ca/doc/default/tutorials/basic/part3.html
#

from deap import tools
import matplotlib.pyplot as plt
import sys

flag = 2
pfitAvg = list( float(l.strip('\n')) for l in open("AVG_"+str(flag)+".txt","r"))
pfitBest = list( float(l.strip('\n')) for l in open("BEST_"+str(flag)+".txt","r"))

#Automatically scales the axes
plt.plot(pfitBest, "g.-", label="Best" )
plt.plot(pfitAvg, "b*-", label="Average")
plt.ylabel("Adjusted Fitness")
plt.xlabel("Generation")
plt.axis([0,50,0, 1.05])
plt.legend(loc="lower right")
plt.show()
