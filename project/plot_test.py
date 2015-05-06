# Plots out Testing Scores for 
# best GP for each training set size

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.7194018751,0.2146809235,0.0705646457,0.065682173,0.2959904467,0.0717091284,0.064613737,0.0913599606,0.1010617284,0.0828135503])

ind = np.arange(10)
width = 0.70
fig,ax = plt.subplots()
#rects1 = ax.bar(ind, x, width, color='r',yerr=e)
rects = ax.bar(ind, x, width, color='brown')
ax.set_xticks(ind+0.4)
ax.set_ylim([0.0, 0.8])
ax.set_title("\nTesting Score Average Error\n")
ax.set_ylabel("Average Error")
ax.set_xlabel("\nTraining Set Percentage Size")
ax.set_xticklabels(('5%','10%','15%','20%','25%','30%','35%','40%','45%','50%'))
plt.show()
