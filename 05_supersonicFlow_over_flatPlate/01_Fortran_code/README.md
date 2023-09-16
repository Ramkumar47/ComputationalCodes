# laminar viscous supersonic flow over a flat plate
This Fortran code solves the laminar viscous supersonic flow over a flat plate for a case with Re = 1000. freestream Mach number is 4.0 and the
freestream pressure, density, temperature were taken to be at standard sealevel. The length of plate is taken to be 1e-5 m and the height
of domain is taken to be 5 times the boundary layer height at the end of the plate. The Maccormack predictor-corrector method is implemented
for computation.

The code is made as modular as possible, hence any new additions to the code can be made with ease. The post-processing is done using
ParaView with csv file written by Fortran code. Intel compiler "ifort" is used for compilation and execution, and checked to work with gfortran as well

A documentation of results were made and placed along with this code in the repository.

## Method to execute the code
A Makefile is included in the code direcory which can be used for compilation
- Open linux terminal and navigate to the code directory.
- Make sure that the _make_ is installed in the linux machine.
- Modify the boundaryConditions.f90 fortran file to implement the needed boundary conditions
- give the command `make clean` to clean any previous compilations.
- then the command `make` to compile the code with actual procedure i.e. to compile modules first etc...
- and then the command `make run` to run the executable generated during compilation.
- a directory with name _solution_files_  will be created and a csv file containing solution data will be placed inside it at the end of computation.
- the csv file can be used for post-processing like loading it in ParaView or using Python.
