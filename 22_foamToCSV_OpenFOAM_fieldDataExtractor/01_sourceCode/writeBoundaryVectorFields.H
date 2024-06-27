/*
 * writing boundaryVectorFields to the csv file
 */

Info << tab << " writing boundaryVectorFields.csv " << endl;

// preparing lists for volVectorFields and its filenames
label N_vsf = objects.sortedNames(volVectorField::typeName).size();
label N_ssf = objects.sortedNames(surfaceVectorField::typeName).size();

List<autoPtr<volVectorField>> vsf_list(N_vsf);
List<autoPtr<surfaceVectorField>> ssf_list(N_ssf);

// adding volVectorFields to the list
for(label i = 0; i < N_vsf; i++)
{
    // getting field name
    word fieldName = objects.sortedNames(volVectorField::typeName)[i];
    // adding volVectorField to the list
    vsf_list[i].reset
    (
        new volVectorField
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

// adding surfaceVectorFields to the list
for(label i = 0; i < N_ssf; i++)
{
    // getting field name
    word fieldName = objects.sortedNames(surfaceVectorField::typeName)[i];
    // adding surfaceVectorField to the list
    ssf_list[i].reset
    (
        new surfaceVectorField
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
filePtr.reset(new OFstream(timeDirectory/"boundaryVectorFields.csv"));

// writing headers to the csv file
filePtr() << "patchName,X,Y,Z";

for(const word& fieldName : objects.sortedNames(volVectorField::typeName))
    filePtr() << "," << fieldName << "_x" << ","
                     << fieldName << "_y" << ","
                     << fieldName << "_z" ;

for(const word& fieldName : objects.sortedNames(surfaceVectorField::typeName))
    filePtr() << "," << fieldName << "_x" << ","
                     << fieldName << "_y" << ","
                     << fieldName << "_z" ;
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
            filePtr() << "," << vsf_list[j][0].boundaryField()[patchI][i].x()
                      << "," << vsf_list[j][0].boundaryField()[patchI][i].y()
                      << "," << vsf_list[j][0].boundaryField()[patchI][i].z();

        // looping through surface fields
        for(label j = 0; j < N_ssf; j++)
            filePtr() << "," << ssf_list[j][0].boundaryField()[patchI][i]
                      << "," << ssf_list[j][0].boundaryField()[patchI][i].y()
                      << "," << ssf_list[j][0].boundaryField()[patchI][i].z();

        filePtr() << endl;
    }
}
