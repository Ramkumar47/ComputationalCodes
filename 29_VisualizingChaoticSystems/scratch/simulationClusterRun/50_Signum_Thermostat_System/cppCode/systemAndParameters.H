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
    yDot = -x-2*sign(z)*y;
    zDot = pow(y,2)-1;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 1.0;
    jacobian[2] = 0.0;
    jacobian[3] = -1.0;
    jacobian[4] = -2*sign(z);
    jacobian[5] = 0.0;
    jacobian[6] = 0.0;
    jacobian[7] = 2*y;
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {1,-2,0};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
