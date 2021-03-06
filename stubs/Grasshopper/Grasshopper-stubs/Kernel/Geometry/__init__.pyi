from typing import Tuple, Set, Iterable, List

class GH_CurveOffsetCorner:
    Chamfer = 0
    Sharp = 1
    Fillet = 2
class GH_CurveOffset:
    def __init__(self, curve : Curve, offsetPlane : Plane): ...
    def __init__(self, curves : Iterable[Curve], offsetPlane : Plane): ...
    @property
    def OffsetPlane (self) -> Plane: ...
    def OffsetSamples (self, distance : float) -> List: ...
    def Offset (self, distance : float, corner : GH_CurveOffsetCorner) -> List: ...
class GH_SanityXForm:
    def __init__(self): ...
    def CreateSanityXForms (self, box : BoundingBox) -> bool: ...
    def MakeSane (self, geometry : GeometryBase) -> None: ...
    def MakeInsane (self, geometry : GeometryBase) -> None: ...
    def MakeSane (self, geometry : IGH_GeometricGoo) -> Tuple[IGH_GeometricGoo]: ...
    def MakeInsane (self, geometry : IGH_GeometricGoo) -> Tuple[IGH_GeometricGoo]: ...
    def MakeSane (self, geometry : Point3d) -> Tuple[Point3d]: ...
    def MakeInsane (self, geometry : Point3d) -> Tuple[Point3d]: ...
    def MakeSane (self, geometry : Plane) -> Tuple[Plane]: ...
    def MakeInsane (self, geometry : Plane) -> Tuple[Plane]: ...
class Node2:
    def __init__(self): ...
    def __init__(self, nx : float, ny : float): ...
    def __init__(self, nx : float, ny : float, n_tag : int): ...
    def __init__(self, other : Node2): ...
    def __init__(self, other : Node2, dx : float, dy : float): ...
    def __init__(self, A : Node2, B : Node2, f : float, n_tag : int): ...
    def Duplicate (self) -> Node2: ...
    def Set (self, other : Node2) -> None: ...
    def Set (self, nX : float, nY : float) -> None: ...
    def op_Subtraction (A : Node2, B : Node2) -> Vec2: ...
    def op_Addition (P : Node2, V : Vec2) -> Node2: ...
    def op_Addition (A : Node2, B : Node2) -> Node2: ...
    def op_Subtraction (P : Node2, V : Vec2) -> Node2: ...
    def op_Multiply (N : Node2, f : float) -> Node2: ...
    def op_Multiply (f : float, N : Node2) -> Node2: ...
    def Offset (self, dx : float, dy : float) -> None: ...
    def DistanceSquared (self, other : Node2) -> float: ...
    def DistanceSquared (self, nx : float, ny : float) -> float: ...
    def Distance (self, other : Node2) -> float: ...
    def Distance (self, nx : float, ny : float) -> float: ...
    def IsCoincident (self, other : Node2) -> bool: ...
    def IsCoincident (self, ox : float, oy : float) -> bool: ...
    @property
    def IsValid (self) -> bool: ...
    def CompareTo (self, other : Node2) -> int: ...
    def CompareTo (self, other : Node2, tolerance : float) -> int: ...
    def ToString (self) -> str: ...
    @property
    def DebuggerDisplay (self) -> str: ...
class Node3:
    def __init__(self): ...
    def __init__(self, nX : float, nY : float, nZ : float, nI : int): ...
    def __init__(self, other : Node3): ...
    def __init__(self, other : Point3d, nI : int): ...
    def __init__(self, other : Point3f, nI : int): ...
    def Duplicate (self) -> Node3: ...
    def Set (self, other : Node3) -> None: ...
    def Set (self, nX : float, nY : float, nZ : float) -> None: ...
    def op_Subtraction (A : Node3, B : Node3) -> Vec3: ...
    def op_Addition (P : Node3, V : Vec3) -> Node3: ...
    def Offset (self, dx : float, dy : float, dz : float) -> None: ...
    def Distance (self, other : Node3) -> float: ...
    def Distance (self, ox : float, oy : float, oz : float) -> float: ...
    def DistanceSquared (self, other : Node3) -> float: ...
    def DistanceSquared (self, ox : float, oy : float, oz : float) -> float: ...
    def Coincident (self, other : Node3) -> bool: ...
    def CoincidentFlat (self, other : Node3) -> bool: ...
    @property
    def IsValid (self) -> bool: ...
    def CompareTo (self, other : Node3) -> int: ...
    def ToString (self) -> str: ...
    @property
    def DebuggerDisplay (self) -> str: ...
