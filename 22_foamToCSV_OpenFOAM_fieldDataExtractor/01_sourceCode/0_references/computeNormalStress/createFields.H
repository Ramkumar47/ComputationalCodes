
Info<< "Reading field U\n" << endl;
volVectorField U
(
    IOobject
    (
        "U",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

#include "createPhi.H"


Info<< "Reading transportProperties\n" << endl;
immiscibleIncompressibleTwoPhaseMixture mixture(U, phi);

volScalarField& alpha1(mixture.alpha1());
volScalarField& alpha2(mixture.alpha2());

const dimensionedScalar& rho1 = mixture.rho1();
const dimensionedScalar& rho2 = mixture.rho2();


// density
volScalarField rho
(
    IOobject
    (
        "rho",
        runTime.timeName(),
        mesh,
        IOobject::READ_IF_PRESENT
    ),
    alpha1*rho1 + alpha2*rho2
);
rho.oldTime();


// Construct incompressible turbulence model
autoPtr<incompressible::turbulenceModel> turbulence
(
    incompressible::turbulenceModel::New(U, phi, mixture)
);

// turbulent kinematic viscosity field
volScalarField nut
(
    IOobject
    (
        "nut",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

// pressure field in Pa. units
volScalarField P
(
    IOobject
    (
        "p",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

// alpha.water field
volScalarField alpha_water
(
    IOobject
    (
        "alpha.water",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

// new normalStress field
volScalarField normalStress
(
    IOobject
    (
        "normalStress",
        mesh.time().timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedScalar
    (
        "normalStress",
        // sqr(dimLength)/sqr(dimTime),
        dimensionSet(1,-1,-2,0,0,0,0), // N/m^2
        0
    )
);

// new absolute_normalStress field. i.e normalStress_absolute = | normalStress |
volScalarField normalStress_absolute
(
    IOobject
    (
        "normalStress_absolute",
        mesh.time().timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedScalar
    (
        "normalStress_absolute",
        // sqr(dimLength)/sqr(dimTime),
        dimensionSet(1,-1,-2,0,0,0,0), // N/m^2
        0
    )
);

// reading transportProperties dictionary
IOdictionary transportProperties
(
    IOobject
    (
        "transportProperties",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE
    )
);

// reading kinematic viscosity of air and water
dimensionedScalar nu_air
(
    "nu",
    dimViscosity,
    transportProperties.subDict("air") // "air" is the subDict name given in transportProperties dict
);

dimensionedScalar nu_water
(
    "nu",
    dimViscosity,
    transportProperties.subDict("water") // "water" is the subDict name given in transportProperties dict
);

// creating new field for viscosity

volScalarField kinematic_viscosity
(
    IOobject
    (
        "kyn_viscosity",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    alpha1*nu_water + alpha2*nu_air
);

volScalarField mu_eff // effective dynamic viscosity
(
    IOobject
    (
        "mu_eff",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    (kinematic_viscosity + nut)*rho
);
