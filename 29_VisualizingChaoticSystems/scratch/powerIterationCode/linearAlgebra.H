/*===========================================================================*\
 * linear algebra functions definition
 *
 * Ramkumar
 * Sat Jul  5 09:09:07 PM IST 2025
\*===========================================================================*/

/* Index of functions:---------------------------------------------------------

 * vectorMultiplication    - matrix-matrix, matrix-vector multiplication function;
 * vectorDotProduct        - dot product function of 2 vectors
 * printMatrix             - prints matrix to the screen;
 * initializeRandomUniform - initializes given array with random values
            derived from uniform distribution within given range.
 * printVector             - prints vector in space-separated form on screen
-----------------------------------------------------------------------------*/

// preprocessor directives
#include<iostream>
#include<math.h>
#include<random>


/*---------------------------------------------------------------------------*/

// defining vector multiplication function-------------------------------------

// matrix-matrix multiplication

template <typename T> void vectorMultiplication(T* A, unsigned short nRowA,
        unsigned short nColA, T* B, unsigned short nRowB, unsigned short nColB,
        T* C){

    /* Input description
     * double* A   - starting address of  first matrix in row major form
     * short nRowA - number of rows in A matrix
     * short nColA - number of columns in A matrix
     * double* B   - starting address of second matrix in row major form
     * short nRowB - number of rows in B matrix
     * short nColB - number of columns in B matrix
     * double* C   - starting address of the output matrix
     */

    for(short i=0; i<nRowA; i++){
        for(short j=0; j<nColB; j++){
            int cIdx = i*nColB+j;
            for (short k=0; k<nColA; k++){ // nColA == nRowB
                int aIdx = i*nColA+k;
                int bIdx = k*nColB+j;
                C[cIdx] += A[aIdx]*B[bIdx];
            }
        }
    }
}

// matrix-vector multiplication
template <typename T> void vectorMultiplication(T* A, unsigned short nRowA,
        unsigned short nColA, T* B, T *C){

    /* Input description
     * int* A      - starting address of  first matrix in row major form
     * short nRowA - number of rows in A matrix
     * short nColA - number of columns in A matrix
     * int* B      - starting address of the vector in row major form
     * int* C      - starting address of the output vector
     */

    for(unsigned short i=0; i< nRowA; i++){
        T sumVal = 0;
        for(unsigned short j=0; j< nColA; j++){
            int aIdx = i*nRowA+j;
            sumVal += A[aIdx]*B[j];
        }
        C[i] = sumVal;
    }
}

// dot product of vectors
template <typename T> T vectorDotProduct(T* A, T* B, unsigned short nRows){

    /* Input description
     * int* A      - starting address of  first vector
     * int* B      - starting address of second vector
     * short nRows - number of rows in both vectors
     */

    T sumVal = 0;
    for(unsigned short i=0; i < nRows; i++){
        sumVal += A[i]*B[i];
    }

    return sumVal;

}

// random number initializer function------------------------------------------

void initializeRandomUniform(double* A, int size, double minRange,
        double maxRange, int seed=0){

    /* Input description
     * double* A       - starting address of input array
     * int size        - number of elements in the input array
     * double minRange - starting value of the uniform distribution range
     * double maxRange - ending value of the uniform distribution range
     * int seed        - seed value for reproducibility
     */

    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_real_distribution dist(minRange, maxRange);

    if(seed!=0)
        mt.seed(seed);

    for(int i=0; i<size; i++)
        A[i] = dist(mt);

}

void initializeRandomUniform(long* A, int size, long minRange,
        long maxRange, int seed=0){

    /* Input description
     * long* A         - starting address of input array
     * int size        - number of elements in the input array
     * long minRange   - starting value of the uniform distribution range
     * long maxRange   - ending value of the uniform distribution range
     * int seed        - seed value for reproducibility
     */

    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution dist(minRange, maxRange);

    if(seed!=0)
        mt.seed(seed);

    for(int i=0; i<size; i++)
        A[i] = dist(mt);

}

void initializeRandomUniform(int* A, int size, int minRange,
        int maxRange, int seed=0){

    /* Input description
     * int* A          - starting address of input array
     * int size        - number of elements in the input array
     * int minRange    - starting value of the uniform distribution range
     * int maxRange    - ending value of the uniform distribution range
     * int seed        - seed value for reproducibility
     */

    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution dist(minRange, maxRange);

    if(seed!=0)
        mt.seed(seed);

    for(int i=0; i<size; i++)
        A[i] = dist(mt);

}

// print matrix----------------------------------------------------------------

template <typename T> void printMatrix(T* A, unsigned short nRowA, unsigned short nColA){

    /* Input description
     * <type T>* A   - starting address of the input matrix
     * short nRowA - number of rows in the A matrix
     * short nColA - number of cols in the A matrix
     */

    std::cout << "\n" << std::endl;
    for(unsigned short i=0; i<nRowA; i++){
        for(unsigned short j=0; j<nColA; j++){
            int idx=i*nColA+j;
            std::cout << A[idx] << " ";
        }
        std::cout << "\n";
    }
}

// print vector----------------------------------------------------------------

template <typename T> void printVector(T A, unsigned short nRows){

    /* Input description
     * <type T>* A   - starting address of the input matrix
     * short nRowA - number of rows in the A matrix
     * short nColA - number of cols in the A matrix
     */

    std::cout << std::endl;

    for(unsigned short i =0; i<nRows; i++){
        std::cout << A[i] << " ";
    }

    std::cout << std::endl;

}

/*---------------------------------------------------------------------------*/
