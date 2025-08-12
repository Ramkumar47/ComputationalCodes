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

    xDot = -0.32*x-y-z-pow(y,2);
    yDot = -0.32*y-z-x-pow(z,2);
    zDot = -0.32*z-x-y-pow(x,2);

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = -0.32;
    jacobian[1] = -1-2*y;
    jacobian[2] = -1.0;
    jacobian[3] = -1.0;
    jacobian[4] = -0.32;
    jacobian[5] = -1-2*z;
    jacobian[6] = -1.0-2*x;
    jacobian[7] = -1.0;
    jacobian[8] = -0.32;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-2,0,0};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
