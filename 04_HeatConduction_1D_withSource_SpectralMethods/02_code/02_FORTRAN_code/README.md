# Instruction for code execution
This code is developed with Modern FORTRAN for main computation
and Python-3 for post-processing. A Makefile is made to make the execution
easier. The steps below can be followed for code execution

- First, make a working directory and copy all files from this directory to there
- clean the directory by using the command *make clean*
- compile the code using the command *make*
- execute the code using the command *make run*

## software requirements
The following tools were required and the code is developed and run on a linux
machine.
- gfortran
- python3 with numpy, pandas and matplotlib modules
- make

## files description
- *Makefile* 		:  	the file needed by *make* command for compilation and execution
- *main.f90*		:	FORTRAN main program file
- *parameters.f90*	: 	FORTRAN file containing parameter definitions and other variables as modules
- *subroutines1.f90*:	FORTRAN file containing needed subroutines for the program execution
- *script.py*		:	python3 file used for error computation and plotting of results
