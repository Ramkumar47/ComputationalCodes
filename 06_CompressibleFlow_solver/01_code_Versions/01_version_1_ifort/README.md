# laminar viscous supersonic flow over a flat plate
This Fortran code solves the laminar viscous supersonic flow over a flat plate for a case with Re = 1000. freestream Mach number is 4.0 and the
freestream pressure, density, temperature were taken to be at standard sealevel. The length of plate is taken to be 1e-5 m and the height
of domain is taken to be 5 times the boundary layer height at the end of the plate. The Maccormack predictor-corrector method is implemented
for computation.

The code is made as modular as possible, hence any new additions to the code can be made with ease. The post-processing is done using
ParaView with csv file written by Fortran code. Intel compiler "ifort" is used for compilation and execution, and checked to work with gfortran as well

A documentation of results were made and placed along with this code in the repository.
