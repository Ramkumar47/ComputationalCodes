/*
 * writing volScalarFields to the csv file
 */

Info << tab << " writing volScalarFields.csv : " << objects.sortedNames(volScalarField::typeName) << endl;

// preparing lists for volScalarFields and its filenames
label N_vsf = objects.sortedNames(volScalarField::typeName).size();
List<autoPtr<volScalarField>> vsf_list(N_vsf);
wordList vsf_names(N_vsf);

// adding volScalarFields to the list
for(label i = 0; i < N_vsf; i++)
{
    // getting field name
    word fieldName = objects.sortedNames(volScalarField::typeName)[i];

    // adding field name to the list
    vsf_names[i] = fieldName;

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

// initializing csv file path
filePtr.reset(new OFstream(timeDirectory/"volScalarFields.csv"));

// writing headers to the csv file
filePtr() << "X,Y,Z";

for(const word& fieldName : objects.sortedNames(volScalarField::typeName))
    filePtr() << "," << fieldName;
filePtr() << endl;

// writing field values to file
forAll(mesh.C(), cellid)
{
    filePtr() << mesh.C()[cellid].x() << ","
                  << mesh.C()[cellid].y() << ","
                  << mesh.C()[cellid].z();
    // looping through fields
    for(label i = 0; i < N_vsf; i++)
        filePtr() << "," << vsf_list[i][0][cellid];
    filePtr() << endl;
}
