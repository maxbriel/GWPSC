import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt


fig, ax = plt.subplots(1,1,figsize=(10,10))

ax.plot(np.arange(0,10,1), np.arange(10,20,1))

ax.set_xlabel('M$_1$')
ax.set_ylabel(r'd$R$/dM$_1$ [Gpc$^{-3}$ yr$^{-1}$]')

plt.savefig('comparison_plots/BPASS/test.pdf',bbox_inches='tight')
