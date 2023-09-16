# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
spreadSheetView1 = GetActiveViewOrCreate('SpreadSheetView')

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# get layout
layout1 = GetLayoutByName("Layout #1")

# close an empty frame
layout1.Collapse(2)

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# set active view
SetActiveView(renderView1)

# find source
datacsv = FindSource('data.csv')

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(registrationName='TableToPoints1', Input=datacsv)
tableToPoints1.XColumn = 'T'
tableToPoints1.YColumn = 'T'
tableToPoints1.ZColumn = 'T'
tableToPoints1.a2DPoints = 0
tableToPoints1.KeepAllDataArrays = 0

# Properties modified on tableToPoints1
tableToPoints1.XColumn = 'X'
tableToPoints1.YColumn = 'Y'
tableToPoints1.ZColumn = 'Z'

# show data in view
tableToPoints1Display = Show(tableToPoints1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tableToPoints1Display.Selection = None
tableToPoints1Display.Representation = 'Surface'
tableToPoints1Display.ColorArrayName = [None, '']
tableToPoints1Display.LookupTable = None
tableToPoints1Display.MapScalars = 1
tableToPoints1Display.MultiComponentsMapping = 0
tableToPoints1Display.InterpolateScalarsBeforeMapping = 1
tableToPoints1Display.Opacity = 1.0
tableToPoints1Display.PointSize = 2.0
tableToPoints1Display.LineWidth = 1.0
tableToPoints1Display.RenderLinesAsTubes = 0
tableToPoints1Display.RenderPointsAsSpheres = 0
tableToPoints1Display.Interpolation = 'Gouraud'
tableToPoints1Display.Specular = 0.0
tableToPoints1Display.SpecularColor = [1.0, 1.0, 1.0]
tableToPoints1Display.SpecularPower = 100.0
tableToPoints1Display.Luminosity = 0.0
tableToPoints1Display.Ambient = 0.0
tableToPoints1Display.Diffuse = 1.0
tableToPoints1Display.Roughness = 0.3
tableToPoints1Display.Metallic = 0.0
tableToPoints1Display.EdgeTint = [1.0, 1.0, 1.0]
tableToPoints1Display.Anisotropy = 0.0
tableToPoints1Display.AnisotropyRotation = 0.0
tableToPoints1Display.BaseIOR = 1.5
tableToPoints1Display.CoatStrength = 0.0
tableToPoints1Display.CoatIOR = 2.0
tableToPoints1Display.CoatRoughness = 0.0
tableToPoints1Display.CoatColor = [1.0, 1.0, 1.0]
tableToPoints1Display.SelectTCoordArray = 'None'
tableToPoints1Display.SelectNormalArray = 'None'
tableToPoints1Display.SelectTangentArray = 'None'
tableToPoints1Display.Texture = None
tableToPoints1Display.RepeatTextures = 1
tableToPoints1Display.InterpolateTextures = 0
tableToPoints1Display.SeamlessU = 0
tableToPoints1Display.SeamlessV = 0
tableToPoints1Display.UseMipmapTextures = 0
tableToPoints1Display.ShowTexturesOnBackface = 1
tableToPoints1Display.BaseColorTexture = None
tableToPoints1Display.NormalTexture = None
tableToPoints1Display.NormalScale = 1.0
tableToPoints1Display.CoatNormalTexture = None
tableToPoints1Display.CoatNormalScale = 1.0
tableToPoints1Display.MaterialTexture = None
tableToPoints1Display.OcclusionStrength = 1.0
tableToPoints1Display.AnisotropyTexture = None
tableToPoints1Display.EmissiveTexture = None
tableToPoints1Display.EmissiveFactor = [1.0, 1.0, 1.0]
tableToPoints1Display.FlipTextures = 0
tableToPoints1Display.BackfaceRepresentation = 'Follow Frontface'
tableToPoints1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
tableToPoints1Display.BackfaceOpacity = 1.0
tableToPoints1Display.Position = [0.0, 0.0, 0.0]
tableToPoints1Display.Scale = [1.0, 1.0, 1.0]
tableToPoints1Display.Orientation = [0.0, 0.0, 0.0]
tableToPoints1Display.Origin = [0.0, 0.0, 0.0]
tableToPoints1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
tableToPoints1Display.Pickable = 1
tableToPoints1Display.Triangulate = 0
tableToPoints1Display.UseShaderReplacements = 0
tableToPoints1Display.ShaderReplacements = ''
tableToPoints1Display.NonlinearSubdivisionLevel = 1
tableToPoints1Display.UseDataPartitions = 0
tableToPoints1Display.OSPRayUseScaleArray = 'All Approximate'
tableToPoints1Display.OSPRayScaleArray = 'T'
tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tableToPoints1Display.OSPRayMaterial = 'None'
tableToPoints1Display.BlockSelectors = ['/']
tableToPoints1Display.BlockColors = []
tableToPoints1Display.BlockOpacities = []
tableToPoints1Display.Orient = 0
tableToPoints1Display.OrientationMode = 'Direction'
tableToPoints1Display.SelectOrientationVectors = 'None'
tableToPoints1Display.Scaling = 0
tableToPoints1Display.ScaleMode = 'No Data Scaling Off'
tableToPoints1Display.ScaleFactor = 1.0000000000000002e-06
tableToPoints1Display.SelectScaleArray = 'None'
tableToPoints1Display.GlyphType = 'Arrow'
tableToPoints1Display.UseGlyphTable = 0
tableToPoints1Display.GlyphTableIndexArray = 'None'
tableToPoints1Display.UseCompositeGlyphTable = 0
tableToPoints1Display.UseGlyphCullingAndLOD = 0
tableToPoints1Display.LODValues = []
tableToPoints1Display.ColorByLODIndex = 0
tableToPoints1Display.GaussianRadius = 5.0000000000000004e-08
tableToPoints1Display.ShaderPreset = 'Sphere'
tableToPoints1Display.CustomTriangleScale = 3
tableToPoints1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
tableToPoints1Display.Emissive = 0
tableToPoints1Display.ScaleByArray = 0
tableToPoints1Display.SetScaleArray = ['POINTS', 'T']
tableToPoints1Display.ScaleArrayComponent = ''
tableToPoints1Display.UseScaleFunction = 1
tableToPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.OpacityByArray = 0
tableToPoints1Display.OpacityArray = ['POINTS', 'T']
tableToPoints1Display.OpacityArrayComponent = ''
tableToPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
tableToPoints1Display.SelectionCellLabelBold = 0
tableToPoints1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
tableToPoints1Display.SelectionCellLabelFontFamily = 'Arial'
tableToPoints1Display.SelectionCellLabelFontFile = ''
tableToPoints1Display.SelectionCellLabelFontSize = 18
tableToPoints1Display.SelectionCellLabelItalic = 0
tableToPoints1Display.SelectionCellLabelJustification = 'Left'
tableToPoints1Display.SelectionCellLabelOpacity = 1.0
tableToPoints1Display.SelectionCellLabelShadow = 0
tableToPoints1Display.SelectionPointLabelBold = 0
tableToPoints1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
tableToPoints1Display.SelectionPointLabelFontFamily = 'Arial'
tableToPoints1Display.SelectionPointLabelFontFile = ''
tableToPoints1Display.SelectionPointLabelFontSize = 18
tableToPoints1Display.SelectionPointLabelItalic = 0
tableToPoints1Display.SelectionPointLabelJustification = 'Left'
tableToPoints1Display.SelectionPointLabelOpacity = 1.0
tableToPoints1Display.SelectionPointLabelShadow = 0
tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tableToPoints1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
tableToPoints1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
tableToPoints1Display.GlyphType.TipResolution = 6
tableToPoints1Display.GlyphType.TipRadius = 0.1
tableToPoints1Display.GlyphType.TipLength = 0.35
tableToPoints1Display.GlyphType.ShaftResolution = 6
tableToPoints1Display.GlyphType.ShaftRadius = 0.03
tableToPoints1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tableToPoints1Display.ScaleTransferFunction.Points = [288.16, 0.0, 0.5, 0.0, 573.51996, 1.0, 0.5, 0.0]
tableToPoints1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tableToPoints1Display.OpacityTransferFunction.Points = [288.16, 0.0, 0.5, 0.0, 573.51996, 1.0, 0.5, 0.0]
tableToPoints1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tableToPoints1Display.DataAxesGrid.XTitle = 'X Axis'
tableToPoints1Display.DataAxesGrid.YTitle = 'Y Axis'
tableToPoints1Display.DataAxesGrid.ZTitle = 'Z Axis'
tableToPoints1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.XTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.XTitleBold = 0
tableToPoints1Display.DataAxesGrid.XTitleItalic = 0
tableToPoints1Display.DataAxesGrid.XTitleFontSize = 12
tableToPoints1Display.DataAxesGrid.XTitleShadow = 0
tableToPoints1Display.DataAxesGrid.XTitleOpacity = 1.0
tableToPoints1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.YTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.YTitleBold = 0
tableToPoints1Display.DataAxesGrid.YTitleItalic = 0
tableToPoints1Display.DataAxesGrid.YTitleFontSize = 12
tableToPoints1Display.DataAxesGrid.YTitleShadow = 0
tableToPoints1Display.DataAxesGrid.YTitleOpacity = 1.0
tableToPoints1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.ZTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.ZTitleBold = 0
tableToPoints1Display.DataAxesGrid.ZTitleItalic = 0
tableToPoints1Display.DataAxesGrid.ZTitleFontSize = 12
tableToPoints1Display.DataAxesGrid.ZTitleShadow = 0
tableToPoints1Display.DataAxesGrid.ZTitleOpacity = 1.0
tableToPoints1Display.DataAxesGrid.FacesToRender = 63
tableToPoints1Display.DataAxesGrid.CullBackface = 0
tableToPoints1Display.DataAxesGrid.CullFrontface = 1
tableToPoints1Display.DataAxesGrid.ShowGrid = 0
tableToPoints1Display.DataAxesGrid.ShowEdges = 1
tableToPoints1Display.DataAxesGrid.ShowTicks = 1
tableToPoints1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
tableToPoints1Display.DataAxesGrid.AxesToLabel = 63
tableToPoints1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.XLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.XLabelBold = 0
tableToPoints1Display.DataAxesGrid.XLabelItalic = 0
tableToPoints1Display.DataAxesGrid.XLabelFontSize = 12
tableToPoints1Display.DataAxesGrid.XLabelShadow = 0
tableToPoints1Display.DataAxesGrid.XLabelOpacity = 1.0
tableToPoints1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.YLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.YLabelBold = 0
tableToPoints1Display.DataAxesGrid.YLabelItalic = 0
tableToPoints1Display.DataAxesGrid.YLabelFontSize = 12
tableToPoints1Display.DataAxesGrid.YLabelShadow = 0
tableToPoints1Display.DataAxesGrid.YLabelOpacity = 1.0
tableToPoints1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.ZLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.ZLabelBold = 0
tableToPoints1Display.DataAxesGrid.ZLabelItalic = 0
tableToPoints1Display.DataAxesGrid.ZLabelFontSize = 12
tableToPoints1Display.DataAxesGrid.ZLabelShadow = 0
tableToPoints1Display.DataAxesGrid.ZLabelOpacity = 1.0
tableToPoints1Display.DataAxesGrid.XAxisNotation = 'Mixed'
tableToPoints1Display.DataAxesGrid.XAxisPrecision = 2
tableToPoints1Display.DataAxesGrid.XAxisUseCustomLabels = 0
tableToPoints1Display.DataAxesGrid.XAxisLabels = []
tableToPoints1Display.DataAxesGrid.YAxisNotation = 'Mixed'
tableToPoints1Display.DataAxesGrid.YAxisPrecision = 2
tableToPoints1Display.DataAxesGrid.YAxisUseCustomLabels = 0
tableToPoints1Display.DataAxesGrid.YAxisLabels = []
tableToPoints1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
tableToPoints1Display.DataAxesGrid.ZAxisPrecision = 2
tableToPoints1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
tableToPoints1Display.DataAxesGrid.ZAxisLabels = []
tableToPoints1Display.DataAxesGrid.UseCustomBounds = 0
tableToPoints1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tableToPoints1Display.PolarAxes.Visibility = 0
tableToPoints1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
tableToPoints1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
tableToPoints1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
tableToPoints1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
tableToPoints1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
tableToPoints1Display.PolarAxes.EnableCustomRange = 0
tableToPoints1Display.PolarAxes.CustomRange = [0.0, 1.0]
tableToPoints1Display.PolarAxes.PolarAxisVisibility = 1
tableToPoints1Display.PolarAxes.RadialAxesVisibility = 1
tableToPoints1Display.PolarAxes.DrawRadialGridlines = 1
tableToPoints1Display.PolarAxes.PolarArcsVisibility = 1
tableToPoints1Display.PolarAxes.DrawPolarArcsGridlines = 1
tableToPoints1Display.PolarAxes.NumberOfRadialAxes = 0
tableToPoints1Display.PolarAxes.AutoSubdividePolarAxis = 1
tableToPoints1Display.PolarAxes.NumberOfPolarAxis = 0
tableToPoints1Display.PolarAxes.MinimumRadius = 0.0
tableToPoints1Display.PolarAxes.MinimumAngle = 0.0
tableToPoints1Display.PolarAxes.MaximumAngle = 90.0
tableToPoints1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
tableToPoints1Display.PolarAxes.Ratio = 1.0
tableToPoints1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
tableToPoints1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
tableToPoints1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
tableToPoints1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
tableToPoints1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
tableToPoints1Display.PolarAxes.PolarAxisTitleVisibility = 1
tableToPoints1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
tableToPoints1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
tableToPoints1Display.PolarAxes.PolarLabelVisibility = 1
tableToPoints1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
tableToPoints1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
tableToPoints1Display.PolarAxes.RadialLabelVisibility = 1
tableToPoints1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
tableToPoints1Display.PolarAxes.RadialLabelLocation = 'Bottom'
tableToPoints1Display.PolarAxes.RadialUnitsVisibility = 1
tableToPoints1Display.PolarAxes.ScreenSize = 10.0
tableToPoints1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
tableToPoints1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
tableToPoints1Display.PolarAxes.PolarAxisTitleFontFile = ''
tableToPoints1Display.PolarAxes.PolarAxisTitleBold = 0
tableToPoints1Display.PolarAxes.PolarAxisTitleItalic = 0
tableToPoints1Display.PolarAxes.PolarAxisTitleShadow = 0
tableToPoints1Display.PolarAxes.PolarAxisTitleFontSize = 12
tableToPoints1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
tableToPoints1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
tableToPoints1Display.PolarAxes.PolarAxisLabelFontFile = ''
tableToPoints1Display.PolarAxes.PolarAxisLabelBold = 0
tableToPoints1Display.PolarAxes.PolarAxisLabelItalic = 0
tableToPoints1Display.PolarAxes.PolarAxisLabelShadow = 0
tableToPoints1Display.PolarAxes.PolarAxisLabelFontSize = 12
tableToPoints1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
tableToPoints1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
tableToPoints1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tableToPoints1Display.PolarAxes.LastRadialAxisTextBold = 0
tableToPoints1Display.PolarAxes.LastRadialAxisTextItalic = 0
tableToPoints1Display.PolarAxes.LastRadialAxisTextShadow = 0
tableToPoints1Display.PolarAxes.LastRadialAxisTextFontSize = 12
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
tableToPoints1Display.PolarAxes.EnableDistanceLOD = 1
tableToPoints1Display.PolarAxes.DistanceLODThreshold = 0.7
tableToPoints1Display.PolarAxes.EnableViewAngleLOD = 1
tableToPoints1Display.PolarAxes.ViewAngleLODThreshold = 0.7
tableToPoints1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
tableToPoints1Display.PolarAxes.PolarTicksVisibility = 1
tableToPoints1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
tableToPoints1Display.PolarAxes.TickLocation = 'Both'
tableToPoints1Display.PolarAxes.AxisTickVisibility = 1
tableToPoints1Display.PolarAxes.AxisMinorTickVisibility = 0
tableToPoints1Display.PolarAxes.ArcTickVisibility = 1
tableToPoints1Display.PolarAxes.ArcMinorTickVisibility = 0
tableToPoints1Display.PolarAxes.DeltaAngleMajor = 10.0
tableToPoints1Display.PolarAxes.DeltaAngleMinor = 5.0
tableToPoints1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
tableToPoints1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
tableToPoints1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
tableToPoints1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
tableToPoints1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
tableToPoints1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
tableToPoints1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
tableToPoints1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
tableToPoints1Display.PolarAxes.ArcMajorTickSize = 0.0
tableToPoints1Display.PolarAxes.ArcTickRatioSize = 0.3
tableToPoints1Display.PolarAxes.ArcMajorTickThickness = 1.0
tableToPoints1Display.PolarAxes.ArcTickRatioThickness = 0.5
tableToPoints1Display.PolarAxes.Use2DMode = 0
tableToPoints1Display.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera(False)

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [5e-06, 3.95285e-06, 10000.0]
renderView1.CameraFocalPoint = [5e-06, 3.95285e-06, 0.0]

# update the view to ensure updated data information
renderView1.Update()

#change interaction mode for render view
renderView1.InteractionMode = '3D'

# reset view to fit data
renderView1.ResetCamera(False)

# create a new 'Delaunay 2D'
delaunay2D1 = Delaunay2D(registrationName='Delaunay2D1', Input=tableToPoints1)
delaunay2D1.ProjectionPlaneMode = 'XY Plane'
delaunay2D1.Alpha = 0.0
delaunay2D1.Tolerance = 1e-05
delaunay2D1.Offset = 1.0
delaunay2D1.BoundingTriangulation = 0

# show data in view
delaunay2D1Display = Show(delaunay2D1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
delaunay2D1Display.Selection = None
delaunay2D1Display.Representation = 'Surface'
delaunay2D1Display.ColorArrayName = [None, '']
delaunay2D1Display.LookupTable = None
delaunay2D1Display.MapScalars = 1
delaunay2D1Display.MultiComponentsMapping = 0
delaunay2D1Display.InterpolateScalarsBeforeMapping = 1
delaunay2D1Display.Opacity = 1.0
delaunay2D1Display.PointSize = 2.0
delaunay2D1Display.LineWidth = 1.0
delaunay2D1Display.RenderLinesAsTubes = 0
delaunay2D1Display.RenderPointsAsSpheres = 0
delaunay2D1Display.Interpolation = 'Gouraud'
delaunay2D1Display.Specular = 0.0
delaunay2D1Display.SpecularColor = [1.0, 1.0, 1.0]
delaunay2D1Display.SpecularPower = 100.0
delaunay2D1Display.Luminosity = 0.0
delaunay2D1Display.Ambient = 0.0
delaunay2D1Display.Diffuse = 1.0
delaunay2D1Display.Roughness = 0.3
delaunay2D1Display.Metallic = 0.0
delaunay2D1Display.EdgeTint = [1.0, 1.0, 1.0]
delaunay2D1Display.Anisotropy = 0.0
delaunay2D1Display.AnisotropyRotation = 0.0
delaunay2D1Display.BaseIOR = 1.5
delaunay2D1Display.CoatStrength = 0.0
delaunay2D1Display.CoatIOR = 2.0
delaunay2D1Display.CoatRoughness = 0.0
delaunay2D1Display.CoatColor = [1.0, 1.0, 1.0]
delaunay2D1Display.SelectTCoordArray = 'None'
delaunay2D1Display.SelectNormalArray = 'None'
delaunay2D1Display.SelectTangentArray = 'None'
delaunay2D1Display.Texture = None
delaunay2D1Display.RepeatTextures = 1
delaunay2D1Display.InterpolateTextures = 0
delaunay2D1Display.SeamlessU = 0
delaunay2D1Display.SeamlessV = 0
delaunay2D1Display.UseMipmapTextures = 0
delaunay2D1Display.ShowTexturesOnBackface = 1
delaunay2D1Display.BaseColorTexture = None
delaunay2D1Display.NormalTexture = None
delaunay2D1Display.NormalScale = 1.0
delaunay2D1Display.CoatNormalTexture = None
delaunay2D1Display.CoatNormalScale = 1.0
delaunay2D1Display.MaterialTexture = None
delaunay2D1Display.OcclusionStrength = 1.0
delaunay2D1Display.AnisotropyTexture = None
delaunay2D1Display.EmissiveTexture = None
delaunay2D1Display.EmissiveFactor = [1.0, 1.0, 1.0]
delaunay2D1Display.FlipTextures = 0
delaunay2D1Display.BackfaceRepresentation = 'Follow Frontface'
delaunay2D1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
delaunay2D1Display.BackfaceOpacity = 1.0
delaunay2D1Display.Position = [0.0, 0.0, 0.0]
delaunay2D1Display.Scale = [1.0, 1.0, 1.0]
delaunay2D1Display.Orientation = [0.0, 0.0, 0.0]
delaunay2D1Display.Origin = [0.0, 0.0, 0.0]
delaunay2D1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
delaunay2D1Display.Pickable = 1
delaunay2D1Display.Triangulate = 0
delaunay2D1Display.UseShaderReplacements = 0
delaunay2D1Display.ShaderReplacements = ''
delaunay2D1Display.NonlinearSubdivisionLevel = 1
delaunay2D1Display.UseDataPartitions = 0
delaunay2D1Display.OSPRayUseScaleArray = 'All Approximate'
delaunay2D1Display.OSPRayScaleArray = 'T'
delaunay2D1Display.OSPRayScaleFunction = 'PiecewiseFunction'
delaunay2D1Display.OSPRayMaterial = 'None'
delaunay2D1Display.BlockSelectors = ['/']
delaunay2D1Display.BlockColors = []
delaunay2D1Display.BlockOpacities = []
delaunay2D1Display.Orient = 0
delaunay2D1Display.OrientationMode = 'Direction'
delaunay2D1Display.SelectOrientationVectors = 'None'
delaunay2D1Display.Scaling = 0
delaunay2D1Display.ScaleMode = 'No Data Scaling Off'
delaunay2D1Display.ScaleFactor = 1.0000000000000002e-06
delaunay2D1Display.SelectScaleArray = 'None'
delaunay2D1Display.GlyphType = 'Arrow'
delaunay2D1Display.UseGlyphTable = 0
delaunay2D1Display.GlyphTableIndexArray = 'None'
delaunay2D1Display.UseCompositeGlyphTable = 0
delaunay2D1Display.UseGlyphCullingAndLOD = 0
delaunay2D1Display.LODValues = []
delaunay2D1Display.ColorByLODIndex = 0
delaunay2D1Display.GaussianRadius = 5.0000000000000004e-08
delaunay2D1Display.ShaderPreset = 'Sphere'
delaunay2D1Display.CustomTriangleScale = 3
delaunay2D1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
delaunay2D1Display.Emissive = 0
delaunay2D1Display.ScaleByArray = 0
delaunay2D1Display.SetScaleArray = ['POINTS', 'T']
delaunay2D1Display.ScaleArrayComponent = ''
delaunay2D1Display.UseScaleFunction = 1
delaunay2D1Display.ScaleTransferFunction = 'PiecewiseFunction'
delaunay2D1Display.OpacityByArray = 0
delaunay2D1Display.OpacityArray = ['POINTS', 'T']
delaunay2D1Display.OpacityArrayComponent = ''
delaunay2D1Display.OpacityTransferFunction = 'PiecewiseFunction'
delaunay2D1Display.DataAxesGrid = 'GridAxesRepresentation'
delaunay2D1Display.SelectionCellLabelBold = 0
delaunay2D1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
delaunay2D1Display.SelectionCellLabelFontFamily = 'Arial'
delaunay2D1Display.SelectionCellLabelFontFile = ''
delaunay2D1Display.SelectionCellLabelFontSize = 18
delaunay2D1Display.SelectionCellLabelItalic = 0
delaunay2D1Display.SelectionCellLabelJustification = 'Left'
delaunay2D1Display.SelectionCellLabelOpacity = 1.0
delaunay2D1Display.SelectionCellLabelShadow = 0
delaunay2D1Display.SelectionPointLabelBold = 0
delaunay2D1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
delaunay2D1Display.SelectionPointLabelFontFamily = 'Arial'
delaunay2D1Display.SelectionPointLabelFontFile = ''
delaunay2D1Display.SelectionPointLabelFontSize = 18
delaunay2D1Display.SelectionPointLabelItalic = 0
delaunay2D1Display.SelectionPointLabelJustification = 'Left'
delaunay2D1Display.SelectionPointLabelOpacity = 1.0
delaunay2D1Display.SelectionPointLabelShadow = 0
delaunay2D1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
delaunay2D1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
delaunay2D1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
delaunay2D1Display.GlyphType.TipResolution = 6
delaunay2D1Display.GlyphType.TipRadius = 0.1
delaunay2D1Display.GlyphType.TipLength = 0.35
delaunay2D1Display.GlyphType.ShaftResolution = 6
delaunay2D1Display.GlyphType.ShaftRadius = 0.03
delaunay2D1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
delaunay2D1Display.ScaleTransferFunction.Points = [288.16, 0.0, 0.5, 0.0, 573.51996, 1.0, 0.5, 0.0]
delaunay2D1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
delaunay2D1Display.OpacityTransferFunction.Points = [288.16, 0.0, 0.5, 0.0, 573.51996, 1.0, 0.5, 0.0]
delaunay2D1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
delaunay2D1Display.DataAxesGrid.XTitle = 'X Axis'
delaunay2D1Display.DataAxesGrid.YTitle = 'Y Axis'
delaunay2D1Display.DataAxesGrid.ZTitle = 'Z Axis'
delaunay2D1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
delaunay2D1Display.DataAxesGrid.XTitleFontFile = ''
delaunay2D1Display.DataAxesGrid.XTitleBold = 0
delaunay2D1Display.DataAxesGrid.XTitleItalic = 0
delaunay2D1Display.DataAxesGrid.XTitleFontSize = 12
delaunay2D1Display.DataAxesGrid.XTitleShadow = 0
delaunay2D1Display.DataAxesGrid.XTitleOpacity = 1.0
delaunay2D1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
delaunay2D1Display.DataAxesGrid.YTitleFontFile = ''
delaunay2D1Display.DataAxesGrid.YTitleBold = 0
delaunay2D1Display.DataAxesGrid.YTitleItalic = 0
delaunay2D1Display.DataAxesGrid.YTitleFontSize = 12
delaunay2D1Display.DataAxesGrid.YTitleShadow = 0
delaunay2D1Display.DataAxesGrid.YTitleOpacity = 1.0
delaunay2D1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
delaunay2D1Display.DataAxesGrid.ZTitleFontFile = ''
delaunay2D1Display.DataAxesGrid.ZTitleBold = 0
delaunay2D1Display.DataAxesGrid.ZTitleItalic = 0
delaunay2D1Display.DataAxesGrid.ZTitleFontSize = 12
delaunay2D1Display.DataAxesGrid.ZTitleShadow = 0
delaunay2D1Display.DataAxesGrid.ZTitleOpacity = 1.0
delaunay2D1Display.DataAxesGrid.FacesToRender = 63
delaunay2D1Display.DataAxesGrid.CullBackface = 0
delaunay2D1Display.DataAxesGrid.CullFrontface = 1
delaunay2D1Display.DataAxesGrid.ShowGrid = 0
delaunay2D1Display.DataAxesGrid.ShowEdges = 1
delaunay2D1Display.DataAxesGrid.ShowTicks = 1
delaunay2D1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
delaunay2D1Display.DataAxesGrid.AxesToLabel = 63
delaunay2D1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
delaunay2D1Display.DataAxesGrid.XLabelFontFile = ''
delaunay2D1Display.DataAxesGrid.XLabelBold = 0
delaunay2D1Display.DataAxesGrid.XLabelItalic = 0
delaunay2D1Display.DataAxesGrid.XLabelFontSize = 12
delaunay2D1Display.DataAxesGrid.XLabelShadow = 0
delaunay2D1Display.DataAxesGrid.XLabelOpacity = 1.0
delaunay2D1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
delaunay2D1Display.DataAxesGrid.YLabelFontFile = ''
delaunay2D1Display.DataAxesGrid.YLabelBold = 0
delaunay2D1Display.DataAxesGrid.YLabelItalic = 0
delaunay2D1Display.DataAxesGrid.YLabelFontSize = 12
delaunay2D1Display.DataAxesGrid.YLabelShadow = 0
delaunay2D1Display.DataAxesGrid.YLabelOpacity = 1.0
delaunay2D1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
delaunay2D1Display.DataAxesGrid.ZLabelFontFile = ''
delaunay2D1Display.DataAxesGrid.ZLabelBold = 0
delaunay2D1Display.DataAxesGrid.ZLabelItalic = 0
delaunay2D1Display.DataAxesGrid.ZLabelFontSize = 12
delaunay2D1Display.DataAxesGrid.ZLabelShadow = 0
delaunay2D1Display.DataAxesGrid.ZLabelOpacity = 1.0
delaunay2D1Display.DataAxesGrid.XAxisNotation = 'Mixed'
delaunay2D1Display.DataAxesGrid.XAxisPrecision = 2
delaunay2D1Display.DataAxesGrid.XAxisUseCustomLabels = 0
delaunay2D1Display.DataAxesGrid.XAxisLabels = []
delaunay2D1Display.DataAxesGrid.YAxisNotation = 'Mixed'
delaunay2D1Display.DataAxesGrid.YAxisPrecision = 2
delaunay2D1Display.DataAxesGrid.YAxisUseCustomLabels = 0
delaunay2D1Display.DataAxesGrid.YAxisLabels = []
delaunay2D1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
delaunay2D1Display.DataAxesGrid.ZAxisPrecision = 2
delaunay2D1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
delaunay2D1Display.DataAxesGrid.ZAxisLabels = []
delaunay2D1Display.DataAxesGrid.UseCustomBounds = 0
delaunay2D1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
delaunay2D1Display.PolarAxes.Visibility = 0
delaunay2D1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
delaunay2D1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
delaunay2D1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
delaunay2D1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
delaunay2D1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
delaunay2D1Display.PolarAxes.EnableCustomRange = 0
delaunay2D1Display.PolarAxes.CustomRange = [0.0, 1.0]
delaunay2D1Display.PolarAxes.PolarAxisVisibility = 1
delaunay2D1Display.PolarAxes.RadialAxesVisibility = 1
delaunay2D1Display.PolarAxes.DrawRadialGridlines = 1
delaunay2D1Display.PolarAxes.PolarArcsVisibility = 1
delaunay2D1Display.PolarAxes.DrawPolarArcsGridlines = 1
delaunay2D1Display.PolarAxes.NumberOfRadialAxes = 0
delaunay2D1Display.PolarAxes.AutoSubdividePolarAxis = 1
delaunay2D1Display.PolarAxes.NumberOfPolarAxis = 0
delaunay2D1Display.PolarAxes.MinimumRadius = 0.0
delaunay2D1Display.PolarAxes.MinimumAngle = 0.0
delaunay2D1Display.PolarAxes.MaximumAngle = 90.0
delaunay2D1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
delaunay2D1Display.PolarAxes.Ratio = 1.0
delaunay2D1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
delaunay2D1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
delaunay2D1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
delaunay2D1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
delaunay2D1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
delaunay2D1Display.PolarAxes.PolarAxisTitleVisibility = 1
delaunay2D1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
delaunay2D1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
delaunay2D1Display.PolarAxes.PolarLabelVisibility = 1
delaunay2D1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
delaunay2D1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
delaunay2D1Display.PolarAxes.RadialLabelVisibility = 1
delaunay2D1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
delaunay2D1Display.PolarAxes.RadialLabelLocation = 'Bottom'
delaunay2D1Display.PolarAxes.RadialUnitsVisibility = 1
delaunay2D1Display.PolarAxes.ScreenSize = 10.0
delaunay2D1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
delaunay2D1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
delaunay2D1Display.PolarAxes.PolarAxisTitleFontFile = ''
delaunay2D1Display.PolarAxes.PolarAxisTitleBold = 0
delaunay2D1Display.PolarAxes.PolarAxisTitleItalic = 0
delaunay2D1Display.PolarAxes.PolarAxisTitleShadow = 0
delaunay2D1Display.PolarAxes.PolarAxisTitleFontSize = 12
delaunay2D1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
delaunay2D1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
delaunay2D1Display.PolarAxes.PolarAxisLabelFontFile = ''
delaunay2D1Display.PolarAxes.PolarAxisLabelBold = 0
delaunay2D1Display.PolarAxes.PolarAxisLabelItalic = 0
delaunay2D1Display.PolarAxes.PolarAxisLabelShadow = 0
delaunay2D1Display.PolarAxes.PolarAxisLabelFontSize = 12
delaunay2D1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
delaunay2D1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
delaunay2D1Display.PolarAxes.LastRadialAxisTextFontFile = ''
delaunay2D1Display.PolarAxes.LastRadialAxisTextBold = 0
delaunay2D1Display.PolarAxes.LastRadialAxisTextItalic = 0
delaunay2D1Display.PolarAxes.LastRadialAxisTextShadow = 0
delaunay2D1Display.PolarAxes.LastRadialAxisTextFontSize = 12
delaunay2D1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
delaunay2D1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
delaunay2D1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
delaunay2D1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
delaunay2D1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
delaunay2D1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
delaunay2D1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
delaunay2D1Display.PolarAxes.EnableDistanceLOD = 1
delaunay2D1Display.PolarAxes.DistanceLODThreshold = 0.7
delaunay2D1Display.PolarAxes.EnableViewAngleLOD = 1
delaunay2D1Display.PolarAxes.ViewAngleLODThreshold = 0.7
delaunay2D1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
delaunay2D1Display.PolarAxes.PolarTicksVisibility = 1
delaunay2D1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
delaunay2D1Display.PolarAxes.TickLocation = 'Both'
delaunay2D1Display.PolarAxes.AxisTickVisibility = 1
delaunay2D1Display.PolarAxes.AxisMinorTickVisibility = 0
delaunay2D1Display.PolarAxes.ArcTickVisibility = 1
delaunay2D1Display.PolarAxes.ArcMinorTickVisibility = 0
delaunay2D1Display.PolarAxes.DeltaAngleMajor = 10.0
delaunay2D1Display.PolarAxes.DeltaAngleMinor = 5.0
delaunay2D1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
delaunay2D1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
delaunay2D1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
delaunay2D1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
delaunay2D1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
delaunay2D1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
delaunay2D1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
delaunay2D1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
delaunay2D1Display.PolarAxes.ArcMajorTickSize = 0.0
delaunay2D1Display.PolarAxes.ArcTickRatioSize = 0.3
delaunay2D1Display.PolarAxes.ArcMajorTickThickness = 1.0
delaunay2D1Display.PolarAxes.ArcTickRatioThickness = 0.5
delaunay2D1Display.PolarAxes.Use2DMode = 0
delaunay2D1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(tableToPoints1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(delaunay2D1Display, ('POINTS', 'T'))

# rescale color and/or opacity maps used to include current data range
delaunay2D1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
delaunay2D1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1556, 790)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [5e-06, 3.95285e-06, 2.4626380192941915e-05]
renderView1.CameraFocalPoint = [5e-06, 3.95285e-06, 0.0]
renderView1.CameraParallelScale = 6.3737762058688574e-06

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).