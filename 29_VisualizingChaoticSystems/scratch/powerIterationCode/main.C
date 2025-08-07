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

    // size of matrix
    int n = 3;

    // initializing matrix
    double A[] = {0,1,2,3,4,5,6,7,8};

    // expected eigen value max = 13.348462
    // corresponding eigen vector = [ 0.16476382,  0.79969966,  0.40824829]

    // initializing vector
    double x_t[n]   = {0};
    double x_tp1[n] = {0};

    initializeRandomUniform(x_t,n,-1.0,1.0,1);

    // setting convergence tolerance
    double tol = 1e-4;

    // declaring eigen value variables
    double lambda_t=0, lambda_tp1=0;

    int maxItr = 1000;

    for(int itr=0; itr<maxItr; itr++){
    }
}


/*---------------------------------------------------------------------------*/
