/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------

filename: readData.H
description:
        it contains the snippets that read needed data from dictionary

\*---------------------------------------------------------------------------*/

// defining dictionary object
IOdictionary pointDataDict
(
    IOobject
    (
        "pointDataExtractDict",
        runTime.system(),
        mesh,
        IOobject::MUST_READ,
        IOobject::NO_WRITE
    )
);

// reading point indices
labelList pointId (pointDataDict.lookup("pointIndexList"));

// reading patch name
word sourcePatchName (pointDataDict.lookup("sourcePatchName"));

// setting the simulation time to latest
instantList runTimes = runTime.times();
runTime.setTime(runTimes.last(),0);

Info << nl << "setting simulation time = " << runTime.timeName() << endl;

// reading velocity and pressure fields at latest time
Info << nl << "reading solution fields" << endl;
volVectorField U
(
    IOobject
    (
        "U",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::NO_WRITE
    ),
    mesh
);

volScalarField p
(
    IOobject
    (
        "p",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::NO_WRITE
    ),
    mesh
);

