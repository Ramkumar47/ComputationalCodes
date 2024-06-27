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
    foamToCSV

Description
    this custom application dumps OpenFOAM solution field values into csv files

\*---------------------------------------------------------------------------*/

#include "fvCFD.H"
#include "IOobjectList.H"
#include "turbulentTransportModel.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

int main(int argc, char *argv[])
{
    argList::addNote
    (
        "this application writes OF solution fields into csv files"
    );

    argList::addBoolOption
    (
        "latestTime",
        "takes only latest timestep solution fields for conversion"
    );

    #include "setRootCase.H"
    #include "createTime.H"
    #include "createMesh.H"

    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    // checking latestTime option bool
    const bool takeLatestTime = args.found("latestTime");

    // making a directory to store CSV files
    Info << nl << "creating CSV directory..." << endl;
    fileName masterDirectory = mesh.time().path()/"CSV";
    mkDir(masterDirectory);

    // getting list of times
    instantList Times = runTime.times();

    // setting starting index for time directories
    label startIndex(0);
    if (takeLatestTime) // if to take only latestTime step
        startIndex = runTime.times().size()-3; // skipping 0 & constant folder,

    // declaring pointer for csv files
    autoPtr<OFstream> filePtr;

    // for(const instant& time : Times)
    for(label I = startIndex; I < Times.size()-2; I++) // skipping 0 and constant folder
    {
        // setting current time
        runTime.setTime(Times[I+2], 0);

        // making subdirectory to store csv files
        fileName timeDirectory = masterDirectory/runTime.timeName();
        mkDir(timeDirectory);

        // getting list of objects under current time
        IOobjectList objects(mesh, runTime.timeName());

        Info << nl << "current Time : " << runTime.timeName() << endl;

        // working on volScalarFields
        if (objects.sortedNames(volScalarField::typeName).size() > 0)
        {
            #include "writeVolScalarFields.H"
        }

        // working on volVectorFields
        if (objects.sortedNames(volVectorField::typeName).size() > 0)
        {
            #include "writeVolVectorFields.H"
        }

        // working on surfaceScalarFields
        if (objects.sortedNames(surfaceScalarField::typeName).size() > 0)
        {
            #include "writeSurfaceScalarFields.H"
        }

        // working on surfaceVectorFields
        if (objects.sortedNames(surfaceVectorField::typeName).size() > 0)
        {
            #include "writeSurfaceVectorFields.H"
        }

        // working on boundaryScalarFields
        if (objects.sortedNames(surfaceScalarField::typeName).size()
                + objects.sortedNames(volScalarField::typeName).size() > 0)
        {
            #include "writeBoundaryScalarFields.H"
        }

        // working on boundaryVectorFields
        if (objects.sortedNames(surfaceVectorField::typeName).size()
                + objects.sortedNames(volVectorField::typeName).size() > 0)
        {
            #include "writeBoundaryVectorFields.H"
        }

    }

    Info<< nl;
    runTime.printExecutionTime(Info);

    Info<< "End\n" << endl;

    return 0;
}


// ************************************************************************* //
