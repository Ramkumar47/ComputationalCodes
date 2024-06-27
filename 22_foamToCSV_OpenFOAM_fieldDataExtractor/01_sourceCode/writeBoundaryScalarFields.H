/*
 * writing boundaryScalarFields to the csv file
 */

Info << tab << " writing boundaryScalarFields.csv " << endl;

// preparing lists for volScalarFields and its filenames
label N_vsf = objects.sortedNames(volScalarField::typeName).size();
label N_ssf = objects.sortedNames(surfaceScalarField::typeName).size();

List<autoPtr<volScalarField>> vsf_list(N_vsf);
List<autoPtr<surfaceScalarField>> ssf_list(N_ssf);

// adding volScalarFields to the list
for(label i = 0; i < N_vsf; i++)
{
    // getting field name
    word fieldName = objects.sortedNames(volScalarField::typeName)[i];
    // adding volScalarField to the list
    vsf_list[i].reset
    (
        new volScalarField
        (
            IOobject
            (
                fieldName,
                runTime.timeName(),
                mesh,
                IOobject::MUST_READ,
                IOobject::AUTO_WRITE
            ),
            mesh
        )
    );
}

// adding surfaceScalarFields to the list
for(label i = 0; i < N_ssf; i++)
{
    // getting field name
    word fieldName = objects.sortedNames(surfaceScalarField::typeName)[i];
    // adding surfaceScalarField to the list
    ssf_list[i].reset
    (
        new surfaceScalarField
        (
            IOobject
            (
                fieldName,
                runTime.timeName(),
                mesh,
                IOobject::MUST_READ,
                IOobject::AUTO_WRITE
            ),
            mesh
        )
    );
}

// initializing csv file path
filePtr.reset(new OFstream(timeDirectory/"boundaryScalarFields.csv"));

// writing headers to the csv file
filePtr() << "patchName,X,Y,Z";

for(const word& fieldName : objects.sortedNames(volScalarField::typeName))
    filePtr() << "," << fieldName;

for(const word& fieldName : objects.sortedNames(surfaceScalarField::typeName))
    filePtr() << "," << fieldName;
filePtr() << endl;

// looping through boundary patches
forAll(mesh.boundary(), patchI)
{
    // getting patch name
    word patchName = mesh.boundary()[patchI].name();

    // getting patch face size indices
    label faceCount = mesh.boundary()[patchI].Cf().size();

    // looping through boundary patch faces
    for(label i = 0; i < faceCount; i++)
    {
        // writing patch name and face coordinates
        filePtr() << patchName << "," << mesh.boundary()[patchI].Cf()[i].x()
                  << "," << mesh.boundary()[patchI].Cf()[i].y()
                  << "," << mesh.boundary()[patchI].Cf()[i].z();

        // looping through volume fields
        for(label j = 0; j < N_vsf; j++)
            filePtr() << "," << vsf_list[j][0].boundaryField()[patchI][i];

        // looping through surface fields
        for(label j = 0; j < N_ssf; j++)
            filePtr() << "," << ssf_list[j][0].boundaryField()[patchI][i];

        filePtr() << endl;
    }
}
