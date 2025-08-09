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

    xDot = 0.3*y;
    yDot = -x-z*y;
    zDot = abs(y)-1;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 0.3;
    jacobian[2] = 0.0;
    jacobian[3] = -1.0;
    jacobian[4] = -z;
    jacobian[5] = -y;
    jacobian[6] = 0.0;
    jacobian[7] = sign(y);
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-1,5,0};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
