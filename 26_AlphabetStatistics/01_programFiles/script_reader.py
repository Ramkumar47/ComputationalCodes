#!/bin/python3
"""============================================================================
Alphabet statistics generator from pdf books

Ramkumar
Wed Oct 30 04:55:14 PM IST 2024
============================================================================"""

# importing needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pypdf import PdfReader
import os,glob

#==============================================================================

# specifying names of books and its contained directory
bookNames = ["For The Love of Physics.pdf",
             "Around The World In Eighty Days.pdf",
             "Flow by Philip Ball.pdf",
             "Animal Farm.pdf",
             "The Power of Positive Thinking.pdf",
             "Ikigai.pdf"]
directory = "books/"

# specifying starting and ending page numbers to exclude title, index etc...
pageStart = [10,4,12,5,5,8]
pageEnd   = [161,320,189,83,700,115]

# creating a directory to store line-wise data files
os.system("rm -rf linewise_data && mkdir linewise_data")

# looping through books
for I in range(len(bookNames)):
    # preparing book name
    bookName = directory + "/" + bookNames[I]

    print("reading book : ",bookNames[I])

    # reading book
    reader = PdfReader(bookName)

    # getting number of pages
    N_pages = len(reader.pages)

    # setting index to start page and end page numbers in python indexing
    start = pageStart[I]
    end   = pageEnd[I]

    # extracting lines
    total_lines = []
    for i in range(start,end):
        # extracting text from current page
        page = reader.pages[i]
        content = page.extract_text()

        # extracting lines from the content
        lines = content.split("\n")
        total_lines.extend(lines)

        print("reading page : ",i-start+1," of ",end-start+1)

    # counting number of characters in each line
    a_list = []; b_list = []; c_list = []; d_list = []; e_list = []; f_list = []
    g_list = []; h_list = []; i_list = []; j_list = []; k_list = []; l_list = []
    m_list = []; n_list = []; o_list = []; p_list = []; q_list = []; r_list = []
    s_list = []; t_list = []; u_list = []; v_list = []; w_list = []; x_list = []
    y_list = []; z_list = []; line_length = [];

    idx = 1
    for line in total_lines:
        # extracting total length of alpha characters
        length = len([char for char in line if char.isalpha()])

        # extracting total number of each alphabets
        a_len = len([char for char in line if char == 'a' or char == 'A'])
        b_len = len([char for char in line if char == 'b' or char == 'B'])
        c_len = len([char for char in line if char == 'c' or char == 'C'])
        d_len = len([char for char in line if char == 'd' or char == 'D'])
        e_len = len([char for char in line if char == 'e' or char == 'E'])
        f_len = len([char for char in line if char == 'f' or char == 'F'])
        g_len = len([char for char in line if char == 'g' or char == 'G'])
        h_len = len([char for char in line if char == 'h' or char == 'H'])
        i_len = len([char for char in line if char == 'i' or char == 'I'])
        j_len = len([char for char in line if char == 'j' or char == 'J'])
        k_len = len([char for char in line if char == 'k' or char == 'K'])
        l_len = len([char for char in line if char == 'l' or char == 'L'])
        m_len = len([char for char in line if char == 'm' or char == 'M'])
        n_len = len([char for char in line if char == 'n' or char == 'N'])
        o_len = len([char for char in line if char == 'o' or char == 'O'])
        p_len = len([char for char in line if char == 'p' or char == 'P'])
        q_len = len([char for char in line if char == 'q' or char == 'Q'])
        r_len = len([char for char in line if char == 'r' or char == 'R'])
        s_len = len([char for char in line if char == 's' or char == 'S'])
        t_len = len([char for char in line if char == 't' or char == 'T'])
        u_len = len([char for char in line if char == 'u' or char == 'U'])
        v_len = len([char for char in line if char == 'v' or char == 'V'])
        w_len = len([char for char in line if char == 'w' or char == 'W'])
        x_len = len([char for char in line if char == 'x' or char == 'X'])
        y_len = len([char for char in line if char == 'y' or char == 'Y'])
        z_len = len([char for char in line if char == 'z' or char == 'Z'])

        # appending to the lists
        a_list.append(a_len); b_list.append(b_len); c_list.append(c_len)
        d_list.append(d_len); e_list.append(e_len); f_list.append(f_len)
        g_list.append(g_len); h_list.append(h_len); i_list.append(i_len)
        j_list.append(j_len); k_list.append(k_len); l_list.append(l_len)
        m_list.append(m_len); n_list.append(n_len); o_list.append(o_len)
        p_list.append(p_len); q_list.append(q_len); r_list.append(r_len)
        s_list.append(s_len); t_list.append(t_len); u_list.append(u_len)
        v_list.append(v_len); w_list.append(w_len); x_list.append(x_len)
        y_list.append(y_len); z_list.append(z_len); line_length.append(length)

        print("processing line = ",idx," of ",len(total_lines))
        idx += 1

    # preparing pandas dataframe to store the results
    filename = "alphabetCount_"+bookNames[I].split(".pdf")[0]+".csv"
    fid = pd.DataFrame(np.transpose([
                    a_list,b_list,c_list,d_list,e_list,f_list,g_list,
                    h_list,i_list,j_list,k_list,l_list,m_list,n_list,
                    o_list,p_list,q_list,r_list,s_list,t_list,u_list,
                    v_list,w_list,x_list,y_list,z_list,line_length]),
                       columns = ["a","b","c","d","e","f","g",
                                  "h","i","j","k","l","m","n",
                                  "o","p","q","r","s","t","u",
                                  "v","w","x","y","z","line_length"])
    fid.to_csv("linewise_data/"+filename,index = None)

print("done")

#==============================================================================
