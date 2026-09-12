import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eigh
from scipy.linalg import ishermitian
import matplotlib.pyplot as plt

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


from matplotlib.ticker import MultipleLocator

x2=np.loadtxt("eig_1_-1-111_10dw")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[4], s=35,marker='s')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_8dw")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[3], s=35,marker='o')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_6dw")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[2], s=35,marker='>')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_4dw")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[1], s=35,marker='*')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_2")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[0], s=35,marker='^')#, edgecolors='black')
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
plt.ylim([-3,3])
plt.savefig("en_1_-1-111_dw_szoom.png",dpi=600)
plt.show()

x2=np.loadtxt("eig_1_-1-111_10dw")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[4], s=45,marker='s')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_8dw")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[3], s=45,marker='o')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_6dw")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[2], s=45,marker='>')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_4dw")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[1], s=45,marker='*')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_2")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[0], s=40,marker='^')#, edgecolors='black')
plt.gca().xaxis.set_major_locator(MultipleLocator(20))
plt.gca().xaxis.set_minor_locator(MultipleLocator(10))
plt.gca().yaxis.set_major_locator(MultipleLocator(1))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.5))
plt.tick_params(axis='y', which='major', length=15, width=2, direction='in')   # major ticks
plt.tick_params(axis='y', which='minor', length=10, width=2, direction='in')   # minor ticks
plt.tick_params(axis='x', which='major', length=15, width=2, direction='in')   # major ticks
plt.tick_params(axis='x', which='minor', length=10, width=2, direction='in')   # minor ticks
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi/6$',r'$-\pi/12$',r'0',r'$\pi/12$',r'$\pi/6$'])
plt.xlim([100,140])
plt.ylim([-1,1])
plt.savefig("en_1_-1-111_dw_zoom.png",dpi=600)
plt.show()

x2=np.loadtxt("eig_1_-1-111_1")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[0], s=20,marker='s')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_2")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[1], s=20,marker='o')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_4")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[2], s=20,marker='>')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_10")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[3], s=20,marker='*')#, edgecolors='black')
x2=np.loadtxt("eig_1_-1-111_20")
xa=np.linspace(0,239,240)
ya=x2[:]
plt.scatter(xa,ya,color=colors[4], s=20,marker='^')#, edgecolors='black')
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
plt.ylim([-3,3])
plt.savefig("en_1_-1-111.png",dpi=600)
plt.show()

