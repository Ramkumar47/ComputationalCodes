/*===========================================================================*\
 * power iteration main file
 *
 * Ramkumar
 * Wed Aug  6 07:12:24 PM IST 2025
\*===========================================================================*/

// preprocessor directives
#include<iomanip>
#include "linearAlgebra.H"

/*---------------------------------------------------------------------------*/

// main file
int main(int argc, char* argv[]){

    // size of matrix
    int n = 3;

    // initializing matrix
    double A[] = {0,1,2,3,4,5,6,7,8};

    // expected eigen value max = 13.348462
    // corresponding eigen vector = [0.16476382, 0.50577448, 0.84678513]

    double lambda;
    double eigenVector[n]={0};
    powerIterationFunction(A,n,1e-12,lambda,eigenVector);


    std::cout << std::setprecision(12) << "max eigen value = " << lambda << std::endl;
    std::cout << "corresponding eigen vector" << std::endl;
    printVector(eigenVector,n);

    std::cout << " test log value " << log(lambda) << std::endl;


}


/*---------------------------------------------------------------------------*/
