parameters.o: parameters.f90
	gfortran -c parameters.f90

modelVars.o: modelVars.f90 parameters.o
	gfortran -c modelVars.f90

initAndComp.o: initAndComp.f90
	gfortran -c initAndComp.f90

main.o: main.f90 parameters.o modelVars.o initAndComp.o
	gfortran -c main.f90

run.exe: main.o
	gfortran *.o -o run.exe

run: run.exe
	./run.exe

clean:
	rm -f *.exe *.o *.mod
