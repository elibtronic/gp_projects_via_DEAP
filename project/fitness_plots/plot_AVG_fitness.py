# Derived from http://deap.gel.ulaval.ca/doc/default/tutorials/basic/part3.html
# Plots either the 35 or 50 training set size logarithmic adjusted fitness score

from deap import tools
import matplotlib.pyplot as plt
import sys

pfitAvg1 = list( float(l.strip('\n')) for l in open("35_AVG_log.txt","r"))
pfitAvg2 = list( float(l.strip('\n')) for l in open("50_AVG_log.txt","r"))
plt.plot(pfitAvg1, "g.-", label="35% Training Set" )
#plt.plot(pfitAvg2, "bx-", label="50% Training Set")

plt.title("Logarithmic Average of all GP")
plt.ylabel("Log of Raw Fitness")
plt.xlabel("Generation")
plt.legend(loc="upper right")
plt.show()
