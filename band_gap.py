import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eigh
from scipy.linalg import ishermitian
import matplotlib.pyplot as plt

import pandas as pd                                                                
import pyarrow as pa                                                               
import pyarrow.parquet as pq 

N=240

u=np.ones((3,int(N/3)))
print(u)
un=np.ones(int(N/6))
def Hamiltonian_OBC(J):
    H=np.zeros((N,N),dtype=np.complex64)
    # H[1,1]=1j
    for im in range(int(N/3)):
        i=im*3
        ###########################
        #sysy coupling            #
        ###########################
        # print('yy:',i,i+1,im)
        H[i][i+1]=J[1]*u[1][im]
        H[i+1][i]=J[1]*u[1][im]
        if i%6==0:
            #######################
            #szsz coupling        #
            #######################
            j=i+5
            # print('zz:',i,j,im)
            H[i,j]=J[2]*u[2][im]
            H[j,i]=J[2]*u[2][im]
            #######################
            #sxsx coupling        #
            #######################
            # j=(i+6)%N  #######################PBC CONDITION###################
            # print('xxn:',i+3,j,im)
            # H[i+3,j]=J[0]*un[int(im/2)]
            # H[j,i+3]=J[0]*un[int(im/2)]
            j=i+6      #######################OBC CONDITION###################
            if j<N:    #######################OBC CONDITION###################
                # print('xx:',i+3,j)
                H[i+3,j]=J[0]*un[int(im/2)]
                H[j,i+3]=J[0]*un[int(im/2)]
        else:
            #######################
            #szsz coupling        #
            #######################
            j=i-1
            # print('zz:',i,j,im)
            H[i,j]=J[2]*u[2][im]
            H[j,i]=J[2]*u[2][im]
            #######################
            #sxsx coupling        #
            #######################
            j=(i+2)%N
            # print('xx:',i+1,j,im)
            H[i+1,j]=J[0]*u[0][im]
            H[j,i+1]=J[0]*u[0][im]
            # print('xx:',i-2,j-3,im-1)
            H[i-2,j-3]=J[0]*u[0][im-1]
            H[j-3,i-2]=J[0]*u[0][im-1]
    return H

for ij in range(25):
    J=[1+ij/50,1,1]
    f=open("./data/o"+str(50+ij)+".dat",'w')
    for k in range(2*nc):
        H=Hamiltonian_OBC(J)
        # print(H.imag)
        # print(ishermitian(H))
        eigvals, eigenvectors = eigh(H)
        # f.write(str(J[0])+"\t")
        for i in range(len(eigvals)):
            f.write(str(J[0])+"\t"+str(eigvals[i])+"\n")
    f.close()

gap=[]
jv=[]
for i in range(200):
    x1=np.loadtxt("./data/o"+str(i)+".dat")
    y=x1[:,1]
    pos_val = np.min(y[y >= 0])
    neg_val = np.max(y[y <= 0])
    # print(x1[0,0],pos_val,neg_val)
    jv.append(x1[0,0])
    gap.append(2*pos_val)


gap2=[]
jv2=[]
for i in range(200):
    x1=np.loadtxt("./data/e"+str(i)+".dat")
    y3=x1[:,4]
    y4=x1[:,5]
    jv2.append(x1[0,0])
    gap2.append(y4.min()-y3.max())
plt.plot(jv2,gap2)
plt.plot(jv,gap)
# plt.xlim([0,50])
# plt.ylim([0,10])
plt.show()
