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

    xDot = -z;
    yDot = x-0.5*y;
    zDot = x+pow(y,2)+0.28*z;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 0.0;
    jacobian[2] = -1.0;
    jacobian[3] = 1.0;
    jacobian[4] = -0.5;
    jacobian[5] = 0.0;
    jacobian[6] = 1.0;
    jacobian[7] = 2.0*y;
    jacobian[8] = 0.28;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {0,1,0};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
