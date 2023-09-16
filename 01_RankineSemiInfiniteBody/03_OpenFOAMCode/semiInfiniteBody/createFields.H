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

// radial velocity field
volScalarField Vr
(
    IOobject
    (
        "Vr",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

// azimuthal velocity field
volScalarField V_theta
(
    IOobject
    (
        "V_theta",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

// radial direction field
volScalarField r
(
    IOobject
    (
        "r",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

// azimuthal direction field (theta)
volScalarField theta
(
    IOobject
    (
        "theta",
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
const point sourceCenter = transportProperties.lookupOrDefault<point>("sourceCenter",vector(0,0,0));

// reading freestream velocity magnitude
const scalar V_inf = transportProperties.lookupOrDefault<scalar>("V_inf",0);

// reading source strength
const scalar gamma = transportProperties.lookupOrDefault<scalar>("gamma",0);
