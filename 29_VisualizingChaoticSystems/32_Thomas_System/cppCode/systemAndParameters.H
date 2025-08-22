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

    xDot = -0.1*x+sin(y);
    yDot = -0.1*y+sin(z);
    zDot = -0.1*z+sin(x);

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = -0.1;
    jacobian[1] = cos(y);
    jacobian[2] = 0.0;
    jacobian[3] = 0.0;
    jacobian[4] = -0.1;
    jacobian[5] = cos(z);
    jacobian[6] = cos(x);
    jacobian[7] = 0.0;
    jacobian[8] = -0.1;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-1,-2,2};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
