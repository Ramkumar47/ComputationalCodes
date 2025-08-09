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

    xDot = y*z+0.1;
    yDot = pow(x,2)-2*y;
    zDot = 1-x;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = z;
    jacobian[2] = y;
    jacobian[3] = 2*x;
    jacobian[4] = -2.0;
    jacobian[5] = 0.0;
    jacobian[6] = -1.0;
    jacobian[7] = 0.0;
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-3,8,1};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
