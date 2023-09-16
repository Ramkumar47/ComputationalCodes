# modules.o: modules.f08
#     gfortran -c modules.f08
# subroutines.o: subroutines.f08 modules.o
#     gfortran -c subroutines.f08
# main.o: main.f08 subroutines.o
#     gfortran -c main.f08
# run.exe: main.o
#     gfortran *.o -o run.exe

# Program Name
PROG = HC2D.exe

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
# FFLAGS = -c -mcmodel=large -fopenmp -O3 -g -I/usr/include/hdf5/serial/
# FLINK = -O3 -mcmodel=large -g -L /usr/lib/x86_64-linux-gnu/hdf5/serial/ -lhdf5_fortran -lhdf5 -fopenmp
FFLAGS = -c -mcmodel=large
FLINK = -O3 -mcmodel=large
# FFLAGS = -c -mcmodel=large -fopenmp -O3 -g -I/usr/include/hdf5/serial/
# FLINK = -O3 -mcmodel=large -g -L /usr/lib/x86_64-linux-gnu/hdf5/serial/ -lhdf5_fortran -lhdf5 -fopenmp
LINKER = $(FC) -o

# Object files
OBJS = subroutines.o main.o modules.o

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

%.o: %.f08
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


main.o 				:  main.f08 subroutines.o modules.o
subroutines.o		:  subroutines.f08 modules.o
modules.o			:  modules.f08
