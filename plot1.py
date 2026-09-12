import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eigh
from scipy.linalg import ishermitian
import matplotlib.pyplot as plt

import pandas as pd                                                                
import pyarrow as pa                                                               
import pyarrow.parquet as pq 


from matplotlib.ticker import MultipleLocator
# colour=['red','orange','darkgreen','deepskyblue','mediumblue','fuchsia','magenta']
cmap = plt.cm.bwr
colors = [cmap(i) for i in np.linspace(0, 1, 6)]
# xb=x1[:,0]
# yb=x1[:,2]
# for i in range(len(xb)):
#     s=yb[i]
#     clean = s.split(")")[0].strip("()")

#     # Convert to complex and take real part
#     val = complex(clean).real
#     yb[i]=val
# xb=xb.astype(float)

x2=np.loadtxt("eig_1414_-1-111_10")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[0], s=20,marker='s')#, edgecolors='black')
x2=np.loadtxt("eig_1414_-1-111_20")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[2], s=20,marker='o')#, edgecolors='black')
x2=np.loadtxt("eig_1414_-1-111_4")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[5], s=20,marker='>')#, edgecolors='black')
plt.gca().xaxis.set_major_locator(MultipleLocator(60))
plt.gca().xaxis.set_minor_locator(MultipleLocator(20))
plt.gca().yaxis.set_major_locator(MultipleLocator(2))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.5))
plt.tick_params(axis='y', which='major', length=10, width=2)#, direction='in')   # major ticks
plt.tick_params(axis='y', which='minor', length=5, width=2,)#, direction='in')   # minor ticks
plt.tick_params(axis='x', which='major', length=10, width=2, direction='in')   # major ticks
plt.tick_params(axis='x', which='minor', length=5, width=2, direction='in')   # minor ticks
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi/6$',r'$-\pi/12$',r'0',r'$\pi/12$',r'$\pi/6$'])
plt.xlim([0,240])
plt.ylim([-2,2])
plt.gca().set_aspect(18)
plt.savefig("en_1414_-1-111.png",dpi=600)
plt.show()

cmap = plt.cm.bwr
colors = [cmap(i) for i in np.linspace(0, 1, 6)]
# xb=x1[:,0]
# yb=x1[:,2]
# for i in range(len(xb)):
#     s=yb[i]
#     clean = s.split(")")[0].strip("()")

#     # Convert to complex and take real part
#     val = complex(clean).real
#     yb[i]=val
# xb=xb.astype(float)

# x2=np.loadtxt("eig_2_-1-111_10")
# xa=np.linspace(0,239,240)
# ya=x2[:]
# plt.scatter(xa,ya,color=colors[0], s=20,marker='s')#, edgecolors='black')
x2=np.loadtxt("eig_2_-1-111_20")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[0], s=15,marker='o')#, edgecolors='black')
x2=np.loadtxt("eig_2_-1-111_4")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[4], s=15,marker='*')#, edgecolors='black')
plt.gca().xaxis.set_major_locator(MultipleLocator(60))
plt.gca().xaxis.set_minor_locator(MultipleLocator(20))
plt.gca().yaxis.set_major_locator(MultipleLocator(3))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.5))
plt.tick_params(axis='y', which='major', length=10, width=2)#, direction='in')   # major ticks
plt.tick_params(axis='y', which='minor', length=5, width=2,)#, direction='in')   # minor ticks
plt.tick_params(axis='x', which='major', length=10, width=2, direction='in')   # major ticks
plt.tick_params(axis='x', which='minor', length=5, width=2, direction='in')   # minor ticks
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi/6$',r'$-\pi/12$',r'0',r'$\pi/12$',r'$\pi/6$'])
plt.xlim([0,240])
# plt.ylim([-3,3])
plt.gca().set_aspect(12)
plt.savefig("en_2_-1-111.png",dpi=600)
plt.show()


