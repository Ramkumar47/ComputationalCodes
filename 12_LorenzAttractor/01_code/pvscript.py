"""----------------------------------------------------------------------------
ParaView programmable filter source code for postprocessing
----------------------------------------------------------------------------"""

import numpy as np
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

# reading data
fid = np.genfromtxt('solution_data/data.csv', names=True, delimiter=',',
                    dtype=None, autostrip=True)

# Compute the point coordinates for the helix.
x = fid['X']
y = fid['Y']
z = fid['Z']

scalar = np.sqrt(x**2 + y**2 + z**2)

# Create a (x,y,z) coordinates array and associate that with
# points to pass to the output dataset.
coordinates = algs.make_vector(x, y, z)
pts = vtk.vtkPoints()
pts.SetData(dsa.numpyTovtkDataArray(coordinates, 'Points'))
output.SetPoints(pts)
numPts = pts.GetNumberOfPoints()
# Add scalars to the output point data.
output.PointData.append(scalar, 'scalar')

# Next, we need to define the topology i.e.
# cell information. This helix will be a single
# polyline connecting all the  points in order.
ptIds = vtk.vtkIdList()
ptIds.SetNumberOfIds(numPts)
for i in range(numPts):
   #Add the points to the line. The first value indicates
   #the order of the point on the line. The second value
   #is a reference to a point in a vtkPoints object. Depends
   #on the order that Points were added to vtkPoints object.
   #Note that this will not be associated with actual points
   #until it is added to a vtkPolyData object which holds a
   #vtkPoints object.
   ptIds.SetId(i, i)

# Allocate the number of 'cells' that will be added. We are just
# adding one vtkPolyLine 'cell' to the vtkPolyData object.
output.Allocate(1, 1)

# Add the poly line 'cell' to the vtkPolyData object.
output.InsertNextCell(vtk.VTK_POLY_LINE, ptIds)