class Parallax:
    Divergent = 0
    Parallel = 1
    AntiParallel = -1
class Containment:
    none = 0
    inside = 1
    coincident = 2
    outside = 3
class Vec2:
    def __init__(self): ...
    def __init__(self, nX : float, nY : float): ...
    def __init__(self, other : Vec2): ...
    def __init__(self, other : Vector2d): ...
    def __init__(self, other : Vector2f): ...
    def Duplicate (self) -> Vec2: ...
    def Set (self, other : Vec2) -> None: ...
    def Set (self, nX : float, nY : float) -> None: ...
    def op_Addition (A : Vec2, B : Vec2) -> Vec2: ...
    def op_Subtraction (A : Vec2, B : Vec2) -> Vec2: ...
    def op_Multiply (V : Vec2, F : float) -> Vec2: ...
    @property
    def Unit_X () -> Vec2: ...
    @property
    def Unit_Y () -> Vec2: ...
    def Length (self) -> float: ...
    def LengthSquared (self) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def ToString (self) -> str: ...
    @property
    def DebuggerDisplay (self) -> str: ...
    def CompareTo (self, other : Vec2) -> int: ...
    def CreatePerpendicular (self) -> Vec2: ...
    def PerpendicularTo (self, v : Vec2) -> bool: ...
    def PerpendicularTo (self, v : Vec2, angle_tol : float) -> bool: ...
    def ParallelTo (self, v : Vec2) -> Parallax: ...
    def ParallelTo (self, v : Vec2, angle_tol : float) -> Parallax: ...
    def Unitize (self) -> None: ...
class Vec3:
    def __init__(self): ...
    def __init__(self, nX : float, nY : float, nZ : float): ...
    def __init__(self, other : Vec3): ...
    def __init__(self, other : Vector3d): ...
    def __init__(self, other : Vector3f): ...
    def Duplicate (self) -> Vec3: ...
    def Set (self, other : Vec3) -> None: ...
    def Set (self, nX : float, nY : float, nZ : float) -> None: ...
    def op_Addition (A : Vec3, B : Vec3) -> Vec3: ...
    def op_Subtraction (A : Vec3, B : Vec3) -> Vec3: ...
    def op_Multiply (A : Vec3, B : Vec3) -> float: ...
    def op_Multiply (V : Vec3, F : float) -> Vec3: ...
    def CrossProduct (A : Vec3, B : Vec3) -> Vec3: ...
    def CrossProduct (ax : float, ay : float, az : float, bx : float, by : float, bz : float) -> Vec3: ...
    @property
    def Unit_X () -> Vec3: ...
    @property
    def Unit_Y () -> Vec3: ...
    @property
    def Unit_Z () -> Vec3: ...
    def Length (self) -> float: ...
    def LengthFlat (self) -> float: ...
    def LengthSquared (self) -> float: ...
    def LengthSquaredFlat (self) -> float: ...
    @property
    def IsValid (self) -> bool: ...
    def ToString (self) -> str: ...
    @property
    def DebuggerDisplay (self) -> str: ...
    def CompareTo (self, other : Vec3) -> int: ...
    def CreatePerpendicular (self) -> Vec3: ...
    def PerpendicularTo (self, v : Vec3) -> bool: ...
    def PerpendicularTo (self, v : Vec3, angle_tol : float) -> bool: ...
    def ParallelTo (self, v : Vec3) -> Parallax: ...
    def ParallelTo (self, v : Vec3, angle_tol : float) -> Parallax: ...
    def Unitize (self) -> None: ...
class Side2:
    Coincident = 0
    Right = 1
    Left = -1
class LineX:
    None = 0
    Parallel = 1
    Coincident = 2
    Point = 3
class LineCircleX:
    None = 0
    Tangent = 1
    Secant = 2
