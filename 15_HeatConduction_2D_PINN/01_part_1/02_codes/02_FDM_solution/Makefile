parameters.o: parameters.f08
	gfortran -c parameters.f08
subroutines.o: subroutines.f08 parameters.o
	gfortran -c subroutines.f08
main.o: main.f08 subroutines.o params.mod modelvars.mod
	gfortran -c main.f08
run.exe: main.o parameters.o params.mod modelvars.mod subroutines.o
	gfortran *.o -o run.exe
run: run.exe
	./run.exe
clean:
	rm -rf *.o *.mod *.exe
plot:
	python plotter.py
