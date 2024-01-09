"""----------------------------------------------------------------------------
Finite Element solution of 1D HC with source

with
 - linear shape function
 - constant source

 Input file
----------------------------------------------------------------------------"""

# themal conductivity
K              = 1.0

#  # constant heat source
#  Q              = 2.0

# rod length
L              = 1.0

# number of elements
N_ele          = 20

# output file names
out_fileName   = "computed_output_10.csv"
out_figName    = "output_10.png"
out_errFigName = "error_10.png"

# analytical function definition
def AnalyticalFunction(x):
    return x**2 - x**3
