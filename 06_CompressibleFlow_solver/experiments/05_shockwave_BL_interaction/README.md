# laminar shockwave-boundary layer interaction
This is version -03 of the code that is solved on a rectangular
grid of size 1e-4X1e-5 to see the reflected shockwave interacting with the
boundary layer

and following upgrades were made in this version of the code
- loops instead of matrix multiplications for enhanced speed
- resume simulation from previously computed solution fields
- new Makefile for organized compilation
- HDF5 data writer
- inverse grid transformation

## instruction for code execution
- on a linux terminal, cd to the current directory
- `make` and `gfortran` need to be installed in the machine for compiling/executing the code
- type `make clean` to clean any previous compilations and `make` for compiling and executing the code
- csv file will be written in solution_files_csv/ folder and it can be used for further post-processing

script_gridGen.py is the python script used to create the grid (a trial script)
pvscript.py is a paraview python script, for loading csv file
input_grid.dat is the grid file generated by the python script
src/ is the folder containing source code