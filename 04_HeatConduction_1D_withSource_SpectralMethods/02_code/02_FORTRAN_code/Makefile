parameters.o: parameters.f90
	gfortran -c parameters.f90
subroutines1.o: subroutines1.f90
	gfortran -c subroutines1.f90
main.o: main.f90 parameters.mod
	gfortran -c main.f90
run.exe: main.o subroutines1.o
	gfortran *.o -o run.exe
run: run.exe
	./run.exe
	python script.py
clean:
	rm -f *.o *.mod *.exe
