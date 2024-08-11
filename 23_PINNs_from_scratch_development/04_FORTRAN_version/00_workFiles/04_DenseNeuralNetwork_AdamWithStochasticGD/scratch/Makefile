main.o: main.f95
	gfortran -c main.f95
run.exe: main.o
	gfortran *.o -o run.exe
run: run.exe
	./run.exe
clean:
	rm -f *.o *.exe *.mod && clear
all: clean run
