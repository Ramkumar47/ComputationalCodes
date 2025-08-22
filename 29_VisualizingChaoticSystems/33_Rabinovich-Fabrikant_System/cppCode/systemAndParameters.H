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

    xDot = y*z-y+0.6*pow(x,2)*y+x;
    yDot = x*z+x-pow(x,3)+0.07*y;
    zDot = -z-x*y*z;

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 1.0 + 1.2*x*y;
    jacobian[1] = z-1.0+0.6*pow(x,2);
    jacobian[2] = y;
    jacobian[3] = z+1-3*pow(x,2);
    jacobian[4] = 0.07;
    jacobian[5] = x;
    jacobian[6] = -y*z;
    jacobian[7] = -x*z;
    jacobian[8] = -1-x*y;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {2,-1,1};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
