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

    xDot = 1-0.52*y;
    yDot = 1+z;
    zDot = x*y-z;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = -0.52;
    jacobian[2] = 0.0;
    jacobian[3] = 0.0;
    jacobian[4] = 0.0;
    jacobian[5] = 1.0;
    jacobian[6] = y;
    jacobian[7] = x;
    jacobian[8] = -1.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-1,-3,3};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
