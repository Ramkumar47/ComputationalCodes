parameters.o: parameters.f90
	ifort -c parameters.f90

modelVars.o: modelVars.f90 parameters.o
	ifort -c modelVars.f90

boundaryConditions.o: boundaryConditions.f90 parameters.o modelVars.o
	ifort -c boundaryConditions.f90

differentiation.o: differentiation.f90 parameters.o modelVars.o
	ifort -c differentiation.f90

bcSubroutines.o: bcSubroutines.f90 parameters.o modelVars.o boundaryConditions.o
	ifort -c bcSubroutines.f90

gridGeneration.o: gridGeneration.f90 parameters.o modelVars.o
	ifort -c gridGeneration.f90

writeData.o: writeData.f90 parameters.o modelVars.o
	ifort -c writeData.f90

initAndComp.o: initAndComp.f90 parameters.o modelVars.o gridGeneration.o
	ifort -c initAndComp.f90

Maccormack_solver.o: Maccormack_solver.f90 parameters.o modelVars.o differentiation.o bcSubroutines.o
	ifort -c Maccormack_solver.f90

main.o: main.f90 parameters.o modelVars.o initAndComp.o writeData.o bcSubroutines.o differentiation.o Maccormack_solver.o
	ifort -c main.f90

run.exe: main.o parameters.mod
	ifort *.o -o run.exe

run: run.exe
	./run.exe

clean:
	rm -f *.o *.mod *.exe
