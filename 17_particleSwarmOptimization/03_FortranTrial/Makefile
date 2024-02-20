parameters.o: parameters.f95
	gfortran -c parameters.f95
modelVariables.o: modelVariables.f95 parameters.o
	gfortran -c modelVariables.f95
subroutines.o: subroutines.f95 modelVariables.o
	gfortran -c subroutines.f95
main.o: main.f95 subroutines.o
	gfortran -c main.f95
run.exe: main.o
	gfortran *.o -o run.exe
run: run.exe
	./run.exe
clean:
	rm -f *.o run.exe *.mod
plot:
	python plotter.py

all: clean parameters.o modelVariables.o subroutines.o main.o run.exe run plot
