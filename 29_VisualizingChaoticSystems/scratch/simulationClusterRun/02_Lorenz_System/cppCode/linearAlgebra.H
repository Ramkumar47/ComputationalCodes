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
     */

    std::cout << std::endl;

    for(unsigned short i =0; i<nRows; i++){
        std::cout << A[i] << " ";
    }

    std::cout << std::endl;

}

// magnitude of a vector-------------------------------------------------------

template <typename T> T vectorMagnitude(T* A, unsigned short nRows){

    /* Input description
     * <type T>* A   - starting address of the input matrix
     * short nRowA - number of rows in the A matrix
     */

    T magVal = 0;
    for(unsigned short i=0; i<nRows; i++){
        magVal += pow(A[i],2);
    }

    return sqrt(magVal);
}


// power iteration function definition-----------------------------------------

/* Description:
 * This function is used to compute the eigen value with maximum magnitude
 * and its corresponding eigen vector for a given square matrix.
 * This function uses power iteration algorithm.
 */
void powerIterationFunction(double* A, unsigned short nSize, double tolerance,
        double& eigenValue, double* eigenVector){

    /* Input description
     * <type T>* A  - starting address of the input square matrix
     * unsigned short nSize - no. of rows/columns in the input square matrix
     * double tolerance - iteration convergence tolerance
     * double& eigenValue - output max mag eigen value
     * double* eigenVector - corresponding eigen vector
     */

    // initializing vector
    double x_t[nSize]   = {0};
    double x_tp1[nSize] = {0};

    initializeRandomUniform(x_t,nSize,-1.0,1.0);

    // declaring eigen value variables
    double lambda_t=0, lambda_tp1=0;

    int maxItr = 1000;

    for(int itr=0; itr<maxItr; itr++){

        // computing x_tp1
        double Ax_t[nSize] = {0};
        vectorMultiplication(A,nSize,nSize,x_t,Ax_t);
        double magAx_t = vectorMagnitude(Ax_t,nSize);

        for(int i=0; i<nSize; i++)
            x_tp1[i] = Ax_t[i]/magAx_t;

        // computing lambda_tp1
        double Ax_tp1[nSize] = {0};
        vectorMultiplication(A,nSize,nSize,x_tp1,Ax_tp1);
        double numerator   = vectorDotProduct(x_tp1,Ax_tp1,nSize);
        double denominator = vectorDotProduct(x_tp1,x_tp1,nSize);
        lambda_tp1 = numerator/denominator;

        // checking convergence
        if (abs(lambda_tp1-lambda_t)<tolerance){
            std::cout << "Power iteation converged in "
                << itr+1 <<" iterations" << std::endl;
            break;
        }

        // updating values for next iteration
        lambda_t = lambda_tp1;
        for(int i =0; i<nSize; i++)
            x_t[i] = x_tp1[i];

    }

    eigenValue = lambda_tp1;
    for(unsigned short i=0; i<nSize; i++)
        eigenVector[i] = x_tp1[i];

}

// sign function---------------------------------------------------------------
template <typename T> int sign(T val) {
    return (T(0) < val) - (val < T(0));
}

/*---------------------------------------------------------------------------*/
