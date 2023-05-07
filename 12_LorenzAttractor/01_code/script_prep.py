"""----------------------------------------------------------------------------
python script to convert data to proper csv file
----------------------------------------------------------------------------"""

# imporing needed modules
import pandas as pd

# reading the file with proper arguments
fid = pd.read_csv("solution_data/data.csv", delim_whitespace = True)

# overwriting the data back to file
fid.to_csv("solution_data/data.csv", index = None)

print("file prep done")
