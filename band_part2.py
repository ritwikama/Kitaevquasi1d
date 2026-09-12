import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eigh
from scipy.linalg import ishermitian
import matplotlib.pyplot as plt

import pandas as pd                                                                
import pyarrow as pa                                                               
import pyarrow.parquet as pq 

from matplotlib.ticker import MultipleLocator

iv=1.5#np.sqrt(2)#1
# colour=['red','orange','green','blue','indigo','violet']
# colour=['brown','red','orange','green','mediumblue','midnightblue']
# colour=['darkviolet','orangered','orange','green','mediumblue','crimson']
# colour=['crimson','orangered','orange','green','mediumblue','darkviolet']
colour=['red','gold','darkgreen','deepskyblue','mediumblue','fuchsia','magenta']
file="bandyz"+str(iv)+".dat"
x1=np.loadtxt(file)
x=x1[:,0]
y1=x1[:,1]
y2=x1[:,2]
y3=x1[:,3]
y4=x1[:,4]
y5=x1[:,5]
y6=x1[:,6]
plt.plot(x,y1,color=colour[0], linewidth=2)
plt.plot(x,y2,color=colour[1], linewidth=2)
plt.plot(x,y3,color=colour[2], linewidth=2)
plt.plot(x,y4,color=colour[3], linewidth=2)
plt.plot(x,y5,color=colour[4], linewidth=2)
plt.plot(x,y6,color=colour[5], linewidth=2)
plt.gca().xaxis.set_major_locator(MultipleLocator(np.pi/2))
plt.gca().xaxis.set_minor_locator(MultipleLocator(np.pi/4))
plt.gca().yaxis.set_major_locator(MultipleLocator(1))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.5))
plt.tick_params(axis='both', which='major', length=10, width=2)   # major ticks
plt.tick_params(axis='both', which='minor', length=5, width=2)   # minor ticks
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi/6$',r'$-\pi/12$',r'0',r'$\pi/12$',r'$\pi/6$'])
plt.xlim([-np.pi,np.pi])
plt.savefig("bandplotyz"+str(iv)+".png",dpi=600)
plt.show()
