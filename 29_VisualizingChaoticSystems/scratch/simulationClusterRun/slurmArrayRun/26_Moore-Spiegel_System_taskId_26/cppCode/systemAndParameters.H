/*===========================================================================*\
 * chaotic system and parameters definition program
 *
 * Ramkumar
 * Thu Aug  7 07:18:12 PM IST 2025
\*===========================================================================*/

/*---------------------------------------------------------------------------*/

// chaotic system definition
void chaoticSystemFunction(double x, double y, double z,
        double& xDot, double& yDot, double& zDot){

    xDot = y;
    yDot = z;
    zDot = -0.2*z+9*y-pow(x,2)*y-x;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 1.0;
    jacobian[2] = 0.0;
    jacobian[3] = 0.0;
    jacobian[4] = 0.0;
    jacobian[5] = 1.0;
    jacobian[6] = -2*x*y-1;
    jacobian[7] = 9.0-pow(x,2);
    jacobian[8] = -0.2;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-1,-4,9};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
