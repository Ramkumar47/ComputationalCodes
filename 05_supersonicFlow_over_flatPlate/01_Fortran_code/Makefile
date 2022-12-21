parameters.o: parameters.f08
	gfortran -c parameters.f08

modelVars.o: modelVars.f08 parameters.o
	gfortran -c modelVars.f08

boundaryConditions.o: boundaryConditions.f08 parameters.o modelVars.o
	gfortran -c boundaryConditions.f08

differentiation.o: differentiation.f08 parameters.o modelVars.o
	gfortran -c differentiation.f08

bcSubroutines.o: bcSubroutines.f08 parameters.o modelVars.o boundaryConditions.o
	gfortran -c bcSubroutines.f08

gridGeneration.o: gridGeneration.f08 parameters.o modelVars.o
	gfortran -c gridGeneration.f08

writeData.o: writeData.f08 parameters.o modelVars.o
	gfortran -c writeData.f08

initAndComp.o: initAndComp.f08 parameters.o modelVars.o gridGeneration.o
	gfortran -c initAndComp.f08

main.o: main.f08 parameters.o modelVars.o initAndComp.o writeData.o bcSubroutines.o differentiation.o
	gfortran -c main.f08

run.exe: main.o parameters.mod
	gfortran *.o -o run.exe

run: run.exe
	./run.exe

clean:
	rm -f *.o *.mod *.exe
