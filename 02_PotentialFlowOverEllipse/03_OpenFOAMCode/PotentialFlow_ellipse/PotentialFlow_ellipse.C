/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2022 AUTHOR,AFFILIATION
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Application
    PotentialFlow_ellipse

Description
    this code solves potential flow over ellipse using a combination of
    potential flow elements: source, sink and uniform flow.

\*---------------------------------------------------------------------------*/

#include "fvCFD.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

int main(int argc, char *argv[])
{
    #include "setRootCase.H"
    #include "createTime.H"
    #include "createMesh.H"

    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    // setting simulation time
    runTime.setTime(0,0);

    // creating needed fields
    #include "createFields.H"

    // calculating Shi field values of all cell centers
    forAll(mesh.cells(),cellId)
    {
        // calculating radius values: r, r_source and r_sink
        /*
         * here r - radial distance from global origin
         * r_source - radial distance from source center
         * r_sink - radial distance from sink center
         */
        scalar r = Foam::mag(mesh.C()[cellId] - originVector);
        /*
         * here r_source and r_sink are not used in any calculations,
         * it is shown just for understanding purpose only
        scalar r_source = Foam::mag(mesh.C()[cellId] - source_center);
        scalar r_sink = Foam::mag(mesh.C()[cellId] - sink_center);
         */

        // calculating theta values: theta, theta_source and theta_sink
        /*
         * here theta - angle of vector w.r.t x-axis from global origin
         * theta_source - angle of vector w.r.t x-axis from source center
         * theta_sink - angle of vector w.r.t x-axis from sink center
         */
        scalar theta, theta_source, theta_sink;
        theta = Foam::atan2(mesh.C()[cellId].y() - originVector.y(),
                                mesh.C()[cellId].x() - originVector.x());
        theta_source = Foam::atan2(mesh.C()[cellId].y() - source_center.y(),
                                mesh.C()[cellId].x() - source_center.x());
        theta_sink = Foam::atan2(mesh.C()[cellId].y() - sink_center.y(),
                                mesh.C()[cellId].x() - sink_center.x());

        // calculating shi
        Shi[cellId] = V_inf*r*Foam::sin(theta) +
                        gamma_source/2.0/PI*theta_source +
                        gamma_sink/2.0/PI*theta_sink;

    }

    // looping through boundary patches for calculating Shi field
    forAll(mesh.boundary(), patchId)
    {
        // getting the no. of faces in current boundary
        const label faceCount = mesh.boundary()[patchId].Cf().size();

        // looping through boundary faces
        for(label i = 0; i < faceCount; i++)
        {
            // getting center coordinates of current face
            scalar Xf = mesh.boundary()[patchId].Cf()[i].x();
            scalar Yf = mesh.boundary()[patchId].Cf()[i].y();

            // calculating radius and theta values just like above
            scalar r, theta, theta_source, theta_sink;
            r = Foam::mag(vector(Xf,Yf,0) - originVector);
            theta = Foam::atan2(Yf - originVector.y(),
                                        Xf - originVector.x());
            theta_source = Foam::atan2(Yf - source_center.y(),
                                        Xf - source_center.x());
            theta_sink = Foam::atan2(Yf - sink_center.y(),
                                        Xf - sink_center.x());

            // calculating shi for the boundary face
            Shi.boundaryFieldRef()[patchId][i] = V_inf*r*Foam::sin(theta) +
                            gamma_source/2.0/PI*theta_source +
                            gamma_sink/2.0/PI*theta_sink;
        }
    }

    // taking gradient of field Shi, to the the cartesian velocities
    volVectorField VelocityField = fvc::grad(Shi);

    // looping through cells to calculate cartesian velocities
    forAll(mesh.cells(),cellId)
    {
        // x-component velocity
        /*
         * Ux = d(shi)/dy
         */
        scalar Ux = VelocityField[cellId].y();

        // y-component velocity
        /*
         * Uy = -d(shi)/dx
         */
        scalar Uy = VelocityField[cellId].x()*-1;

        // assembling velocity components into the vector field
        U[cellId] = vector(Ux,Uy,0);
    }

    // updating fields
    Shi.write();
    U.write();

    Info<< nl;
    runTime.printExecutionTime(Info);

    Info<< "End\n" << endl;

    return 0;
}


// ************************************************************************* //
