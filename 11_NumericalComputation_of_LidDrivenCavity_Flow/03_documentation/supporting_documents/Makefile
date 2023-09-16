parameters.o: parameters.f08
	gfortran -c parameters.f08

subroutines.o: subroutines.f08 parameters.o
	gfortran -c subroutines.f08

main.o: main.f08 subroutines.o
	gfortran -c main.f08

run.exe: main.o
	gfortran *.o -o run.exe

run: run.exe
	./run.exe

clean:
	rm -f *.o *.mod *.exe

dir:
	rm -rf solution_data && mkdir solution_data

plot:
	python script_plotter.py
