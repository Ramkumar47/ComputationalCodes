this is a custom application that will write the OpenFOAM solution field values into csv files

compilation instructions:
1) go into the source code directory using terminal.
2) initialize OpenFOAM environment and give the command "wclean && wmake"
3) if no error in red block text is showm, then compilation is successful
4) to test the compilation, give the command "foamToCSV -help" it should be executed without any error.

execution instructions:
1. go into the simulation case directory that has some saved solution files
2. execute the command "foamToCSV" (to get csv for all available timesteps) or "foamToCSV -latestTime" (to get csv for only latest timestep)
3. program will execute and a new folder named "CSV" will be created in the case directory, inside which the csv files are placed inside each timestep subfolders.

general instructions:
In OpenFOAM computations, generally the output solution fields can be classified into one of the 4 types below
-	surfaceScalarField
-	surfaceVectorField
-	volScalarField
-	volVectorField

hence the code is made such that for each solution timestep, there will be a max of 6 csv files made (4 above types and 2 additional for boundary fields)
not all simulation cases will have its solution fields under all 4 categories. hence only the field types that are available, will be writen into csv files.
the names of csv files are
-	surfaceScalarFields.csv			these will have internal volume/surface scalar/vector field values.
-	surfaceVectorFields.csv
-	volScalarFields.csv
-	volVectorFields.csv
-	boundaryScalarFields.csv		it will contain only the boundary surface scalar fields,
-	boundaryVectorFields.csv		it will contain only the boundary surface vector fields.