class Line2:
    def __init__(self): ...
    def __init__(self, nAx : float, nAy : float, nBx : float, nBy : float): ...
    def __init__(self, nA : Node2, nB : Node2): ...
    def __init__(self, other : Line2): ...
    def Duplicate (self) -> Line2: ...
    def Set (self, other : Line2) -> None: ...
    def Set (self, A : Node2, B : Node2) -> None: ...
    def Length (self) -> float: ...
    def LengthSquared (self) -> float: ...
    def PointAt (self, t : float) -> Node2: ...
    def ClosestPoint (self, pt : Node2) -> float: ...
    def ClosestPoint (self, x : float, y : float) -> float: ...
    def DistanceTo (self, pt : Node2) -> float: ...
    def DistanceTo (self, x : float, y : float) -> float: ...
    def DistanceToSquared (self, pt : Node2) -> float: ...
    def DistanceToSquared (self, x : float, y : float) -> float: ...
    def Side (edge : Line2, pt : Node2) -> Side2: ...
    def Side (Ax : float, Ay : float, Bx : float, By : float, Px : float, Py : float) -> Side2: ...
    def Intersect (A : Line2, B : Line2, t : float) -> Tuple[LineX, float]: ...
    def Intersect (Ax : float, Ay : float, Bx : float, By : float, Cx : float, Cy : float, Dx : float, Dy : float, t : float) -> Tuple[LineX, float]: ...
    def Intersect (A : Line2, B : Line2, t0 : float, t1 : float) -> Tuple[LineX, float, float]: ...
    def Intersect (Ax : float, Ay : float, Bx : float, By : float, Cx : float, Cy : float, Dx : float, Dy : float, t0 : float, t1 : float) -> Tuple[LineX, float, float]: ...
    def MidLine (A : Node2, B : Node2) -> Line2: ...
    def MidLine (A : Node2, B : Node2, Wa : float, Wb : float) -> Line2: ...
class Line3:
    def __init__(self): ...
    def __init__(self, nAx : float, nAy : float, nAz : float, nBx : float, nBy : float, nBz : float): ...
    def __init__(self, nA : Node3, nB : Node3): ...
    def __init__(self, other : Line3): ...
    def Duplicate (self) -> Line3: ...
    def Set (self, other : Line3) -> None: ...
    def Set (self, A : Node3, B : Node3) -> None: ...
    def Length (self) -> float: ...
    def LengthSquared (self) -> float: ...
    def PointAt (self, t : float) -> Node3: ...
    def ClosestPoint (self, pt : Node3) -> float: ...
    def ClosestPoint (self, x : float, y : float, z : float) -> float: ...
    def DistanceTo (self, pt : Node3) -> float: ...
    def DistanceTo (self, x : float, y : float, z : float) -> float: ...
    def DistanceToSquared (self, pt : Node3) -> float: ...
    def DistanceToSquared (self, x : float, y : float, z : float) -> float: ...
    def Intersect (A : Line3, B : Line3, t : float) -> Tuple[LineX, float]: ...
    def Intersect (Ax : float, Ay : float, Az : float, Bx : float, By : float, Bz : float, Cx : float, Cy : float, Cz : float, Dx : float, Dy : float, Dz : float, t : float) -> Tuple[LineX, float]: ...
    def Intersect (A : Line3, B : Line3, t0 : float, t1 : float) -> Tuple[LineX, float, float]: ...
    def Intersect (Ax : float, Ay : float, Az : float, Bx : float, By : float, Bz : float, Cx : float, Cy : float, Cz : float, Dx : float, Dy : float, Dz : float, t0 : float, t1 : float) -> Tuple[LineX, float, float]: ...
class Rectangle2:
    def __init__(self): ...
    def __init__(self, x0 : float, y0 : float, x1 : float, y1 : float): ...
    def __init__(self, p0 : Node2, p1 : Node2): ...
    def MakeIncreasing (self) -> None: ...
    @property
    def IsValid (self) -> bool: ...
    def PointAt (self, x : float, y : float) -> Node2: ...
    def ParameterAt (self, pt : Node2) -> Node2: ...
    def ParameterAt (self, x : float, y : float) -> Node2: ...
    def Grow (self, pt : Node2) -> None: ...
    def Grow (self, x : float, y : float) -> None: ...
    def Grow (self, rec : Rectangle2) -> None: ...
    def Includes (self, pt : Node2) -> Containment: ...
    def Includes (self, x : float, y : float) -> Containment: ...
    def Intersect (self, line : Line2) -> Node2: ...
