parameters.o: parameters.f95
	gfortran -c parameters.f95
modules.o: parameters.o
	gfortran -c modules.f95
variables.o: modules.o
	gfortran -c variables.f95
subroutines.o: variables.o
	gfortran -c subroutines.f95
main.o: subroutines.o
	gfortran -c main.f95
run.exe: main.o
	gfortran *.o -o run.exe
run: run.exe
	./run.exe
clean:
	rm -f *.o *.exe *.mod && clear
all: clean run

postprocess:
	python script_postprocess.py
