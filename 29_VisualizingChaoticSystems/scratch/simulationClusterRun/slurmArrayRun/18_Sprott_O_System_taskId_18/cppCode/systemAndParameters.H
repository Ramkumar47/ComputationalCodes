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
    yDot = -x+z;
    zDot = x+x*z+0.3*y;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 1.0;
    jacobian[2] = 0.0;
    jacobian[3] = -1.0;
    jacobian[4] = 0.0;
    jacobian[5] = 1.0;
    jacobian[6] = 1.0+z;
    jacobian[7] = 0.3;
    jacobian[8] = x;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-2,0,-1};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
