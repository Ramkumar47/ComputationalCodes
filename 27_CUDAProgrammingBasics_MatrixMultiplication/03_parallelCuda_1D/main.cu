/*===========================================================================*\
  * matrix multiplication code on cuda

  * reference for error checking code snippet
https://stackoverflow.com/questions/14038589/what-is-the-canonical-way-to-check-for-errors-using-the-cuda-runtime-api

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
__global__ void matMul(int *A, int *B, int *C);
__global__ void hadamardProduct(int *A, int *B);
void initMat(int *A);
void writeMatrix(int *A, std::string name);

#define gpuErrchk(ans) { gpuAssert((ans), __FILE__, __LINE__); }
inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true)
{
	if (code != cudaSuccess)
	{
		fprintf(stderr,"GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
		if (abort) exit(code);
	}
}

/*---------------------------------------------------------------------------*/

int main(int argc, char* argv[]){

    // defining 2D pointer (double pointers)
    int *A,*B,*C;
    A = new int [N*N];
    B = new int [N*N];
    C = new int [N*N];

    initMat(A);
    writeMatrix(A,"A.mat");
    initMat(B);
    writeMatrix(B,"B.mat");

    // allocating memory on device
    int *d_A,*d_B,*d_C;

    gpuErrchk( cudaMalloc((void**)&d_A, N*N*sizeof(int*)) );
    gpuErrchk( cudaMalloc((void**)&d_B, N*N*sizeof(int*)) );
    gpuErrchk( cudaMalloc((void**)&d_C, N*N*sizeof(int*)) );

    // copying host **array to device
    gpuErrchk( cudaMemcpy(d_A,A,N*N*sizeof(int),cudaMemcpyHostToDevice) );
    gpuErrchk( cudaMemcpy(d_B,B,N*N*sizeof(int),cudaMemcpyHostToDevice) );

    // defining number of threads
    dim3 noOfThreads(32,32);
    dim3 noOfBlocks(126,126);

    // setting timer
    auto timerStart = std::chrono::high_resolution_clock::now();
    matMul<<<noOfBlocks,noOfThreads>>>(d_A,d_B,d_C);
    gpuErrchk( cudaPeekAtLastError() );
    cudaDeviceSynchronize();
    auto timerStop = std::chrono::high_resolution_clock::now();


    // getting back the result matrix
    cudaMemcpy(C,d_C, N*N*sizeof(int), cudaMemcpyDeviceToHost);

    auto duration = std::chrono::duration_cast<std::chrono::seconds>(timerStop-timerStart);


    std::cout << std::endl;

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

__global__
void hadamardProduct(int *A, int *B){
    int i = threadIdx.x+blockDim.x*blockIdx.x;
    int j = threadIdx.y+blockDim.y*blockIdx.y;
    int idx = j+i*N;
    B[idx] = A[idx]*A[idx];
}

__global__
void matMul(int *A, int *B, int *C){
    int i = threadIdx.x+blockDim.x*blockIdx.x;
    int j = threadIdx.y+blockDim.y*blockIdx.y;
    if (i<N && j<N){
        int idx = j+i*N;
        for(int k=0; k<N; k++)
            C[idx] += A[k+i*N]*B[j+k*N];
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
