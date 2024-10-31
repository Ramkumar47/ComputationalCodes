#!/bin/python3
"""============================================================================
post processing for the script_reader.py

Ramkumar
Wed Oct 30 06:12:10 PM IST 2024
============================================================================"""

# importing needed modules
import pandas as pd
import matplotlib.pyplot as plt
import os,glob

#==============================================================================

# reading data files
fileNames = sorted(glob.glob1(os.getcwd()+"/linewise_data/","*.csv"))

# preparing booknames
bookNames = [name.split("alphabetCount_")[1].split(".csv")[0] for name in fileNames]

# preparing list to store line-normalized character values
a_list = []; b_list = []; c_list = []; d_list = []; e_list = []; f_list = []
g_list = []; h_list = []; i_list = []; j_list = []; k_list = []; l_list = []
m_list = []; n_list = []; o_list = []; p_list = []; q_list = []; r_list = []
s_list = []; t_list = []; u_list = []; v_list = []; w_list = []; x_list = []
y_list = []; z_list = []

charArray = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
                "o","p","q","r","s","t","u","v","w","x","y","z"]

# looping through the data files
for file in fileNames:
    # reading data
    fid = pd.read_csv("linewise_data/"+file)

    # looping through characters, normalizing and storing 'em in the lists
    for char in charArray:
        fid[char] = fid[char]/(fid["line_length"]+1)*100
        eval(char+"_list.append(fid[\""+char+"\"])")

# preparing directory to store graphs
os.system("rm -rf histograms && mkdir histograms")

# preparing plots and saving them
for char in charArray:

    # getting the current list
    exec("curr_list = "+char+"_list")

    # plotting histogram
    plt.rcParams.update({"font.size":15})
    plt.figure(figsize=(16,9))
    for i in range(len(bookNames)):
        plt.hist(curr_list[i],bins=30,histtype="step",label=bookNames[i],
                 density=False,linewidth=2)
    plt.grid()
    plt.xlabel("Percentage of \'"+char.upper()+"\' or "+char+" in total alphabets per line")
    plt.ylabel("Number of lines")
    #  plt.title("Alphabet : "+char.upper()+" or "+char)
    #  plt.legend(loc=(1.01,0.75))
    plt.legend(title="Books")
    plt.savefig("histograms/"+char+".png",dpi=150,bbox_inches="tight")
    plt.close()

    print("Character : ",char.upper())

print("done")

#==============================================================================
