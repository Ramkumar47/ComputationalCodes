main.o: main.C
	g++ -c main.C
run.exe: main.o
	g++ *.o -o run.exe

run: run.exe
	./run.exe

clean:
	rm -f *.o *.exe