class Plane:
    def __init__(self): ...
    def __init__(self, other : Plane): ...
    def __init__(self, nOrigin : Node3, nNormal : Vec3): ...
    def __init__(self, nOrigin : Node3, nXAxis : Vec3, nYAxis : Vec3): ...
    def __init__(self, nOrigin : Node3, nXAxis : Vec3, nYAxis : Vec3, nZAxis : Vec3): ...
    def __init__(self, other : Plane): ...
    @property
    def World_XY () -> Plane: ...
    def Project (self, pt : Node3, s : float, t : float) -> Tuple[float, float]: ...
    def Project (self, pt : Node3) -> None: ...
    def Project (self, pts : List[Node3]) -> None: ...
    def PointAt (self, u : float, v : float) -> Node3: ...
    def PointAt (self, u : float, v : float, w : float) -> Node3: ...
    def Unitize (self) -> None: ...
class Circle2:
    def __init__(self): ...
    def __init__(self, origin : Node2, radius : float): ...
    def __init__(self, other : Circle2): ...
    def __init__(self, A : Node2, B : Node2, C : Node2): ...
    def Circle3Pt (ax : float, ay : float, bx : float, by : float, cx : float, cy : float, ox : float, oy : float, r2 : float) -> Tuple[bool, float, float, float]: ...
    def Duplicate (self) -> Circle2: ...
    @property
    def Circumference (self) -> float: ...
    @property
    def Area (self) -> float: ...
    def PointAt (self, t : float) -> Node2: ...
    def TangentAt (self, t : float) -> Vec2: ...
    def ClosestPointTo (self, pt : Node2) -> float: ...
    def ClosestPointTo (self, x : float, y : float) -> float: ...
    def ClosestPointTo (self, pt : Node2, t : float) -> Tuple[Node2, float]: ...
    def ClosestPointTo (self, x : float, y : float, t : float) -> Tuple[Node2, float]: ...
    def Contains (self, pt : Node2) -> Containment: ...
    def Contains (self, x : float, y : float) -> Containment: ...
    def Intersect (self, line : Line2, l0 : float, l1 : float) -> Tuple[LineCircleX, float, float]: ...
    def Intersect (self, line : Line2, l0 : float, l1 : float, a0 : float, a1 : float) -> Tuple[LineCircleX, float, float, float, float]: ...
class Region2:
    def __init__(self, nodes : Iterable[Node2]): ...
    def Contains (self, node : Node2) -> bool: ...
class SamplingRegion:
    def __init__(self, regions : Iterable[Curve]): ...
    def Dispose (self) -> None: ...
class Node2List:
    def __init__(self): ...
    def __init__(self, L : Iterable[Node2]): ...
    def __init__(self, L : Node2List): ...
    def __init__(self, pts : Iterable[GH_Point]): ...
    def __init__(self, pts : Iterable[Point3d]): ...
    def Append (self, node : Node2) -> None: ...
    def AppendRange (self, nodes : Iterable[Node2]) -> None: ...
    def Insert (self, index : int, node : Node2) -> None: ...
    def InsertRange (self, index : int, nodes : Iterable[Node2]) -> None: ...
    def Remove (self, node : Node2) -> bool: ...
    def RemoveAt (self, index : int) -> None: ...
    @property
    def Node (self, i : int) -> Node2: ...
    @Node.setter
    def Node (self, i : int, Value : Node2) -> None: ...
    @property
    def Count (self) -> int: ...
    @property
    def Capacity (self) -> int: ...
    @Capacity.setter
    def Capacity (self, Value : int) -> None: ...
    def CullDuplicates (self) -> int: ...
    def NullifyDuplicates (self) -> int: ...
    def CullNullRefs (self) -> int: ...
    @property
    def InternalList (self) -> List: ...
    @InternalList.setter
    def InternalList (self, Value : List) -> None: ...
    def JitterNodes (self, amount : float) -> None: ...
    def ExpireSequence (self) -> None: ...
    def Sort (self, type : NodeListSort) -> None: ...
    def RenumberNodes (self) -> None: ...
    def BinarySearch_X (self, x : float) -> int: ...
    def BinarySearch_Y (self, y : float) -> int: ...
    def BinarySearch_I (self, i : int) -> int: ...
    def NearestNodes (self, x : float, y : float, N : int, min_dist_squared : float, max_dist_squared : float) -> List: ...
    def BoundingBox (self, GrowthFactor : float, ForceSquareLeaves : bool, x0 : float, x1 : float, y0 : float, y1 : float) -> Tuple[bool, float, float, float, float]: ...
    def CreateTree (self, GrowthFactor : float, SquareLeaves : bool, GroupLimit : int) -> Node2Tree: ...
    def GetEnumerator (self) -> IEnumerator: ...
    def GetEnumerator1 (self) -> IEnumerator: ...
