/*===========================================================================*\
  * matrix multiplication code on cpu with 1D array

  * Ramkumar
  * Thu Feb  6 14:39:46 IST 2025
\*===========================================================================*/

// preprocessor directives
#include<iostream>
#include<chrono>
#include<random>
#include<fstream>

// defining size of square matrix
const int N = 4001;

// function declarations
void printMatrix(int *A);
void matMul(int *A, int *B, int *C);
void initMat(int *A);
void writeMatrix(int *A, std::string name);

/*---------------------------------------------------------------------------*/

int main(int argc, char* argv[]){

	// defining 1D pointer
	int matSize = N*N;
	int *A,*B,*C;
	A = new int[matSize];
	B = new int[matSize];
	C = new int[matSize];

	initMat(A);
	initMat(B);

	// setting timer
	auto timerStart = std::chrono::high_resolution_clock::now();
	matMul(A,B,C);
	auto timerStop = std::chrono::high_resolution_clock::now();

	auto duration = std::chrono::duration_cast<std::chrono::seconds>(timerStop-timerStart);

	writeMatrix(A,"A.mat");
	writeMatrix(B,"B.mat");
	writeMatrix(C,"C.mat");

	std::cout << "Time elapsed : " << duration.count() << std::endl;

	return 0;
}

// function definitions

void printMatrix(int *A){
	for(int i=0; i<N; i++){ // rows
		for(int j=0; j<N; j++){ // columns
			int idx = j+i*N; // c+r*N
			std::cout << " " << A[idx];
		}
		std::cout << std::endl;
	}
}

void matMul(int *A, int *B, int *C){
	for(int i=0; i<N; i++){ // rows
		for(int j=0; j<N; j++){ // columns
			int idx = j+i*N;
			C[idx] = 0;
			for(int k=0; k<N; k++){
				C[idx] += A[k+i*N]*B[j+k*N];
			}
		}
	}
}

void initMat(int *A){
	for(int i=0; i<N; i++){ // rows
		for(int j=0; j<N; j++){ // columns
			int idx = j+i*N;
			A[idx] = random()%9+1;
		}
	}
}

void writeMatrix(int *A, std::string name){
    std::ofstream fid(name);
    for(int i=0; i<N; i++){ // rows
        for(int j=0; j<N; j++){ // columns
            int idx = j+i*N;
            fid << A[idx] << ",";
        }
        fid << std::endl;
    }
    fid.close();
}


/*---------------------------------------------------------------------------*/
