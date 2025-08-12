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

    xDot = 5*y;
    yDot = -x+0.1*y*cos(x)+sin(z);
    zDot = 1.0;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 5.0;
    jacobian[2] = 0.0;
    jacobian[3] = -1.0-0.1*y*sin(x);
    jacobian[4] = 0.1*cos(x);
    jacobian[5] = cos(z);
    jacobian[6] = 0.0;
    jacobian[7] = 0.0;
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {0,1,-3};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
