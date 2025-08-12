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

    xDot = -y*z;
    yDot = 2*x*z+y*z+pow(z,3);
    zDot = x-pow(x,3);

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.0;
    jacobian[1] = -z;
    jacobian[2] = -y;
    jacobian[3] = 2*z;
    jacobian[4] = z;
    jacobian[5] = 2*x+3*pow(z,2);
    jacobian[6] = 1-3*pow(x,2);
    jacobian[7] = 0.0;
    jacobian[8] = 0.0;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-1,1,-1};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
