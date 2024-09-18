import numpy as np
import matplotlib.pyplot as plt

def psi(x,n,L):
    return np.sqrt(2/L)*np.sin(n*np.pi*x/L)

L = 1.0
n = 1
x = np.linspace(0,L, num=1000)
psi1_ = psi(x,n,L)
psi2_ = psi(x,n+1,L)
psi_s = 1/np.sqrt(2)*(psi1_+psi2_)

def plotpsi2(x,psi):
    
    plt.plot(x,psi**2,c='r')
    plt.fill_between(x,psi**2, color='r',alpha=0.5)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$|\psi|^2$')
    plt.show()

def plotpsi(x,psi,psi1,psi2):
    plt.plot(x,psi,c='r')
    if psi1 is not None:
        plt.plot(x,psi1,c='b')
    if psi2 is not None:
        plt.plot(x,psi2,c='k')
    plt.fill_between(x,psi, color='r',alpha=0.5)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\psi$')
    if psi1 is not None and psi2 is not None:
        plt.legend(['$1/\sqrt{2}(|0>+|1>$'])
    plt.show()

plotpsi(x,psi_s,1/np.sqrt(2)*psi1_, 1/np.sqrt(2)*psi2_)
plotpsi(x,psi2_,None, None)
