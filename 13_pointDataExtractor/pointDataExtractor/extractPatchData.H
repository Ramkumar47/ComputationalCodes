/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------

filename: extractPatchData.H
description:
    it contains snippets for extracting flow and mesh field data from domain

\*---------------------------------------------------------------------------*/

// getting patchId of source patch
label sourcePatchId = mesh.boundaryMesh().findPatchID(sourcePatchName);

// getting faces list on the source boundary
label startFaceId = mesh.boundary()[sourcePatchId].start();
label faceCount = mesh.boundary()[sourcePatchId].size();

// preparing patch faces list
Info << nl << "extracting patch faces" << endl;
labelList patchFaceIds(0);
for(int i = 0; i < faceCount; i++)
{
    patchFaceIds.append(i + startFaceId);
}

// preparing lists to store the extracted field values
scalarList p_values;
vectorList U_values;

// extracting data on all the points given
Info << nl << "extracting data on all given points" << endl;
forAll(pointId, idx)
{
    // getting current point index
    label pid = pointId[idx];

    // extracting faces that share the current point
    labelList pointFaces = mesh.pointFaces()[pid];

    // getting ids of faces that lie on the chosen patch
    labelList currentFaces = checkFaceOnBoundary(pointFaces, patchFaceIds);

    // averaging face field values to the current point
    scalar p_point(0); vector U_point(0,0,0);
    for(int i = 0; i < currentFaces.size(); i++)
    {
        // getting pressure
        p_point += p.boundaryField()[sourcePatchId][currentFaces[i]-startFaceId];

        // getting velocity
        U_point += U.boundaryField()[sourcePatchId][currentFaces[i]-startFaceId];

    }
    p_point = p_point/currentFaces.size();
    U_point = U_point/currentFaces.size();

    // appending data to list
    p_values.append(p_point);
    U_values.append(U_point);
}
