from typing import Tuple, Set, Iterable, List

class GH_BezierGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ClearCaches (self) -> None: ...
    def GDI_GraphPath (self, reg : RectangleF) -> Set(PointF): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def Draw_PreRenderGrip (self, g : Graphics, cnt : GH_GraphContainer, index : int) -> GH_GraphDrawInstruction: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_ConicGraph(GH_AbstractGraph):
    def __init__(self): ...
    def GDI_GraphPath (self, reg : RectangleF) -> Set(PointF): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_GaussianGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_GripConstraint:
    none = 0
    horizontal = 1
    vertical = 2
class GH_GraphGrip:
    def __init__(self): ...
    def __init__(self, nX : float, nY : float): ...
    def __init__(self, nX : float, nY : float, nConstraint : GH_GripConstraint): ...
    def __init__(self, nOther : GH_GraphGrip): ...
    def add_GripChanged (self, obj : GripChangedEventHandler) -> None: ...
    def remove_GripChanged (self, obj : GripChangedEventHandler) -> None: ...
    def OnGripChanged (self, bIntermediate : bool) -> None: ...
    def SetIndex (self, nIndex : int) -> None: ...
    @property
    def Index (self) -> int: ...
    @property
    def X (self) -> float: ...
    @X.setter
    def X (self, Value : float) -> None: ...
    @property
    def Y (self) -> float: ...
    @Y.setter
    def Y (self, Value : float) -> None: ...
    @property
    def Point (self) -> PointF: ...
    def LimitToUnitDomain (self, bLimitX : bool, bLimitY : bool) -> None: ...
    @property
    def Constraint (self) -> GH_GripConstraint: ...
    @Constraint.setter
    def Constraint (self, Value : GH_GripConstraint) -> None: ...
    def op_Equality (A : GH_GraphGrip, B : GH_GraphGrip) -> bool: ...
    def op_Inequality (A : GH_GraphGrip, B : GH_GraphGrip) -> bool: ...
