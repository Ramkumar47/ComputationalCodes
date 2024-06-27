/*
 * writing volVectorFields to the csv file
 */

Info << tab << " writing volVectorFields.csv : " << objects.sortedNames(volVectorField::typeName) << endl;

// preparing lists for volVectorFields and its filenames
label N_vvf = objects.sortedNames(volVectorField::typeName).size();
List<autoPtr<volVectorField>> vvf_list(N_vvf);
wordList vvf_names(N_vvf);

// adding volVectorFields to the list
for(label i = 0; i < N_vvf; i++)
{
    // getting field name
    word fieldName = objects.sortedNames(volVectorField::typeName)[i];

    // adding field name to the list
    vvf_names[i] = fieldName;

    // adding volVectorField to the list
    vvf_list[i].reset
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

// initializing csv file path
filePtr.reset(new OFstream(timeDirectory/"volVectorFields.csv"));

// writing headers to the csv file
filePtr() << "X,Y,Z";

for(const word& fieldName : objects.sortedNames(volVectorField::typeName))
    filePtr() << "," << fieldName << "_x" << "," << fieldName << "_y"
              << "," << fieldName << "_z";
filePtr() << endl;

// writing field values to file
forAll(mesh.C(), cellid)
{
    filePtr() << mesh.C()[cellid].x() << ","
                  << mesh.C()[cellid].y() << ","
                  << mesh.C()[cellid].z();
    // looping through fields
    for(label i = 0; i < N_vvf; i++)
        filePtr() << "," << vvf_list[i][0][cellid].x()
                  << "," << vvf_list[i][0][cellid].y()
                  << "," << vvf_list[i][0][cellid].z();
    filePtr() << endl;
}
