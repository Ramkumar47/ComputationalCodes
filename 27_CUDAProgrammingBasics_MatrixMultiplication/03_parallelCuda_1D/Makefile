main.o: main.cu
	nvcc -c main.cu -Wno-deprecated-gpu-targets
run.exe: main.o
	nvcc *.o -o run.exe -Wno-deprecated-gpu-targets

run: run.exe
	./run.exe

clean:
	rm -f *.o *.exe
