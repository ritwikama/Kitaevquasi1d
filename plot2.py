import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eigh
from scipy.linalg import ishermitian
import matplotlib.pyplot as plt

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


from matplotlib.ticker import MultipleLocator

cmap = plt.cm.plasma
colors = [cmap(i) for i in np.linspace(0, 1, 6)]
xa=np.linspace(0,239,240)
x1=np.loadtxt("func_1_-1-111_20.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
plt.scatter(xa,xb**2,color=colors[0], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[0], linewidth=2)
plt.scatter(xa,yb**2,color=colors[0], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[0], linewidth=2)

x1=np.loadtxt("func_1_-1-111_15.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
plt.scatter(xa,xb**2,color=colors[1], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[1], linewidth=2)
plt.scatter(xa,yb**2,color=colors[1], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[1], linewidth=2)

x1=np.loadtxt("func_1_-1-111_10.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
plt.scatter(xa,xb**2,color=colors[2], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[2], linewidth=2)
plt.scatter(xa,yb**2,color=colors[2], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[2], linewidth=2)

x1=np.loadtxt("func_1_-1-111_5.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
plt.scatter(xa,xb**2,color=colors[3], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[3], linewidth=2)
plt.scatter(xa,yb**2,color=colors[3], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[3], linewidth=2)

x1=np.loadtxt("func_1_-1-111_0.dat")#,dtype=str)
xb=x1[:,0]/np.sqrt(1.9)
yb=x1[:,2]/np.sqrt(1.9)
plt.scatter(xa,xb**2,color=colors[4], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[4], linewidth=2)
plt.scatter(xa,yb**2,color=colors[4], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[4], linewidth=2)

plt.gca().xaxis.set_major_locator(MultipleLocator(60))
plt.gca().xaxis.set_minor_locator(MultipleLocator(20))
plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.02))
plt.tick_params(axis='y', which='major', length=10, width=2)#, direction='in')   # major ticks
plt.tick_params(axis='y', which='minor', length=5, width=2,)#, direction='in')   # minor ticks
plt.tick_params(axis='x', which='major', length=10, width=2, direction='in')   # major ticks
plt.tick_params(axis='x', which='minor', length=5, width=2, direction='in')   # minor ticks
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi/6$',r'$-\pi/12$',r'0',r'$\pi/12$',r'$\pi/6$'])
plt.xlim([0,240])
plt.ylim([0,0.25])
plt.savefig("func_1_-1-111_trans.png",dpi=600)
plt.show()

cmap = plt.cm.plasma
colors = [cmap(i) for i in np.linspace(0, 1, 6)]
xa=np.linspace(0,239,240)

x1=np.loadtxt("func_1_-1-111_1s.dat")#,dtype=str)
xb=x1[:,0]#/np.sqrt(1.9)
yb=x1[:,2]#/np.sqrt(1.9)
plt.scatter(xa,xb**2,color=colors[0], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[0], linewidth=2)
plt.scatter(xa,yb**2,color=colors[0], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[0], linewidth=2)

x1=np.loadtxt("func_1_-1-111_2s.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
plt.scatter(xa,xb**2,color=colors[1], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[1], linewidth=2)
plt.scatter(xa,yb**2,color=colors[1], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[1], linewidth=2)

x1=np.loadtxt("func_1_-1-111_4s.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
plt.scatter(xa,xb**2,color=colors[2], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[2], linewidth=2)
plt.scatter(xa,yb**2,color=colors[2], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[2], linewidth=2)

x1=np.loadtxt("func_1_-1-111_10s.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
plt.scatter(xa,xb**2,color=colors[3], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[3], linewidth=2)
plt.scatter(xa,yb**2,color=colors[3], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[3], linewidth=2)

x1=np.loadtxt("func_1_-1-111_20s.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
plt.scatter(xa,xb**2,color=colors[4], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[4], linewidth=2)
plt.scatter(xa,yb**2,color=colors[4], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[4], linewidth=2)

plt.gca().xaxis.set_major_locator(MultipleLocator(60))
plt.gca().xaxis.set_minor_locator(MultipleLocator(20))
plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.02))
plt.tick_params(axis='y', which='major', length=10, width=2)#, direction='in')   # major ticks
plt.tick_params(axis='y', which='minor', length=5, width=2,)#, direction='in')   # minor ticks
plt.tick_params(axis='x', which='major', length=10, width=2, direction='in')   # major ticks
plt.tick_params(axis='x', which='minor', length=5, width=2, direction='in')   # minor ticks
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi/6$',r'$-\pi/12$',r'0',r'$\pi/12$',r'$\pi/6$'])
plt.xlim([0,240])
# plt.ylim([0,0.2])
plt.savefig("func_1_-1-111_squeeze.png",dpi=600)
plt.show()

cmap = plt.cm.plasma
colors = [cmap(i) for i in np.linspace(0, 1, 6)]
xa=np.linspace(0,239,240)

x1=np.loadtxt("func_1_-1-111_2dw.dat")#,dtype=str)
xb=x1[:,0]#/np.sqrt(1.9)
yb=x1[:,2]#/np.sqrt(1.9)
plt.scatter(xa,xb**2,color=colors[0], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[0], linewidth=2)
plt.scatter(xa,yb**2,color=colors[0], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[0], linewidth=2)

x1=np.loadtxt("func_1_-1-111_4dw.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
xc=x1[:,4]
yc=x1[:,6]
plt.scatter(xa,xb**2,color=colors[1], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[1], linewidth=2)
plt.scatter(xa,yb**2,color=colors[1], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[1], linewidth=2)
plt.scatter(xa,xc**2,color=colors[1], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xc**2,color=colors[1], linewidth=2)
plt.scatter(xa,yc**2,color=colors[1], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yc**2,color=colors[1], linewidth=2)

x1=np.loadtxt("func_1_-1-111_6dw.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
xc=x1[:,4]
yc=x1[:,6]
xd=x1[:,8]
yd=x1[:,10]
plt.scatter(xa,xb**2,color=colors[2], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[2], linewidth=2)
plt.scatter(xa,yb**2,color=colors[2], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[2], linewidth=2)
plt.scatter(xa,xc**2,color=colors[2], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xc**2,color=colors[2], linewidth=2)
plt.scatter(xa,yc**2,color=colors[2], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yc**2,color=colors[2], linewidth=2)
plt.scatter(xa,xd**2,color=colors[2], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xd**2,color=colors[2], linewidth=2)
plt.scatter(xa,yd**2,color=colors[2], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yd**2,color=colors[2], linewidth=2)

x1=np.loadtxt("func_1_-1-111_8dw.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
xc=x1[:,4]
yc=x1[:,6]
xd=x1[:,8]
yd=x1[:,10]
xe=x1[:,12]
ye=x1[:,14]
plt.scatter(xa,xb**2,color=colors[3], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[3], linewidth=2)
plt.scatter(xa,yb**2,color=colors[3], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[3], linewidth=2)
plt.scatter(xa,xc**2,color=colors[3], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xc**2,color=colors[3], linewidth=2)
plt.scatter(xa,yc**2,color=colors[3], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yc**2,color=colors[3], linewidth=2)
plt.scatter(xa,xd**2,color=colors[3], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xd**2,color=colors[3], linewidth=2)
plt.scatter(xa,yd**2,color=colors[3], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yd**2,color=colors[3], linewidth=2)
plt.scatter(xa,xe**2,color=colors[3], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xe**2,color=colors[3], linewidth=2)
plt.scatter(xa,ye**2,color=colors[3], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,ye**2,color=colors[3], linewidth=2)

x1=np.loadtxt("func_1_-1-111_10dw.dat")#,dtype=str)
xb=x1[:,0]
yb=x1[:,2]
xc=x1[:,4]
yc=x1[:,6]
xd=x1[:,8]
yd=x1[:,10]
xe=x1[:,12]
ye=x1[:,14]
xf=x1[:,16]
yf=x1[:,18]
plt.scatter(xa,xb**2,color=colors[4], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xb**2,color=colors[4], linewidth=2)
plt.scatter(xa,yb**2,color=colors[4], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yb**2,color=colors[4], linewidth=2)
plt.scatter(xa,xc**2,color=colors[4], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xc**2,color=colors[4], linewidth=2)
plt.scatter(xa,yc**2,color=colors[4], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yc**2,color=colors[4], linewidth=2)
plt.scatter(xa,xd**2,color=colors[4], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xd**2,color=colors[4], linewidth=2)
plt.scatter(xa,yd**2,color=colors[4], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,yd**2,color=colors[4], linewidth=2)
plt.scatter(xa,xe**2,color=colors[4], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xe**2,color=colors[4], linewidth=2)
plt.scatter(xa,ye**2,color=colors[4], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,ye**2,color=colors[4], linewidth=2)
plt.scatter(xa,xe**2,color=colors[4], s=30,marker='o')#, edgecolors='black')
plt.plot(xa,xe**2,color=colors[4], linewidth=2)
plt.scatter(xa,ye**2,color=colors[4], s=30,marker='*')#, edgecolors='black')
plt.plot(xa,ye**2,color=colors[4], linewidth=2)

plt.gca().xaxis.set_major_locator(MultipleLocator(60))
plt.gca().xaxis.set_minor_locator(MultipleLocator(20))
plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.02))
plt.tick_params(axis='y', which='major', length=10, width=2)#, direction='in')   # major ticks
plt.tick_params(axis='y', which='minor', length=5, width=2,)#, direction='in')   # minor ticks
plt.tick_params(axis='x', which='major', length=10, width=2, direction='in')   # major ticks
plt.tick_params(axis='x', which='minor', length=5, width=2, direction='in')   # minor ticks
# plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi/6$',r'$-\pi/12$',r'0',r'$\pi/12$',r'$\pi/6$'])
plt.xlim([0,240])
# plt.ylim([0,0.2])
plt.savefig("func_1_-1-111_dw.png",dpi=600)
plt.show()

