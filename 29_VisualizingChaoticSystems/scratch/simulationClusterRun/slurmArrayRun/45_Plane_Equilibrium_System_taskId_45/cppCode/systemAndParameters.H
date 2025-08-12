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

    xDot = x*z;
    yDot = 3*x*pow(z,2)-pow(x,2)*y;
    zDot = -pow(x,2)+x*y;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = z;
    jacobian[1] = 0.0;
    jacobian[2] = x;
    jacobian[3] = 3*pow(z,2)-2*x*y;
    jacobian[4] = -pow(x,2);
    jacobian[5] = 6*x*z;
    jacobian[6] = -2*x+y;
    jacobian[7] = x;
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {1,2,-1};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
