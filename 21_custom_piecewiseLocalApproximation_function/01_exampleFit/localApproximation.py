#!/bin/python3
"""----------------------------------------------------------------------------
custom-made piecewise local approximation functions
----------------------------------------------------------------------------"""

# importing needed libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# cubic fit--------------------------------------------------------------------
def cubic_fit(x,y,knots_location):

    """
    equation form: y_hat = a (x-x_k)^3 + b (x-x_k)^2 + c (x-x_k) + d

    x_k - starting point of a knot segment in x-data
    """

    N = x.shape[0]

    N_knots = len(knots_location)
    knots = np.array([np.where(x >= knots_location[i])[0][0] for i in range(N_knots)])

    # initializing vector equation terms
    A = np.zeros([N+4*N_knots-8, 4*(N_knots-1)])
    b = np.zeros([N+4*N_knots-8])

    # filling the matrix and vector
    rindex = 0
    for k in range(1,N_knots): #  adding intermediate points and c0 continuity
        for i in range(knots[k-1],knots[k]+1):
            A[rindex,4*(k-1)]   = (x[i]-x[knots[k-1]])**3
            A[rindex,4*(k-1)+1] = (x[i]-x[knots[k-1]])**2
            A[rindex,4*(k-1)+2] = (x[i]-x[knots[k-1]])
            A[rindex,4*(k-1)+3] = 1.0
            b[rindex]           = y[i]

            rindex += 1

    for k in range(1,N_knots-1): #  adding c0 continuity
        A[rindex,4*(k-1)]   = (x[knots[k]]-x[knots[k-1]])**3
        A[rindex,4*(k-1)+1] = (x[knots[k]]-x[knots[k-1]])**2
        A[rindex,4*(k-1)+2] = (x[knots[k]]-x[knots[k-1]])
        A[rindex,4*(k-1)+3] = 1.0

        A[rindex,4*(k-1)+7] = -1.0

        b[rindex]           = 0.0

        rindex += 1

    for k in range(1,N_knots-1): #  adding c1 continuity
        A[rindex,4*(k-1)]   = 3*(x[knots[k]]-x[knots[k-1]])**2
        A[rindex,4*(k-1)+1] = 2*(x[knots[k]]-x[knots[k-1]])
        A[rindex,4*(k-1)+2] = 1.0

        A[rindex,4*(k-1)+6] = -1.0

        b[rindex]           = 0.0

        rindex += 1

    for k in range(1,N_knots-1): #  adding c2 continuity
        A[rindex,4*(k-1)]   = 6*(x[knots[k]]-x[knots[k-1]])
        A[rindex,4*(k-1)+1] = 2

        A[rindex,4*(k-1)+5] = -2.0

        b[rindex]           = 0.0

        rindex += 1

    # computing coefficients using ordinary least squares
    tmp1   = np.matmul(A.transpose(),A)
    tmp2   = np.matmul(np.linalg.inv(tmp1),A.transpose())
    coeffs = np.matmul(tmp2,b)

    # computing approximated profile
    y_approx = np.zeros_like(y)
    for k in range(N_knots-1):
        for i in range(knots[k],knots[k+1]+1):
            y_approx[i] = coeffs[4*k]*(x[i]-x[knots[k]])**3+coeffs[4*k+1]*(x[i]-x[knots[k]])**2+coeffs[4*k+2]*(x[i]-x[knots[k]])+coeffs[4*k+3]

    # computing R2
    SS_res = np.sum(np.square(y-y_approx))
    SS_tot = np.sum(np.square(y-y.mean()))
    R2 = 1 - SS_res/SS_tot

    # preparing coeffs df
    coeffs_df = pd.DataFrame(np.transpose([coeffs[0::4], coeffs[1::4], coeffs[2::4], coeffs[3::4]]),
                             columns = ["a","b","c","d"])

    return coeffs_df, y_approx, R2, knots

# quadratic fit----------------------------------------------------------------
def quadratic_fit(x,y,knots_location):

    """
    equation form: y_hat = a (x-x_k)^3 + b (x-x_k)^2 + c (x-x_k) + d

    x_k - starting point of a knot segment in x-data
    """

    N = x.shape[0]

    N_knots = len(knots_location)
    knots = np.array([np.where(x >= knots_location[i])[0][0] for i in range(N_knots)])

    # initializing vector equation terms
    A = np.zeros([N+3*N_knots-6, 3*(N_knots-1)])
    b = np.zeros([N+3*N_knots-6])

    # filling the matrix and vector
    rindex = 0
    for k in range(1,N_knots): #  adding intermediate points and c0 continuity
        #  print(x[knots[k-1]:knots[k]+1])
        for i in range(knots[k-1],knots[k]+1):
            A[rindex,3*(k-1)]   = (x[i]-x[knots[k-1]])**2
            A[rindex,3*(k-1)+1] = (x[i]-x[knots[k-1]])
            A[rindex,3*(k-1)+2] = 1.0
            b[rindex]           = y[i]

            rindex += 1
    for k in range(1,N_knots-1): #  adding c1 continuity
        A[rindex,3*(k-1)]   = 2*(x[knots[k]]-x[knots[k-1]])
        A[rindex,3*(k-1)+1] = 1.0

        A[rindex,3*(k-1)+3] = 0.0
        A[rindex,3*(k-1)+4] = -1.0

        b[rindex]           = 0.0

        rindex += 1
    for k in range(1,N_knots-1): #  adding c0 continuity
        A[rindex,3*(k-1)]   = (x[knots[k]]-x[knots[k-1]])**2
        A[rindex,3*(k-1)+1] = x[knots[k]]-x[knots[k-1]]
        A[rindex,3*(k-1)+2] = 1.0

        A[rindex,3*(k-1)+5] = -1.0

        b[rindex]           = 0.0

        rindex += 1

    # computing coefficients using ordinary least squares
    tmp1   = np.matmul(A.transpose(),A)
    tmp2   = np.matmul(np.linalg.inv(tmp1),A.transpose())
    coeffs = np.matmul(tmp2,b)

    # computing approximated profile
    y_approx = np.zeros_like(y)
    for k in range(N_knots-1):
        for i in range(knots[k],knots[k+1]+1):
            y_approx[i] = coeffs[3*k]*(x[i]-x[knots[k]])**2+coeffs[3*k+1]*(x[i]-x[knots[k]])+coeffs[3*k+2]

    # computing error percentage
    max_Ep = np.max((np.abs(y-y_approx)/y)[1:-1])*100

    # computing R2
    SS_res = np.sum(np.square(y-y_approx))
    SS_tot = np.sum(np.square(y-y.mean()))
    R2 = 1 - SS_res/SS_tot

    # preparing coeffs dataframe
    coeffs_df = pd.DataFrame(np.transpose([coeffs[0::3], coeffs[1::3], coeffs[2::3]]),
                                columns = ["a","b","c"])

    return coeffs_df, y_approx, R2, knots

