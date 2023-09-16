/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------

filename: writeData.H
description:
    it contains snippets for writing extracted data to file

\*---------------------------------------------------------------------------*/

// preparing directory and filename to store data
fileName outputDir = mesh.time().path()/"extractedPointData";
mkDir(outputDir);
fileName outputFile = "pointData.csv";

// creating file pointer
autoPtr<OFstream> dataFilePtr;
dataFilePtr.reset(new OFstream(outputDir/outputFile));

Info << nl << "writing data to file : " << outputDir/outputFile << endl;

// writing header to the file
dataFilePtr() << "pointId,X,Y,Z,Ux,Uy,Uz,p" << endl;

// writing data to file
forAll(pointId, id)
{
    // extracting current point id
    label pid = pointId[id];

    // extracting X,Y,Z coordinates
    scalar X = mesh.points()[pid].x();
    scalar Y = mesh.points()[pid].y();
    scalar Z = mesh.points()[pid].z();

    // extracting individual velocity components
    scalar Ux = U_values[id].x();
    scalar Uy = U_values[id].y();
    scalar Uz = U_values[id].z();

    // extracting pressure value
    scalar p = p_values[id];

    // writing to file
    dataFilePtr() << pid << "," << X << "," << Y << "," << Z << ","
                  << Ux << "," << Uy << "," << Uz << "," << p << endl;
}

Info << nl << "done" << endl;
