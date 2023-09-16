import numpy as np
import matplotlib.pyplot as plt

L = 1.0

Nx = 101
X = np.linspace(0,L,Nx)

N = 40

Tw = 300
Te = 500
q = 1000
k = 1.0

T = np.zeros(Nx)

for i in range(Nx):
    sumVal = 0
    x = X[i]
    for n in range(1,N+1):

        an = 2*q/k*L**2/(n*np.pi)**3*(1-(-1)**n)

        sumVal += an*np.sin(n*np.pi/L*x)

    T[i] = Tw + x/L*(Te-Tw) + sumVal

# analytical solution
A = 1/L*(Te-Tw + q*L**2/2/k)
T_act = -q*X**2/2/k + A*X + Tw

# computing error percentage
error = np.max(np.abs(T_act-T)/T_act)*100.0

Nval = np.linspace(0,Nx-1,15, dtype=int)

plt.figure()
plt.plot(X,T,'-b')
plt.plot(X[Nval],T_act[Nval],'*r')
plt.title("Error percentage = "+str(np.round(error,2))+" %")
plt.grid()
plt.xlabel("X")
plt.ylabel("T")
plt.show()


