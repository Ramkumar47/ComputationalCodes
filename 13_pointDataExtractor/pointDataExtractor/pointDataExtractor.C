/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
    Copyright (C) 2023 AUTHOR,AFFILIATION
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
    pointDataExtractor

Description
    This application is used to interpolate and extract pointField data from
    a given set of point Ids that lie on a patch surface.

    Developed for Unsteady Jet Flow simulation project under Dr.Vinoth B.R.

\*---------------------------------------------------------------------------*/

#include "fvCFD.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// function declarations
labelList checkFaceOnBoundary(labelList faceList, labelList patchFaces);

// main function definition----------------------------------------------------
int main(int argc, char *argv[])
{
    argList::addNote
    (
        "This application extracts data from mesh points (specified through dict)\n"
        "that lie on the specified patch"
    );

    #include "setRootCase.H"
    #include "createTime.H"
    #include "createMesh.H"

    // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

    // reading data from dictionary
    #include "readData.H"

    // extracting face points from given patch
    #include "extractPatchData.H"

    // writing extracted data to file
    #include "writeData.H"

    Info<< nl;
    runTime.printExecutionTime(Info);

    Info<< "End\n" << endl;

    return 0;
}

// function definitions--------------------------------------------------------
labelList checkFaceOnBoundary(labelList faceList, labelList patchFaces)
{
    // getting size of lists
    label Nf = patchFaces.size();
    label Ni = faceList.size();

    // creating empty list to store matched faces
    labelList matchedFaces;

    // looping through to get matched faces
    for(int i = 0; i < Ni ; i++)
    {
        for(int j = 0; j < Nf; j++)
        {
            if (faceList[i] == patchFaces[j])
            {
                matchedFaces.append(faceList[i]);
                break;
            }
        }
    }

    return matchedFaces;
}

// ************************************************************************* //
