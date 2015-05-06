# Plots out Score Ratio 
# best GP for each training set size

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0.117536826,0.6126196466,1.5427635421,1.474201716,0.303370578,1.0677358019,1.0278575611,0.7194516055,0.5798288896,0.6321912315])


ind = np.arange(10)
width = 0.70
fig,ax = plt.subplots()
#rects1 = ax.bar(ind, x, width, color='r',yerr=e)
rects = ax.bar(ind, x, width, color='purple')
ax.set_xticks(ind+0.4)
ax.set_ylim([0.0, 2.0])
ax.set_title("\nTraining to Test Error Ratio\n")
ax.set_ylabel("Error Ratio")
ax.set_xlabel("\nTraining Set Percentage Size")
ax.set_xticklabels(('5%','10%','15%','20%','25%','30%','35%','40%','45%','50%'))
plt.show()
