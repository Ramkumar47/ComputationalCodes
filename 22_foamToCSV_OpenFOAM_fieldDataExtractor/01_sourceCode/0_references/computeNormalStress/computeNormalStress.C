/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | Copyright (C) 2011-2017 OpenFOAM Foundation
     \\/     M anipulation  |
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
    computeNormalStress

Description
    this application computes normal stress

\*---------------------------------------------------------------------------*/

#include "fvCFD.H"
#include "immiscibleIncompressibleTwoPhaseMixture.H"
#include "turbulentTransportModel.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

int main(int argc, char *argv[])
{

    #include "setRootCase.H"
    #include "createTime.H"
    #include "createMesh.H"

    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    // setting simulation time to be latest
    instantList Times = runTime.times(); // getting list of all timesteps
    runTime.setTime(Times.last(),0); // setting last timestep as current one

    // creating needed fields and values
    #include "createFields.H"

    // initiating turbulence stuff
    turbulence->validate();

    // computing stress tensor field
    Info << nl << "computing stress tensor field for whole domain" << endl;
    const volTensorField T = 2*mu_eff*fvc::grad(U);

    // looping through boundaries----------------------------------------------
    forAll(mesh.boundaryMesh(), patchId)
    {
        // print status
        Info << nl << "calculating normal stress at boundary : "
             << mesh.boundary()[patchId].name() << endl;

        // obtaining absolute reference of needed field's boundary
        scalarField& sig = normalStress.boundaryFieldRef()[patchId]; // normal stress at boundary
        const vectorField& Sfp = mesh.Sf().boundaryField()[patchId]; // normal vector at boundary
        const scalarField& magSfp = mesh.magSf().boundaryField()[patchId]; // magnitude of normal vector at boundary
        const scalarField& P_b = P.boundaryField()[patchId]; // pressure at boundary

        // obtaining stress tensor field at boundary
        const tensorField T_b = T.boundaryField()[patchId];

        // projecting stress tensor on the boundary
        vectorField sp = (-Sfp/magSfp) & T_b;

        // computing normal stress
        /* sigma = -{pressure} + fluid_stress */
        sig = (-Sfp/magSfp) & sp; // adding fluid stress part
        sig -= P_b; // adding pressure with -ve sign

    }

    // calculating absolute normal stress
    normalStress_absolute = mag(normalStress);

    // writing normal stress field
    Info << nl << "writing normalStress fields to file.." << endl;
    normalStress.write();
    normalStress_absolute.write();

    Info<< nl;
    runTime.printExecutionTime(Info);
    Info<< "End\n" << endl;

    return 0;
}


// ************************************************************************* //
