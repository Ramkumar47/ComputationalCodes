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

    xDot = -x+y+y*z;
    yDot = -32*x-y+x*y;
    zDot = z-x*y;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = -1.0;
    jacobian[1] = 1.0+z;
    jacobian[2] = y;
    jacobian[3] = -32+y;
    jacobian[4] = -1+x;
    jacobian[5] = 0.0;
    jacobian[6] = -y;
    jacobian[7] = -x;
    jacobian[8] = 1.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-1,5,-2};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
