/*
 * writing surfaceVectorFields to the csv file
 */

Info << tab << " writing surfaceVectorFields.csv : " << objects.sortedNames(surfaceVectorField::typeName) << endl;

// preparing lists for surfaceVectorFields and its filenames
label N_svf = objects.sortedNames(surfaceVectorField::typeName).size();
List<autoPtr<surfaceVectorField>> svf_list(N_svf);
wordList svf_names(N_svf);

// adding surfaceVectorFields to the list
for(label i = 0; i < N_svf; i++)
{
    // getting field name
    word fieldName = objects.sortedNames(surfaceVectorField::typeName)[i];

    // adding field name to the list
    svf_names[i] = fieldName;

    // adding surfaceVectorField to the list
    svf_list[i].reset
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
filePtr.reset(new OFstream(timeDirectory/"surfaceVectorFields.csv"));

// writing headers to the csv file
filePtr() << "X,Y,Z";

for(const word& fieldName : objects.sortedNames(surfaceVectorField::typeName))
    filePtr() << "," << fieldName << "_x" << "," << fieldName << "_y"
              << "," << fieldName << "_z";
filePtr() << endl;

// writing field values to file
forAll(mesh.C(), cellid)
{
    filePtr() << mesh.Cf()[cellid].x() << ","
                  << mesh.Cf()[cellid].y() << ","
                  << mesh.Cf()[cellid].z();
    // looping through fields
    for(label i = 0; i < N_svf; i++)
        filePtr() << "," << svf_list[i][0][cellid].x()
                  << "," << svf_list[i][0][cellid].y()
                  << "," << svf_list[i][0][cellid].z();
    filePtr() << endl;
}
