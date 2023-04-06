import pandas as pd
import os,glob

fnames = sorted(glob.glob1(os.getcwd(),"*.csv"))

for name in fnames:
    fid = pd.read_csv(name)

    df = fid.round(5)

    df.to_csv(name, index = None)



