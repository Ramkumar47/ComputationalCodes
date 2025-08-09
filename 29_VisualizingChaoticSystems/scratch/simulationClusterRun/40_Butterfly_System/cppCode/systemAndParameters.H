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

    xDot = y+y*z;
    yDot = -x*z+y*z;
    zDot = -0.5*z-x*y+1;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 1+z;
    jacobian[2] = y;
    jacobian[3] = -z;
    jacobian[4] = z;
    jacobian[5] = -x+y;
    jacobian[6] = -y;
    jacobian[7] = -x;
    jacobian[8] = -0.5;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {2,1,1};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
