/*===========================================================================*\
 * power iteration main file
 *
 * Ramkumar
 * Wed Aug  6 07:12:24 PM IST 2025
\*===========================================================================*/

// preprocessor directives
#include "linearAlgebra.H"

/*---------------------------------------------------------------------------*/

// main file
int main(int argc, char* argv[]){

    int nRowA = 3, nColA = 3;
    int A[nRowA*nColA] = {0};
    int x[nColA] = {0};
    int b[nRowA] = {0};

    initializeRandomUniform(A,nRowA*nColA,-10,10,1);
    initializeRandomUniform(x,nColA,-10,10,1);

    printMatrix(A,nRowA,nColA);
    printVector(x,nColA);

    vectorMultiplication(A,nRowA,nColA,x,b);

    printVector(b,nRowA);

    int val = vectorDotProduct(b,b,nRowA);

    std::cout << val << std::endl;

    double c[nColA] = {0};

    intializeRandomUniform(c,nColA,1);

    double val2 = vectorDotProduct(c,c,nColA);

    std::cout << val2 << std::endl;


}


/*---------------------------------------------------------------------------*/
