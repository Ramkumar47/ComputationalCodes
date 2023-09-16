#!/bin/python3
"""----------------------------------------------------------------------------
postprocessing the computed data
----------------------------------------------------------------------------"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os,glob

# reading files----------------------------------------------------------------
fnames = sorted(glob.glob1(os.getcwd()+"/../01_FDM/tables_csv/","*.csv"))
# adding path to all the fnames
for i in range(len(fnames)):
    fnames[i] = "../01_FDM/tables_csv/"+fnames[i]
fnames.append("../02_shootingMethod/table_data_m=-0.0904.csv")

fid = []
for name in fnames:
    fid.append(pd.read_csv(name))

# obtaining m values from the filenames
m = []
for name in fnames:
    m.append( float(name.split("=")[1].split("c")[0][:-1]))

# preparing table data---------------------------------------------------------
d_star_dFS_list = [] #  delta*/delta_FS
theta_dFS_list = [] #  theta/delta_FS
H_list = [] #  H
Rex_Cf_list = [] #  sqrt{Re_x} Cf/2
lambda_list = [] #  lambda
Tau_list = [] #  captial Tau
F_theta_list = [] #  F_theta

# looping through m values
for i in range(len(m)):
    # computing d_star_dFS
    d_star_dFS = ((fid[i]['eta'].iloc[-1] - fid[i]['f'].iloc[-1]) -
            (fid[i]['eta'].iloc[0] - fid[i]['f'].iloc[0]))

    # computing theta_dFS numerically
    sum = 0
    func = lambda j: fid[i]['g'].iloc[j] - fid[i]['g'].iloc[j]**2
    for j in range(1,fid[i].shape[0]-1):
        sum += func(j)
    dn = fid[i]['eta'].iloc[1] - fid[i]['eta'].iloc[0]
    theta_dFS = dn/2.0*(func(0) + func(fid[i].shape[0]-1) + 2*sum)

    # compute H
    H = d_star_dFS/theta_dFS

    # computing Rex_Cf
    Rex_Cf = fid[i]['h'].iloc[0] #  @ wall

    # computing lamda
    lamda = m[i]*theta_dFS**2

    # computing Tau
    Tau = theta_dFS*fid[i]['h'].iloc[0] #  @ wall

    # computing F_theta
    F_theta = 2*(Tau - (H + 2)*lamda)

    # appending them to the list
    d_star_dFS_list.append(d_star_dFS)
    theta_dFS_list.append(theta_dFS)
    H_list.append(H)
    Rex_Cf_list.append(Rex_Cf)
    lambda_list.append(lamda)
    Tau_list.append(Tau)
    F_theta_list.append(F_theta)

# preparing dataframe to save it
df = pd.DataFrame(np.transpose([m,d_star_dFS_list, theta_dFS_list, H_list,
    Rex_Cf_list, lambda_list, Tau_list, F_theta_list]),
    columns = ["m","d_star_dFS","theta_dFS","H","Rex_Cf",
                 "lambda","Tau","F_theta"])
df = df.sort_values("m").reset_index(drop=True)
df.to_csv("table_1_FS.csv", index = None)

# plotting graphs--------------------------------------------------------------

# plot 1 : u/ue vs eta
plt.figure()
for i in range(len(fnames)):
    plt.plot(fid[i]["g"],fid[i]["eta"],label="m = "+str(m[i]))
plt.legend()
plt.grid()
plt.xlabel(r"$u/u_e$")
plt.ylabel(r"$\eta$")
plt.title(r"$u/u_e$ vs $\eta$")
plt.savefig("plot_1.png", dpi = 150)

# plot 2 : v sqrt{Rex}/ue vs eta
plt.figure()
for i in range(len(fnames)):
    plt.plot((fid[i]["g"]*fid[i]["eta"] - fid[i]["f"])/2.0,fid[i]["eta"],label="m = "+str(m[i]))
plt.legend()
plt.grid()
plt.xlabel(r"$v/u_e \sqrt{Re_x}$")
plt.ylabel(r"$\eta$")
plt.title(r"$v/u_e \sqrt{Re_x}$ vs $\eta$")
plt.savefig("plot_2.png", dpi = 150)

# plot 3 : tau sqrt{Rex}/(rhoe Ue^2) vs eta
plt.figure()
for i in range(len(fnames)):
    plt.plot(fid[i]["h"],fid[i]["eta"],label="m = "+str(m[i]))
plt.legend()
plt.grid()
plt.xlabel(r"$\tau \sqrt{Re_x}/\rho_e u_e^2$")
plt.ylabel(r"$\eta$")
plt.title(r"$\tau \sqrt{Re_x}/\rho_e u_e^2$ vs $\eta$")
plt.savefig("plot_3.png", dpi = 150)

# reading book data
df_book = pd.read_csv("book_data.csv")

# plot 4 : lambda vs H
plt.figure()
plt.plot(df['lambda'], df['H'], '-b', label = "computed")
plt.plot(df_book['lambda'], df_book['H'], 'or', label = "book data")
plt.grid()
plt.legend()
plt.xlabel(r"$\lambda$")
plt.ylabel("H")
plt.title(r"$\lambda$ vs H")
plt.savefig("lambda_vs_H.png", dpi = 150)

# plot 5 : lambda vs tau
plt.figure()
plt.plot(df['lambda'], df['Tau'], '-b', label = "computed")
plt.plot(df_book['lambda'], df_book['Tau'], 'or', label = "book data")
plt.grid()
plt.legend()
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$\tau$")
plt.title(r"$\lambda$ vs $\tau$")
plt.savefig("lambda_vs_Tau.png", dpi = 150)

# plot 6 : lambda vs F_theta
plt.figure()
plt.plot(df['lambda'], df['F_theta'], '-b', label = "computed")
plt.plot(df_book['lambda'], df_book['F_theta'], 'or', label = "book data")
plt.grid()
plt.legend()
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$F_\theta$")
plt.title(r"$\lambda$ vs $F_\theta$")
plt.savefig("lambda_vs_F_theta.png", dpi = 150)

# computing analytical solution using thwait's method
lambda_T_list = []
d_star_dFS_T_list = []
H_T_list = []
Tau_T_list = []
theta_dFS_T_list = []
Rex_Cf_T_list = []

for i in range(len(m)):
    # computing lambda
    lamda = 0.45*m[i]/(5*m[i]+1)

    # computing H and Tau
    H = 2.61 - 4.1*lamda + 14*lamda**3 + 0.56*lamda**2/(lamda + 0.18)**2
    Tau = 0.220 + 1.52*lamda - 5.0*lamda**3 - 0.072*lamda**2/(lamda + 0.18)**2

    # computing d_star_dFS
    d_star_dFS = H*np.sqrt(0.45/(5*m[i]+1))

    # computing theta_dFS
    theta_dFS = np.sqrt(0.45/(5*m[i]+1))

    # computing Rex_Cf
    Rex_Cf = Tau/theta_dFS

    # appending them to the list
    lambda_T_list.append(lamda)
    H_T_list.append(H)
    Tau_T_list.append(Tau)
    d_star_dFS_T_list.append(d_star_dFS)
    theta_dFS_T_list.append(theta_dFS)
    Rex_Cf_T_list.append(Rex_Cf)

# preparing dataframe to store analytical data
df2 = pd.DataFrame(np.transpose([m,d_star_dFS_T_list, theta_dFS_T_list, H_T_list,
    Rex_Cf_T_list, lambda_T_list, Tau_T_list]),
    columns = ["m","d_star_dFS","theta_dFS","H","Rex_Cf",
                 "lambda","Tau"])
df2 = df2.sort_values("m").reset_index(drop=True)
df2.to_csv("table_2_thwait.csv", index = None)


# plot 7 : lambda vs d_star_dFS thwait comparison
plt.figure()
plt.plot(df2['lambda'], df2['d_star_dFS'], '-b', label = "Thwait solution")
plt.plot(df['lambda'], df['d_star_dFS'], 'or', label = "Fs solution")
plt.grid()
plt.legend()
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$\delta^*/\delta_{FS}$")
plt.title(r"$\lambda$ vs $\delta^*/\delta_{FS}$")
plt.savefig("lambda_vs_d_star_dFS_thwait.png", dpi = 150)

# plot 8 : lambda vs theta_dFS thwait comparison
plt.figure()
plt.plot(df2['lambda'], df2['theta_dFS'], '-b', label = "Thwait solution")
plt.plot(df['lambda'], df['theta_dFS'], 'or', label = "Fs solution")
plt.grid()
plt.legend()
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$\theta/\delta_{FS}$")
plt.title(r"$\lambda$ vs $\theta/\delta_{FS}$")
plt.savefig("lambda_vs_theta_dFS_thwait.png", dpi = 150)

# plot 9 : lambda vs H thwait comparison
plt.figure()
plt.plot(df2['lambda'], df2['H'], '-b', label = "Thwait solution")
plt.plot(df['lambda'], df['H'], 'or', label = "Fs solution")
plt.grid()
plt.legend()
plt.xlabel(r"$\lambda$")
plt.ylabel(r"H")
plt.title(r"$\lambda$ vs H")
plt.savefig("lambda_vs_H_thwait.png", dpi = 150)

# plot 10 : lambda vs Tau thwait comparison
plt.figure()
plt.plot(df2['lambda'], df2['Tau'], '-b', label = "Thwait solution")
plt.plot(df['lambda'], df['Tau'], 'or', label = "Fs solution")
plt.grid()
plt.legend()
plt.xlabel(r"$\lambda$")
plt.ylabel(r"Tau")
plt.title(r"$\lambda$ vs Tau")
plt.savefig("lambda_vs_Tau_thwait.png", dpi = 150)

# plot 11 : lambda vs Rex_Cf thwait comparison
plt.figure()
plt.plot(df2['lambda'], df2['Rex_Cf'], '-b', label = "Thwait solution")
plt.plot(df['lambda'], df['Rex_Cf'], 'or', label = "Fs solution")
plt.grid()
plt.legend()
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$\sqrt{Re_x}C_f/2$")
plt.title(r"$\lambda$ vs $\sqrt{Re_x}C_f/2$")
plt.savefig("lambda_vs_Rex_Cf_thwait.png", dpi = 150)



plt.show()
