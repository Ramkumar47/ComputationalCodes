/*===========================================================================*\
 * Buncha system simulation
 *
 * Ramkumar
 * Thu Aug  7 07:12:00 PM IST 2025
\*===========================================================================*/

// preprocessor directives
#include<iomanip>
#include<string>
#include<fstream>
#include "linearAlgebra.H"

/*---------------------------------------------------------------------------*/

#include "systemAndParameters.H"

// main file
int main(int argc, char* argv[]){

    // initializing state variables
    double x_t = initialCondition[0];
    double y_t = initialCondition[1];
    double z_t = initialCondition[2];
    double x_tp1=0, y_tp1=0, z_tp1=0;

    int count   = 0;
    double time = 0.0;

    // opening solution file
    std::ofstream fid(fileName);

    fid << "time,x,y,z,L" << std::endl;
    fid << 0 <<"," << x_t << "," << y_t << "," << z_t << "," << 0 << std::endl;

    // begining solution loop
    while (time < endSimTime){

        time += timeStep;

        // RK4 step 1
        double k1_x,k1_y,k1_z;
        chaoticSystemFunction(x_t,y_t,z_t, k1_x,k1_y,k1_z);

        // RK4 step 2
        double k2_x,k2_y,k2_z;
        chaoticSystemFunction(x_t+k1_x/2.0*timeStep,
                      y_t+k1_y/2.0*timeStep,
                      z_t+k1_z/2.0*timeStep, k2_x,k2_y,k2_z);

        // RK4 step 3
        double k3_x,k3_y,k3_z;
        chaoticSystemFunction(x_t+k2_x/2.0*timeStep,
                      y_t+k2_y/2.0*timeStep,
                      z_t+k2_z/2.0*timeStep, k3_x,k3_y,k3_z);

        // RK4 step 4
        double k4_x,k4_y,k4_z;
        chaoticSystemFunction(x_t+k3_x*timeStep,
                      y_t+k3_y*timeStep,
                      z_t+k3_z*timeStep, k4_x,k4_y,k4_z);

        // computing solution of next step
        x_tp1 = x_t + timeStep/6.0*(k1_x+2.0*k2_x+2.0*k3_x+k4_x);
        y_tp1 = y_t + timeStep/6.0*(k1_y+2.0*k2_y+2.0*k3_y+k4_y);
        z_tp1 = z_t + timeStep/6.0*(k1_z+2.0*k2_z+2.0*k3_z+k4_z);

        count++;

        if(count >= writeInterval){
            // computing lyapunov exponent

            double jacobian[9] = {0};
            jacobianMatrixFunction(x_tp1,y_tp1,z_tp1,jacobian);

            double eigenValue, eigenVector[3];
            powerIterationFunction(jacobian,3,lyapunovTolerance,
                    eigenValue,eigenVector);

            double lyapunovExponent = log(abs(eigenValue));

            // writing data to file
            fid << time << ","
                << x_tp1 << ","
                << y_tp1 << ","
                << z_tp1 << ","
                << lyapunovExponent << std::endl;
            count = 0;
        }

        x_t = x_tp1;
        y_t = y_tp1;
        z_t = z_tp1;

        std::cout << "time : " << time << std::endl;
    }

    fid.close();

    std::cout << "End. " << std::endl;

}


/*---------------------------------------------------------------------------*/