class Node3List:
    def __init__(self): ...
    def __init__(self, L : Iterable[Node3]): ...
    def __init__(self, L : Node3List): ...
    def __init__(self, pts : Iterable[GH_Point]): ...
    def __init__(self, pts : Iterable[Point3d]): ...
    def Append (self, node : Node3) -> None: ...
    def AppendRange (self, nodes : Iterable[Node3]) -> None: ...
    def Insert (self, index : int, node : Node3) -> None: ...
    def InsertRange (self, index : int, nodes : Iterable[Node3]) -> None: ...
    def Remove (self, node : Node3) -> bool: ...
    def RemoveAt (self, index : int) -> None: ...
    @property
    def Node (self, i : int) -> Node3: ...
    @Node.setter
    def Node (self, i : int, Value : Node3) -> None: ...
    @property
    def Count (self) -> int: ...
    @property
    def Capacity (self) -> int: ...
    @Capacity.setter
    def Capacity (self, Value : int) -> None: ...
    def CullDuplicates (self) -> int: ...
    def NullifyDuplicates (self) -> int: ...
    def CullNullRefs (self) -> int: ...
    @property
    def InternalList (self) -> List: ...
    @InternalList.setter
    def InternalList (self, Value : List) -> None: ...
    def Clear (self) -> None: ...
    def JitterNodes (self, amount : float) -> None: ...
    def ExpireSequence (self) -> None: ...
    def Sort (self, type : NodeListSort) -> None: ...
    def RenumberNodes (self) -> None: ...
    def BinarySearch_X (self, x : float) -> int: ...
    def BinarySearch_Y (self, y : float) -> int: ...
    def BinarySearch_Z (self, z : float) -> int: ...
    def BinarySearch_I (self, i : int) -> int: ...
    def NearestNodes (self, x : float, y : float, z : float, N : int, min_dist_squared : float, max_dist_squared : float) -> List: ...
    def BoundingBox (self, GrowthFactor : float, ForceSquareLeaves : bool, x0 : float, x1 : float, y0 : float, y1 : float, z0 : float, z1 : float) -> Tuple[bool, float, float, float, float, float, float]: ...
    def CreateTree (self, GrowthFactor : float, SquareLeaves : bool, GroupLimit : int) -> Node3Tree: ...
class Node2Tree:
    def __init__(self): ...
    def __init__(self, owner : Node2List): ...
    def RecreateTree (self, GrowthFactor : float, ForceSquareLeaves : bool, GroupLimit : int) -> bool: ...
    def PerformAction (self, func : LeafAction, call_on_empty_leaves : bool) -> None: ...
    def PerformAction (self, func : ILeafAction, call_on_empty_leaves : bool) -> None: ...
    def SolveProximity (self, prox : Node2Proximity) -> None: ...
