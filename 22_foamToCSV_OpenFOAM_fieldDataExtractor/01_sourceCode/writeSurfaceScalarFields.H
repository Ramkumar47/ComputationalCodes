/*
 * writing surfaceScalarFields to the csv file
 */

Info << tab << " writing surfaceScalarFields.csv : " << objects.sortedNames(surfaceScalarField::typeName) << endl;

// preparing lists for surfaceScalarFields and its filenames
label N_ssf = objects.sortedNames(surfaceScalarField::typeName).size();
List<autoPtr<surfaceScalarField>> ssf_list(N_ssf);
wordList ssf_names(N_ssf);

// adding surfaceScalarFields to the list
for(label i = 0; i < N_ssf; i++)
{
    // getting field name
    word fieldName = objects.sortedNames(surfaceScalarField::typeName)[i];

    // adding field name to the list
    ssf_names[i] = fieldName;

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
filePtr.reset(new OFstream(timeDirectory/"surfaceScalarFields.csv"));

// writing headers to the csv file
filePtr() << "X,Y,Z";

for(const word& fieldName : objects.sortedNames(surfaceScalarField::typeName))
    filePtr() << "," << fieldName;
filePtr() << endl;

// writing field values to file
forAll(mesh.C(), cellid)
{
    filePtr() << mesh.Cf()[cellid].x() << ","
                  << mesh.Cf()[cellid].y() << ","
                  << mesh.Cf()[cellid].z();
    // looping through fields
    for(label i = 0; i < N_ssf; i++)
        filePtr() << "," << ssf_list[i][0][cellid];
    filePtr() << endl;
}
