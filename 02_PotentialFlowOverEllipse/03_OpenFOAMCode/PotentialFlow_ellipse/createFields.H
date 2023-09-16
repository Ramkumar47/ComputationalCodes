/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | www.openfoam.com
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/

// creating needed fields
Info << nl << "creating needed fields" << endl;

// stream function field
volScalarField Shi
(
    IOobject
    (
        "Shi",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

// velocity field
volVectorField U
(
    IOobject
    (
        "U",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);


// initializing transportProperties dictionary
IOdictionary transportProperties
(
    IOobject
    (
        "transportProperties",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ,
        IOobject::NO_WRITE
    )
);

// reading the center of source
const point source_center = transportProperties.lookupOrDefault<point>("source_center",vector(0,0,0));

// reading the center of sink
const point sink_center = transportProperties.lookupOrDefault<point>("sink_center",vector(0,0,0));

// reading freestream velocity magnitude
const scalar V_inf = transportProperties.lookupOrDefault<scalar>("V_inf",0);

// reading source strength
const scalar gamma_source = transportProperties.lookupOrDefault<scalar>("gamma_source",0);

// reading sink strength
const scalar gamma_sink = transportProperties.lookupOrDefault<scalar>("gamma_sink",0);

// fixing origin vector and PI value
const vector originVector(0,0,0);
const scalar PI = Foam::atan(1.0)*4.0;
