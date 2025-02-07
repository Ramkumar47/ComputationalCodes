/*===========================================================================*\
  * matrix multiplication code on cpu

  * Ramkumar
  * Thu Feb  6 14:39:46 IST 2025
\*===========================================================================*/

// preprocessor directives
#include<iostream>
#include<chrono>
#include<random>

// defining size of square matrix
const int N = 2001;

// function declarations
void printMatrix(int **A);
void matMul(int **A, int **B, int **C);
void initMat(int **A);

/*---------------------------------------------------------------------------*/

int main(int argc, char* argv[]){

	// defining 2D pointer (double pointers)
	int **A,**B,**C;
	A = new int *[N];
	B = new int *[N];
	C = new int *[N];
	for(int i=0; i<N; i++){
		A[i] = new int[N];
		B[i] = new int[N];
		C[i] = new int[N];
	}

	initMat(A);
	// printMatrix(A);
	std::cout << std::endl;
	initMat(B);
	// printMatrix(B);

	// setting timer
	auto timerStart = std::chrono::high_resolution_clock::now();
	matMul(A,B,C);
	auto timerStop = std::chrono::high_resolution_clock::now();

	auto duration = std::chrono::duration_cast<std::chrono::seconds>(timerStop-timerStart);

	std::cout << "Time elapsed : " << duration.count() << std::endl;

	return 0;
}

// function definitions

void printMatrix(int **A){
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			std::cout << " " << A[i][j];
		}
		std::cout << std::endl;
	}
}

void matMul(int **A, int **B, int **C){
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			C[i][j] = 0;
			for(int k=0; k<N; k++){
				C[i][j] += A[i][k]*B[k][j];
			}
		}
	}
}

void initMat(int **A){
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			A[i][j] = random()%9+1;
		}
	}
}

/*---------------------------------------------------------------------------*/
