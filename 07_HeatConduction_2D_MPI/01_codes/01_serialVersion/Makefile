parameters.o: parameters.f08
	mpifort -c parameters.f08

writeData.o: writeData.f90 parameters.o
	mpifort -c writeData.f90

main.o: main.f08 writeData.o
	mpifort -c main.f08

solver.exe: main.o
	mpifort *.o -o solver.exe

run: solver.exe
	./solver.exe

clean:
	rm -rf *.exe *.o *.mod
