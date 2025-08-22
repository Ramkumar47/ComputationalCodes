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

    xDot = y+x*y+x*z;
    yDot = 1-pow(x,2)+y*z;
    zDot = x-0.61*pow(x,2)-pow(y,2);

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = y+z;
    jacobian[1] = 1+x;
    jacobian[2] = x;
    jacobian[3] = -2*x;
    jacobian[4] = z;
    jacobian[5] = y;
    jacobian[6] = 1-1.22*x;
    jacobian[7] = -2*y;
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {0.-1,0};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
