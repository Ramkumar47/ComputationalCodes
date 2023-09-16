#
# Makefile for Compressible Flow solver model
#

# Program Name
PROG = CompFlow.exe

# Source Folder name # it is a Makefile variable
VPATH=src
# Object Folder
OBJDIR=objs
# Module Folder
MODDIR=mods
# Executable Folder
EXECDIR=exec

# Compiler and Flags
FC = /usr/bin/gfortran
FFLAGS = -c -O3 -g -I/usr/include/hdf5/serial/
FLINK = -O3 -mcmodel=medium -g -L /usr/lib/x86_64-linux-gnu/hdf5/serial/ -lhdf5_fortran -lhdf5
LINKER = $(FC) -o

# Object files
OBJS = bcSubroutines.o  boundaryConditions.o  differentiation.o  gridGeneration.o  initAndComp.o  Maccormack_solver.o  main.o  modelVars.o  parameters.o  writeData.o IBM.o

run: $(PROG)
	$(EXECDIR)/$(PROG)

# Creates the model
$(PROG): $(OBJS)
	@echo "--------------------------------------"
	@echo "Creating the executable for the model"
	@echo "--------------------------------------"
	mkdir -p $(OBJDIR) $(MODDIR) $(EXECDIR)
	$(LINKER) $(PROG) $(OBJS) $(FLINK)
	mv *.o $(OBJDIR)
	mv *.mod $(MODDIR)
	mv *.exe $(EXECDIR)

%.o: %.f90
	@echo "--------------------------------------"
	@echo "Compiling the file $<"
	@echo "--------------------------------------"
	$(FC) $(FFLAGS) $<

# Cleans up everything
clean:
	@echo "--------------------------------------"
	@echo "Cleaning the compilation files"
	@echo "--------------------------------------"
	rm -f *~ *.nc plot*.png *.exe *.o *.mod
	rm -rf $(OBJDIR)
	rm -rf $(MODDIR)
	rm -rf $(EXECDIR)


main.o 				:  main.f90 Maccormack_solver.o
Maccormack_solver.o :  Maccormack_solver.f90 bcSubroutines.o IBM.o
bcSubroutines.o		:  bcSubroutines.f90 boundaryConditions.o
gridGeneration.o    :  gridGeneration.f90 parameters.o modelVars.o
initAndComp.o       :  initAndComp.f90 parameters.o modelVars.o
writeData.o         :  writeData.f90 parameters.o modelVars.o
differentiation.o   :  differentiation.f90 parameters.o modelVars.o
boundaryConditions.o:  boundaryConditions.f90 parameters.o modelVars.o
modelVars.o			:  modelVars.f90 parameters.o
IBM.o	       		:  IBM.f90 modelVars.f90 parameters.o
parameters.o        :  parameters.f90
