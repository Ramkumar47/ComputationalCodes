parameters.o: parameters.f90
	gfortran -c parameters.f90

modelVars.o: modelVars.f90 parameters.o
	gfortran -c modelVars.f90

boundaryConditions.o: boundaryConditions.f90 parameters.o modelVars.o
	gfortran -c boundaryConditions.f90

differentiation.o: differentiation.f90 parameters.o modelVars.o
	gfortran -c differentiation.f90

bcSubroutines.o: bcSubroutines.f90 parameters.o modelVars.o boundaryConditions.o
	gfortran -c bcSubroutines.f90

gridGeneration.o: gridGeneration.f90 parameters.o modelVars.o
	gfortran -c gridGeneration.f90

writeData.o: writeData.f90 parameters.o modelVars.o
	gfortran -c writeData.f90

initAndComp.o: initAndComp.f90 parameters.o modelVars.o gridGeneration.o
	gfortran -c initAndComp.f90

Maccormack_solver.o: Maccormack_solver.f90 parameters.o modelVars.o differentiation.o bcSubroutines.o
	gfortran -c Maccormack_solver.f90

main.o: main.f90 parameters.o modelVars.o initAndComp.o writeData.o bcSubroutines.o differentiation.o Maccormack_solver.o
	gfortran -c main.f90

run.exe: main.o parameters.mod
	gfortran *.o -o run.exe

run: run.exe
	./run.exe

clean:
	rm -f *.o *.mod *.exe
