parameters.o: parameters.f08
	gfortran -c parameters.f08

subroutines.o: parameters.o subroutines.f08
	gfortran -c subroutines.f08

main.o: subroutines.o main.f08
	gfortran -c main.f08

run.exe: main.o
	gfortran *.o -o run.exe

run: run.exe
	./run.exe && python script_prep.py

clean:
	rm -f *.o *.mod *.exe

dir:
	rm -rf solution_data && mkdir solution_data
