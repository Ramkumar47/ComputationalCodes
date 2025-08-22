# Code for plotting chaotic system trajectories
# reference https://docs.paraview.org/en/latest/ReferenceManual/pythonProgrammableFilter.html

import math
import numpy as np
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

data = np.genfromtxt("solutionData.csv", dtype=None, names=True, delimiter=',', autostrip=True)

coordinates = algs.make_vector(data["x"], data["y"], data["z"])

numPts=len(data["x"])

pts = vtk.vtkPoints()
pts.SetData(dsa.numpyTovtkDataArray(coordinates, 'Points'))
output.SetPoints(pts)

# Add scalars to the output point data.
output.PointData.append(data["time"], 'time')
output.PointData.append(data["L"], 'lyapunov')

ptIds = vtk.vtkIdList()
ptIds.SetNumberOfIds(numPts)
for i in range(numPts):
   ptIds.SetId(i, i)

output.Allocate(1, 1)

output.InsertNextCell(vtk.VTK_POLY_LINE, ptIds)
