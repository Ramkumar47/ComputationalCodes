#!/bin/python3
"""----------------------------------------------------------------------------
AE721 - Boundary Layer Theory
Assignment - 04:  Numerical simulation of Compressible Couette Flow
case 2 : adiabatic top wall and constant tempeature bottom wall

Name : Ramkumar S
SCNO : SC22M007
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
from copy import copy as cp
import matplotlib.pyplot as plt

# computation parameters definition--------------------------------------------
Pr = 0.72   # prandtl number
mu0 = 1.789e-5 #  dynamic viscosity reference
T0 = 288.16 #  reference temperature
Cp = 1005.0 #  specific heats at constant pressure
k0 = mu0*Cp/Pr # reference thermal conductivity value for air
N = 201 #  number of steps in y direction

A = [0,5,10,20] #  A = Pr*Ec
T_bot = 288.16/T0 #  top and bottom wall temperatures
T_top = 288.16/T0
U_bot = 1.0 #  top and bottom wall velocities
U_top = 0.0

# function definitions---------------------------------------------------------
# variables definition
T = np.linspace(T_bot, T_top*0.9, N)
U = np.linspace(U_bot,U_top,N)
S = np.ones(N)*(T_top-T_bot)/1.0
y = np.linspace(0,1,N)
mu = np.ones(N)
dy = 1/(N-1)

# test function for T variable
def T_testfunc(tau,PrEc,Sw):
    global mu,S,U,T
    S[0] = Sw
    # begining loop
    for i in range(N-1):
        # computing K, T and mu
        K = mu[i]

        # solving equations
        T[i+1] = T[i] + S[i]/K*dy
        S[i+1] = S[i] - PrEc*tau*(U[i+1]-U[i])/dy*dy

    return S[-1]

# test function for U variable
def U_testfunc(tau):
    global mu,S,U,T
    # integrating
    for i in range(N-1):
        U[i+1] = U[i] + tau/mu[i]*dy

    return U[-1]

# solution computation---------------------------------------------------------

# creating lists to store values
T_list = []
U_list = []

# looping through A values
for A_index in range(len(A)):

    print("Solving for A = ",A[A_index])

    tau = 1.0 #  initial guess for nondim shearstress

    for itr in range(100):
        print("iteration : ",itr+1)
        # solving for T
        S_a = 0
        S_b = 1.0
        S_c = (S_a+S_b)/2

        while abs(T_testfunc(tau,A[A_index],S_b)-0) > 1e-7:
            # solving for T
            S_c = S_b - ((T_testfunc(tau,A[A_index],S_b)-0)/
                    ((T_testfunc(tau,A[A_index],S_b)-
                        T_testfunc(tau,A[A_index],S_a))/(S_b-S_a)))
            S_a = S_b*1.0
            S_b = S_c*1.0

        S[0] = S_c*1.0
        print("\tsolved for T")

        mu = T*1.0

        # solving for U
        tau_a = 0
        tau_b = 1.0
        tau_c = (tau_a + tau_b)/2.0

        while abs(U_testfunc(tau_c) - U_top) > 1e-7:
            # solving for U
            tau_c = tau_b - ((U_testfunc(tau_b)-U_top)/
                    ((U_testfunc(tau_b)-U_testfunc(tau_a))/(tau_b-tau_a)))
            tau_a = tau_b*1.0
            tau_b = tau_c*1.0


        tau = tau_c*1.0
        print("\tsolved for U")

    T_list.append(list(T))
    U_list.append(list(U))

# analytical solution computation----------------------------------------------
# preparing lists to store computed values
T_A_list = []; U_A_list = []

# defining lambda functions for U and T
res_U = lambda y,u,Aval: 1-u*(1+0.5*Aval*(1-u/2))/(1+0.25*Aval) - y
Tval = lambda u,Aval: 1 + 0.5*Aval*(1-u**2)

N_vals = np.linspace(0,N-1,10,dtype=int)
Y_A = np.linspace(0,1,10)

# looping through A values
for A_index in range(len(A)):
    # initializing empty list to store T and U values
    T_A = []; U_A = []

    print("computing analytical solution for A = ", A[A_index])

    # looping through N values
    for i in N_vals:
        # solving for U_A with bisection method
        U_a = -0.1
        U_b = 1.1
        U_c = (U_a+U_b)/2
        while abs(res_U(y[i],U_c,A[A_index])) > 1e-6:
            resVal = res_U(y[i],U_c,A[A_index])
            if resVal > 0:
                U_a = U_c*1.0
            else:
                U_b = U_c*1.0

            U_c = (U_a+U_b)/2.0
        U_A.append(U_c)
    U_A_list.append(U_A)

    # computing temperature
    for i in range(10):
        T_A.append(Tval(U_A[i],A[A_index]))
    T_A_list.append(T_A)

# post-processing--------------------------------------------------------------
# writing data to file

# creating dataframe for T
fid = pd.DataFrame(np.transpose(T_list), columns = ["A="+str(val) for val in A])
fid['Y'] = y
fid.to_csv("T_values.csv", index = None)

# creating dataframe for T_analytical
fid = pd.DataFrame(np.transpose(T_A_list), columns = ["A="+str(val) for val in A])
fid['Y'] = Y_A
fid.to_csv("T_Analytical_values.csv", index = None)

# creating dataframe for U
fid = pd.DataFrame(np.transpose(U_list), columns = ["A="+str(val) for val in A])
fid['Y'] = y
fid.to_csv("U_values.csv", index = None)

# creating dataframe for U_analytical
fid = pd.DataFrame(np.transpose(U_A_list), columns = ["A="+str(val) for val in A])
fid['Y'] = Y_A
fid.to_csv("U_Analytical_values.csv", index = None)


# plotting velocity graph
plt.figure()
#  for i in range(len(A)):
#      plt.plot(U_list[i],y,label='A = '+str(A[i]))
#      plt.plot(U_A_list[i],Y_A,'*',label='analytical A = '+str(A[i]))
plt.plot(U_list[0],y,'-b',label='A = '+str(A[0]))
plt.plot(U_A_list[0],Y_A,'*b',label='analytical A = '+str(A[0]))
plt.plot(U_list[1],y,'-r',label='A = '+str(A[1]))
plt.plot(U_A_list[1],Y_A,'*r',label='analytical A = '+str(A[1]))
plt.plot(U_list[2],y,'-g',label='A = '+str(A[2]))
plt.plot(U_A_list[2],Y_A,'*g',label='analytical A = '+str(A[2]))
plt.plot(U_list[3],y,'-k',label='A = '+str(A[3]))
plt.plot(U_A_list[3],Y_A,'*k',label='analytical A = '+str(A[3]))

plt.grid()
plt.xlabel('U')
plt.ylabel('y')
plt.legend(loc='upper left',bbox_to_anchor=[1.05,1])
plt.title("nondimensinal velocity variation with A")
plt.tight_layout()
plt.savefig("U_profiles.png", dpi = 150)

# plotting temperature graph
plt.figure()
#  for i in range(len(A)):
#      plt.plot(T_list[i],y,label='A = '+str(A[i]))
#      plt.plot(T_A_list[i],Y_A,'o',label='analytical A = '+str(A[i]))
plt.plot(T_list[0],y,'-b',label='A = '+str(A[0]))
plt.plot(T_A_list[0],Y_A,'ob',label='analytical A = '+str(A[0]))
plt.plot(T_list[1],y,'-r',label='A = '+str(A[1]))
plt.plot(T_A_list[1],Y_A,'or',label='analytical A = '+str(A[1]))
plt.plot(T_list[2],y,'-g',label='A = '+str(A[2]))
plt.plot(T_A_list[2],Y_A,'og',label='analytical A = '+str(A[2]))
plt.plot(T_list[3],y,'-k',label='A = '+str(A[3]))
plt.plot(T_A_list[3],Y_A,'ok',label='analytical A = '+str(A[3]))
plt.grid()
plt.xlabel('T')
plt.ylabel('y')
plt.legend(loc='best',bbox_to_anchor=[1.05,1])
plt.title("nondimensinal temperature variation with A")
plt.tight_layout()
plt.savefig("T_profiles.png", dpi = 150)
plt.show()