class Node2Leaf:
    def __init__(self): ...
    def __init__(self, x0 : float, x1 : float, y0 : float, y1 : float): ...
    def __init__(self, other : Node2Leaf): ...
    @property
    def Nodes (self) -> List: ...
    def SubDivide (self, nodes : Node2List, index_subset : List, group_limit : int) -> None: ...
    @property
    def x_min (self) -> float: ...
    @property
    def x_max (self) -> float: ...
    @property
    def y_min (self) -> float: ...
    @property
    def y_max (self) -> float: ...
    @property
    def x_mid (self) -> float: ...
    @property
    def y_mid (self) -> float: ...
    @property
    def A (self) -> Node2Leaf: ...
    @property
    def B (self) -> Node2Leaf: ...
    @property
    def C (self) -> Node2Leaf: ...
    @property
    def D (self) -> Node2Leaf: ...
    @property
    def SubLeafCount (self) -> int: ...
    def Contains (self, x : float, y : float) -> bool: ...
    def MinimumDistance (self, x : float, y : float) -> float: ...
    def MinimumDistanceSquared (self, x : float, y : float) -> float: ...
    def MaximumDistance (self, x : float, y : float) -> float: ...
    def MaximumDistanceSquared (self, x : float, y : float) -> float: ...
    def PerformLeafAction (self, func : LeafAction, call_on_empty_leaves : bool) -> None: ...
    def PerformLeafAction (self, func : ILeafAction, call_on_empty_leaves : bool) -> None: ...
    def SolveProximity (self, nodes : Node2List, prox : Node2Proximity) -> None: ...
class Node3Tree:
    def __init__(self): ...
    def __init__(self, owner : Node3List): ...
    def RecreateTree (self, growthFactor : float, squareLeaves : bool, groupLimit : int) -> bool: ...
    def PerformAction (self, func : LeafAction, call_on_empty_leaves : bool) -> None: ...
    def PerformAction (self, func : ILeafAction, call_on_empty_leaves : bool) -> None: ...
    @property
    def Root (self) -> Node3Leaf: ...
    def SolveProximity (self, prox : Node3Proximity) -> None: ...
class Node3Leaf:
    def __init__(self): ...
    def __init__(self, x0 : float, x1 : float, y0 : float, y1 : float, z0 : float, z1 : float): ...
    def __init__(self, other : Node3Leaf): ...
    @property
    def Nodes (self) -> List: ...
    def SubDivide (self, nodes : Node3List, index_subset : List, group_limit : int) -> None: ...
    def RemoveNode (self, nodes : Node3List, nodeTag : int) -> bool: ...
    def RemoveNode (self, nodes : Node3List, node : Node3) -> bool: ...
    def TrimExcess (self) -> None: ...
    @property
    def x_min (self) -> float: ...
    @property
    def x_max (self) -> float: ...
    @property
    def y_min (self) -> float: ...
    @property
    def y_max (self) -> float: ...
    @property
    def z_min (self) -> float: ...
    @property
    def z_max (self) -> float: ...
    @property
    def x_mid (self) -> float: ...
    @property
    def y_mid (self) -> float: ...
    @property
    def z_mid (self) -> float: ...
    @property
    def A (self) -> Node3Leaf: ...
    @property
    def B (self) -> Node3Leaf: ...
    @property
    def C (self) -> Node3Leaf: ...
    @property
    def D (self) -> Node3Leaf: ...
    @property
    def E (self) -> Node3Leaf: ...
    @property
    def F (self) -> Node3Leaf: ...
    @property
    def G (self) -> Node3Leaf: ...
    @property
    def H (self) -> Node3Leaf: ...
    @property
    def SubLeafCount (self) -> int: ...
    def Contains (self, x : float, y : float, z : float) -> bool: ...
    def MinimumDistance (self, x : float, y : float, z : float) -> float: ...
    def MinimumDistanceSquared (self, x : float, y : float, z : float) -> float: ...
    def MaximumDistance (self, x : float, y : float, z : float) -> float: ...
    def MaximumDistanceSquared (self, x : float, y : float, z : float) -> float: ...
    def PerformLeafAction (self, func : LeafAction, call_on_empty_leaves : bool) -> None: ...
    def PerformLeafAction (self, func : ILeafAction, call_on_empty_leaves : bool) -> None: ...
    def SolveProximity (self, nodes : Node3List, prox : Node3Proximity) -> None: ...
