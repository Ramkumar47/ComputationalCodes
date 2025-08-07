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

    xDot = z;
    yDot = x*y+x*z;
    zDot = -0.1*pow(x,3)+pow(y,3);

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = 0.0;
    jacobian[2] = 1.0;
    jacobian[3] = y+z;
    jacobian[4] = x;
    jacobian[5] = z;
    jacobian[6] = -0.1*3*pow(x,2);
    jacobian[7] = 3*pow(y,2);
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-4;

double endSimTime         = 1000.0;

int writeInterval         = 100;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-1,0.0,0.0};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
