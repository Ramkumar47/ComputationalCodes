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

    xDot = 2.7*y+z;
    yDot = -x+pow(y,2);
    zDot = x+y;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 2.7;
    jacobian[2] = 1.0;
    jacobian[3] = -1.0;
    jacobian[4] = 2.0*y;
    jacobian[5] = 0.0;
    jacobian[6] = 1.0;
    jacobian[7] = 1.0;
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {1,1,-1};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
