main.o: main.C
	g++ -c main.C

run.exe: main.o
	g++ main.o -o run.exe

run: run.exe
	./run.exe

clean:
	rm -f *.o *.exe

refresh:
	rm -f *.o *.exe *.csv
