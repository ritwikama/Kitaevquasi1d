import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eigh
from scipy.linalg import ishermitian
import matplotlib.pyplot as plt

import pandas as pd                                                                
import pyarrow as pa                                                               
import pyarrow.parquet as pq 

N=6

# J=[np.sqrt(2),1,1]
J=[np.sqrt(2),1.5,1]
# J=[1/np.sqrt(2),1,1]
# u=np.ones((3,int(N/3)))
u=np.array([np.array([1,1,1,1,1,1]),np.array([1,1,1,1,1,1]),np.array([1,1,1,1,1,1])])
# u=np.array([np.array([1,1,1,1,1,1]),np.array([1,1,1,1,1,1]),np.array([-1,1,-1,1,-1,1])])
print(u)
un=np.ones(int(N/6))
# un=np.array([-1])#,-1,1,-1,1,-1,1,-1,1,-1])
eig=[]
# file=open("band"+str(J[0])+".dat",'w')
file=open("bandyz"+str(J[1])+".dat",'w')
nc=240
for k in range(2*nc):
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
            j=(i+6)%N  #######################PBC CONDITION###################
            # print('xxn:',i+3,j,im)
            # print(J[0]*un[int(im/2)]*np.exp(1j*k*np.pi/20) )
            H[i+3,j]=J[0]*un[int(im/2)]*np.exp(1j*(k-nc)*np.pi/nc)
            H[j,i+3]=J[0]*un[int(im/2)]*np.exp(-1j*(k-nc)*np.pi/nc)
            # j=i+6      #######################OBC CONDITION###################
            # if j<L:    #######################OBC CONDITION###################
                # print('xx:',i+3,j)
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

    # print(H.real)
    # print(ishermitian(H))
    eigenvalues, eigenvectors = eigh(H)
    eig.append(eigenvalues)
    # print(k,eigenvalues)
    file.write(str((k-nc)*np.pi/nc)+"\t"+str(eigenvalues[0])+"\t"+str(eigenvalues[1])+"\t"+str(eigenvalues[2])+"\t"+str(eigenvalues[3])+"\t"+str(eigenvalues[4])+"\t"+str(eigenvalues[5])+'\n')
    # plt.plot(k,eigenvalues[0],'o',color='red')
    # plt.plot(k,eigenvalues[1],'o',color='orange')
    # plt.plot(k,eigenvalues[2],'o',color='yellow')
    # plt.plot(k,eigenvalues[3],'o',color='green')
    # plt.plot(k,eigenvalues[4],'o',color='blue')
    # plt.plot(k,eigenvalues[5],'o',color='violet')
    # print(eigenvalues[3])
# plt.xticks([0,nc/4,nc/2,3*nc/4,nc],['0','$\pi$/4','$\pi/2$','3$\pi$/4','$\pi$'])
file.close()
# plt.show()
