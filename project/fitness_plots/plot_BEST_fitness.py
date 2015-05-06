# Derived from http://deap.gel.ulaval.ca/doc/default/tutorials/basic/part3.html
# Plots either the 35 or 50 training set size best GP found

from deap import tools
import matplotlib.pyplot as plt
import sys

pfitBest1 = list( float(l.strip('\n')) for l in open("35_BEST.txt","r"))
pfitBest2 = list( float(l.strip('\n')) for l in open("50_BEST.txt","r"))
plt.plot(pfitBest1, "g", label="35% Training Set" )
plt.plot(pfitBest2, "b--", label="50% Training Set")


plt.title("BEST GP Found For Training Set")
plt.ylabel("Raw Fitness")
plt.xlabel("Generation")
plt.legend(loc="upper right")
plt.show()