class GH_PerlinGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_PowerGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_ParabolaGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def Draw_PreRenderGraph (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_SquareRootGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def Draw_PreRenderGraph (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_SineEquation:
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    def SetEquationFromGrips (self) -> None: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_SineGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def GDI_GraphPath (self, reg : RectangleF) -> Set(PointF): ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_DoubleSineGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def ClearCaches (self) -> None: ...
    def GDI_GraphPath (self, reg : RectangleF) -> Set(PointF): ...
    def Draw_PreRenderGraph (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    def Draw_PreRenderGrip (self, g : Graphics, cnt : GH_GraphContainer, index : int) -> GH_GraphDrawInstruction: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_SincGraph(GH_AbstractGraph):
    def __init__(self): ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def GDI_GraphPath (self, reg : RectangleF) -> Set(PointF): ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_LinearGraph(GH_AbstractGraph):
    def __init__(self): ...
    def EmitProxyObject (self) -> IGH_GraphProxyObject: ...
    def SetFromParameters (self, nA : float, nB : float) -> None: ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def GDI_GraphPath (self, reg : RectangleF) -> Set(PointF): ...
    def Draw_PreRenderGraph (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_GraphDrawInstruction:
    none = 0
    skip = 1
class IGH_GraphProxyObject:
class GH_GraphProxyObject:
    def __init__(self, n_owner : IGH_Graph): ...
    @property
    def Name (self) -> str: ...
    @property
    def Description (self) -> str: ...
    @property
    def IsValid (self) -> bool: ...
class IGH_Graph:
    def add_GraphChanged (self, obj : GraphChangedEventHandler) -> None: ...
    def remove_GraphChanged (self, obj : GraphChangedEventHandler) -> None: ...
    def OnGraphChanged (self, bIntermediate : bool) -> None: ...
    def EmitProxyObject (self) -> IGH_GraphProxyObject: ...
    def Duplicate (self) -> IGH_Graph: ...
    def PrepareForUse (self) -> None: ...
    def ClearCaches (self) -> None: ...
    @property
    def Grips (self) -> List: ...
    @property
    def Name (self) -> str: ...
    @property
    def IsValid (self) -> bool: ...
    @property
    def Description (self) -> str: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    def ValueAt (self, t : float) -> float: ...
    def GDI_GraphPath (self, reg : RectangleF) -> Set(PointF): ...
    def Draw_PreRenderGrid (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    def Draw_PostRenderGrid (self, g : Graphics, cnt : GH_GraphContainer) -> None: ...
    def Draw_PreRenderGraph (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    def Draw_PostRenderGraph (self, g : Graphics, cnt : GH_GraphContainer) -> None: ...
    def Draw_PreRenderGrip (self, g : Graphics, cnt : GH_GraphContainer, index : int) -> GH_GraphDrawInstruction: ...
    def Draw_PostRenderGrip (self, g : Graphics, cnt : GH_GraphContainer, index : int) -> None: ...
    def Draw_PreRenderTags (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    def Draw_PostRenderTags (self, g : Graphics, cnt : GH_GraphContainer) -> None: ...
class GH_AbstractGraph:
    def Duplicate (self) -> IGH_Graph: ...
    def PrepareForUse (self) -> None: ...
    def EmitProxyObject (self) -> IGH_GraphProxyObject: ...
    def add_GraphChanged (self, obj : GraphChangedEventHandler) -> None: ...
    def remove_GraphChanged (self, obj : GraphChangedEventHandler) -> None: ...
    def OnGraphChanged (self, bIntermediate : bool) -> None: ...
    @property
    def Name (self) -> str: ...
    @property
    def Description (self) -> str: ...
    @property
    def GraphTypeID (self) -> Guid: ...
    @property
    def Icon_16x16 (self) -> Image: ...
    @property
    def IsValid (self) -> bool: ...
    def ValueAt (self, t : float) -> float: ...
    @property
    def Grips (self) -> List: ...
    def ClearCaches (self) -> None: ...
    def GDI_GraphPath (self, reg : RectangleF) -> Set(PointF): ...
    def Draw_PostRenderGraph (self, g : Graphics, cnt : GH_GraphContainer) -> None: ...
    def Draw_PostRenderGrid (self, g : Graphics, cnt : GH_GraphContainer) -> None: ...
    def Draw_PostRenderGrip (self, g : Graphics, cnt : GH_GraphContainer, index : int) -> None: ...
    def Draw_PostRenderTags (self, g : Graphics, cnt : GH_GraphContainer) -> None: ...
    def Draw_PreRenderGraph (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    def Draw_PreRenderGrid (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    def Draw_PreRenderGrip (self, g : Graphics, cnt : GH_GraphContainer, index : int) -> GH_GraphDrawInstruction: ...
    def Draw_PreRenderTags (self, g : Graphics, cnt : GH_GraphContainer) -> GH_GraphDrawInstruction: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_GraphContainer:
    def __init__(self, n_graph : IGH_Graph): ...
    def __init__(self, n_graph : IGH_Graph, n_x0 : float, n_x1 : float, n_y0 : float, n_y1 : float): ...
    def Duplicate (self) -> GH_GraphContainer: ...
    def PrepareForUse (self) -> None: ...
    def add_GraphChanged (self, obj : GraphChangedEventHandler) -> None: ...
    def remove_GraphChanged (self, obj : GraphChangedEventHandler) -> None: ...
    def OnGraphChanged (self, bIntermediate : bool) -> None: ...
    @property
    def Graph (self) -> IGH_Graph: ...
    @Graph.setter
    def Graph (self, Value : IGH_Graph) -> None: ...
    @property
    def X0 (self) -> float: ...
    @X0.setter
    def X0 (self, Value : float) -> None: ...
    @property
    def X1 (self) -> float: ...
    @X1.setter
    def X1 (self, Value : float) -> None: ...
    @property
    def Y0 (self) -> float: ...
    @Y0.setter
    def Y0 (self, Value : float) -> None: ...
    @property
    def Y1 (self) -> float: ...
    @Y1.setter
    def Y1 (self, Value : float) -> None: ...
    @property
    def LockGrips (self) -> bool: ...
    @LockGrips.setter
    def LockGrips (self, Value : bool) -> None: ...
    @property
    def Region (self) -> RectangleF: ...
    @Region.setter
    def Region (self, Value : RectangleF) -> None: ...
    def RespondToMouseDoubleClick (self, sender : GH_Canvas, e : GH_CanvasMouseEvent) -> GH_ObjectResponse: ...
    def RespondToKeyDown (self, sender : GH_Canvas, e : KeyEventArgs) -> GH_ObjectResponse: ...
    def RespondToKeyUp (self, sender : GH_Canvas, e : KeyEventArgs) -> GH_ObjectResponse: ...
    def RespondToMouseDown (self, sender : GH_Canvas, e : GH_CanvasMouseEvent) -> GH_ObjectResponse: ...
    def RespondToMouseMove (self, sender : GH_Canvas, e : GH_CanvasMouseEvent) -> GH_ObjectResponse: ...
    def RespondToMouseUp (self, sender : GH_Canvas, e : GH_CanvasMouseEvent) -> GH_ObjectResponse: ...
    @property
    def DisplayScale (self) -> Single: ...
    @DisplayScale.setter
    def DisplayScale (self, AutoPropertyValue : Single) -> None: ...
    def RemapPointsToGraphRegion (self, pts : Set(PointF)) -> None: ...
    def ClearCaches (self) -> None: ...
    def Render (self, G : Graphics, bIncludeDomainTags : bool, samples : List) -> None: ...
    def Render_GraphBackground (G : Graphics, region : RectangleF, bActive : bool) -> None: ...
    def Render_GraphGrid (G : Graphics, region : RectangleF) -> None: ...
    def Render_GuidePen () -> Pen: ...
    def Render_GraphPen (self) -> Pen: ...
    def Render_VerticalConstraint (g : Graphics, rec : RectangleF, t : float) -> None: ...
    def Render_HorizontalConstraint (g : Graphics, rec : RectangleF, t : float) -> None: ...
    def ToX (self, t_unit : float) -> float: ...
    def ToY (self, t_unit : float) -> float: ...
    def FromX (self, t : float) -> float: ...
    def FromY (self, t : float) -> float: ...
    def ToUnitBox (self, pt : PointF) -> PointF: ...
    def ToRegionBox (self, pt : PointF) -> PointF: ...
    def ToRegionBox_x (self, x : float) -> Single: ...
    def ToRegionBox_y (self, y : float) -> Single: ...
    def ValueAt (self, t : float) -> float: ...
    def TryValueAt (self, t : float) -> float: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GripChangedEventHandler:
    def __init__(self, TargetObject : Object, TargetMethod : IntPtr): ...
    def BeginInvoke (self, sender : GH_GraphGrip, bIntermediate : bool, DelegateCallback : AsyncCallback, DelegateAsyncState : Object) -> IAsyncResult: ...
    def EndInvoke (self, DelegateAsyncResult : IAsyncResult) -> None: ...
    def Invoke (self, sender : GH_GraphGrip, bIntermediate : bool) -> None: ...
class GH_LinearGraphProxy:
    def __init__(self, n_owner : GH_LinearGraph): ...
    @property
    def Slope (self) -> float: ...
    @Slope.setter
    def Slope (self, Value : float) -> None: ...
    @property
    def Intercept (self) -> float: ...
    @Intercept.setter
    def Intercept (self, Value : float) -> None: ...
class GraphChangedEventHandler:
    def __init__(self, TargetObject : Object, TargetMethod : IntPtr): ...
    def BeginInvoke (self, sender : IGH_Graph, bIntermediate : bool, DelegateCallback : AsyncCallback, DelegateAsyncState : Object) -> IAsyncResult: ...
    def EndInvoke (self, DelegateAsyncResult : IAsyncResult) -> None: ...
    def Invoke (self, sender : IGH_Graph, bIntermediate : bool) -> None: ...
class GraphChangedEventHandler:
    def __init__(self, TargetObject : Object, TargetMethod : IntPtr): ...
    def BeginInvoke (self, sender : GH_GraphContainer, bIntermediate : bool, DelegateCallback : AsyncCallback, DelegateAsyncState : Object) -> IAsyncResult: ...
    def EndInvoke (self, DelegateAsyncResult : IAsyncResult) -> None: ...
    def Invoke (self, sender : GH_GraphContainer, bIntermediate : bool) -> None: ...
