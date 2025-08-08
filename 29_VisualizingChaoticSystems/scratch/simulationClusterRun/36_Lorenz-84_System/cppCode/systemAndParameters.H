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

    xDot = -1.0*pow(y,2)-pow(z,2)-x+1.0;
    yDot = x*y-x*z-0.1*y+1.0;
    zDot = x*y+x*z-z;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = -1.0;
    jacobian[1] = -2*y;
    jacobian[2] = -2*z;
    jacobian[3] = -z;
    jacobian[4] = 1.0-0.1;
    jacobian[5] = -x;
    jacobian[6] = y;
    jacobian[7] = x;
    jacobian[8] = x-1.0;
}

// computation parameters definition

double timeStep           = 1e-3;

double endSimTime         = 1000.0;

int writeInterval         = 100;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {1,1,1};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
