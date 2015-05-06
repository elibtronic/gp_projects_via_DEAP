# Plots out adjusted fitness found for 
# best GP for each training set size

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.5971426434,0.520686117,0.5175759856,0.517541953,0.5082332811,0.5265935557,0.5398494487,0.5278278309,0.547473304,0.5566725227])

ind = np.arange(10)
width = 0.70
fig,ax = plt.subplots()
#rects1 = ax.bar(ind, x, width, color='r',yerr=e)
rects = ax.bar(ind, x, width, color='b')
ax.set_xticks(ind+0.4)
ax.set_ylim([0.45, 0.65])
ax.set_title("\nFitness of Best Genetic Program Found Per Training Set Size\n")
ax.set_ylabel("Adjusted Fitness per Country Score")
ax.set_xlabel("\nTraining Set Percentage Size")
ax.set_xticklabels(('5%','10%','15%','20%','25%','30%','35%','40%','45%','50%'))
plt.show()
