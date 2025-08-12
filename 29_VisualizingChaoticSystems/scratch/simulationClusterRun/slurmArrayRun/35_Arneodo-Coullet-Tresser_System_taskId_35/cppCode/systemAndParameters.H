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

    xDot = 0.58*x-y;
    yDot = -y+x*z+pow(x,3);
    zDot = -0.2*z+x*y-pow(z,2);

}

// jacobian of chaotic system definition
void jacobianMatrixFunction(double x, double y, double z, double* jacobian){

    // filling in row-major order
    jacobian[0] = 0.58;
    jacobian[1] = -1.0;
    jacobian[2] = 0.0;
    jacobian[3] = z+3*pow(x,2);
    jacobian[4] = -1.0;
    jacobian[5] = x;
    jacobian[6] = y;
    jacobian[7] = x;
    jacobian[8] = -0.2-2*z;
}

// computation parameters definition

double timeStep           = 1e-5;

double endSimTime         = 10000.0;

int writeInterval         = 1000;

std::string fileName      = "solutionData.csv";

double initialCondition[] = {-2,-1,0};

double lyapunovTolerance  = 1e-7;

/*---------------------------------------------------------------------------*/
