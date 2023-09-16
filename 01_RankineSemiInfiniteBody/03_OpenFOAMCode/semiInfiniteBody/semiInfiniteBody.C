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
    semiInfiniteBody

Description

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

    // calculating fields
    forAll(mesh.cells(),cellId)
    {
        // calculating r value
        r[cellId] = Foam::mag(mesh.C()[cellId] - sourceCenter);

        // calculating theta value
        theta[cellId] = Foam::atan2(mesh.C()[cellId].y() - sourceCenter.y(),
                                mesh.C()[cellId].x() - sourceCenter.x());

        // calculating shi
        const scalar PI = Foam::atan(1.0)*4.0;
        Shi[cellId] = V_inf * r[cellId]*Foam::sin(theta[cellId]) +
                        gamma/2.0/PI*theta[cellId];

        // calculating polar velocities
        Vr[cellId] = V_inf*Foam::cos(theta[cellId]) + gamma/2.0/PI/r[cellId];
        V_theta[cellId] = -V_inf*Foam::sin(theta[cellId]);

        // calculating cartesian velocity field
        scalar Ux = Vr[cellId]*Foam::cos(theta[cellId]) -
                            r[cellId]*V_theta[cellId]*Foam::sin(theta[cellId]);
        scalar Uy = Vr[cellId]*Foam::sin(theta[cellId]) +
                            r[cellId]*V_theta[cellId]*Foam::cos(theta[cellId]);
        U[cellId] = vector(Ux,Uy,0.0);
    }

    // updating fields
    r.write();
    theta.write();
    Shi.write();
    Vr.write();
    V_theta.write();
    U.write();

    Info<< nl;
    runTime.printExecutionTime(Info);

    Info<< "End\n" << endl;

    return 0;
}


// ************************************************************************* //