class Node2Proximity:
    def __init__(self, search_start : Node2, search_start_index : int): ...
    def __init__(self, search_start : Node2, search_start_index : int, max_results : int): ...
    def __init__(self, search_start : Node2, search_start_index : int, max_results : int, min_distance : float, max_distance : float): ...
    def ResetLists (self) -> None: ...
    @property
    def Start (self) -> Node2: ...
    @property
    def StartIndex (self) -> int: ...
    @property
    def MaximumCount (self) -> int: ...
    @property
    def CurrentCount (self) -> int: ...
    @property
    def MinSearchRadius (self) -> float: ...
    @property
    def MaxSearchRadius (self) -> float: ...
    @property
    def MinSearchRadiusSquared (self) -> float: ...
    @property
    def MaxSearchRadiusSquared (self) -> float: ...
    @property
    def NearestPoint (self) -> int: ...
    @property
    def FurthestPoint (self) -> int: ...
    @property
    def NearestDistance (self) -> float: ...
    @property
    def NearestDistanceSquared (self) -> float: ...
    @property
    def FurthestDistance (self) -> float: ...
    @property
    def FurthestDistanceSquared (self) -> float: ...
    @property
    def IndexList (self) -> List: ...
    @property
    def DistanceList (self) -> List: ...
    def DistanceRange (self, d0 : float, d1 : float) -> Tuple[float, float]: ...
    def RegisterNode (self, node : Node2, index : int) -> bool: ...
class Node3Proximity:
    def __init__(self, search_start : Node3, search_start_index : int): ...
    def __init__(self, search_start : Node3, search_start_index : int, max_results : int): ...
    def __init__(self, search_start : Node3, search_start_index : int, max_results : int, min_distance : float, max_distance : float): ...
    def ResetLists (self) -> None: ...
    @property
    def Start (self) -> Node3: ...
    @property
    def StartIndex (self) -> int: ...
    @property
    def MaximumCount (self) -> int: ...
    @property
    def CurrentCount (self) -> int: ...
    @property
    def MinSearchRadius (self) -> float: ...
    @property
    def MaxSearchRadius (self) -> float: ...
    @property
    def MinSearchRadiusSquared (self) -> float: ...
    @property
    def MaxSearchRadiusSquared (self) -> float: ...
    @property
    def NearestPoint (self) -> int: ...
    @property
    def FurthestPoint (self) -> int: ...
    @property
    def NearestDistance (self) -> float: ...
    @property
    def NearestDistanceSquared (self) -> float: ...
    @property
    def FurthestDistance (self) -> float: ...
    @property
    def FurthestDistanceSquared (self) -> float: ...
    @property
    def IndexList (self) -> List: ...
    @property
    def DistanceList (self) -> List: ...
    def DistanceRange (self, d0 : float, d1 : float) -> Tuple[float, float]: ...
    def RegisterNode (self, node : Node3, index : int) -> bool: ...
class PointCloud:
    def __init__(self): ...
    def InsertPoint (self, pt : Point3d) -> int: ...
class NodeListSort:
    none = 0
    X = 1
    Y = 2
    Index = 3
class NodeListSort:
    none = 0
    X = 1
    Y = 2
    Z = 3
    Index = 4
class VorLeafRecursionResult:
    Continue = 0
    Abort = -1
class LeafAction:
    def __init__(self, TargetObject : Object, TargetMethod : IntPtr): ...
    def BeginInvoke (self, Leaf : Node2Leaf, DelegateCallback : AsyncCallback, DelegateAsyncState : Object) -> IAsyncResult: ...
    def EndInvoke (self, DelegateAsyncResult : IAsyncResult) -> VorLeafRecursionResult: ...
    def Invoke (self, Leaf : Node2Leaf) -> VorLeafRecursionResult: ...
class ILeafAction:
    def LeafAction (self, Leaf : Node2Leaf) -> VorLeafRecursionResult: ...
class VorLeafRecursionResult:
    Continue = 0
    Abort = -1
class LeafAction:
    def __init__(self, TargetObject : Object, TargetMethod : IntPtr): ...
    def BeginInvoke (self, Leaf : Node3Leaf, DelegateCallback : AsyncCallback, DelegateAsyncState : Object) -> IAsyncResult: ...
    def EndInvoke (self, DelegateAsyncResult : IAsyncResult) -> VorLeafRecursionResult: ...
    def Invoke (self, Leaf : Node3Leaf) -> VorLeafRecursionResult: ...
class ILeafAction:
    def LeafAction (self, Leaf : Node3Leaf) -> VorLeafRecursionResult: ...
