# Plots out Training Scores for 
# best GP for each training set size

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.084556213,0.1315177515,0.1088645628,0.0968287722,0.0897947929,0.0765664037,0.0664137181,0.0657290703,0.0585985098,0.0523540003])

ind = np.arange(10)
width = 0.70
fig,ax = plt.subplots()
#rects1 = ax.bar(ind, x, width, color='r',yerr=e)
rects = ax.bar(ind, x, width, color='g')
ax.set_xticks(ind+0.4)
ax.set_ylim([0.0, 0.8])
ax.set_title("\nTraining Score Average Error\n")
ax.set_ylabel("Average Error")
ax.set_xlabel("\nTraining Set Percentage Size")
ax.set_xticklabels(('5%','10%','15%','20%','25%','30%','35%','40%','45%','50%'))
plt.show()
