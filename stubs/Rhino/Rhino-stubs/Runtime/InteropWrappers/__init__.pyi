from typing import Tuple, Set, Iterable, List

class StringHolder:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    def Dispose (self) -> None: ...
    def ToString (self) -> str: ...
    def GetString (pStringHolder : IntPtr) -> str: ...
class SimpleArrayInt:
    def __init__(self): ...
    def __init__(self, values : Iterable[int]): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(int): ...
    def Dispose (self) -> None: ...
class SimpleArrayUint:
    def __init__(self): ...
    def __init__(self, values : Iterable[UInt32]): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    @property
    def UnsignedCount (self) -> UInt32: ...
    def ToArray (self) -> Set(UInt32): ...
    def Dispose (self) -> None: ...
class SimpleArrayGuidPointer:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Item (self, index : int) -> Guid: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(Guid): ...
    def Dispose (self) -> None: ...
class SimpleArrayGuid:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Item (self, index : int) -> Guid: ...
    def Append (self, uuid : Guid) -> None: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(Guid): ...
    def Dispose (self) -> None: ...
class SimpleArrayInterval:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    def Add (self, interval : Interval) -> None: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(Interval): ...
    def Dispose (self) -> None: ...
class SimpleArrayDouble:
    def __init__(self): ...
    def __init__(self, items : Iterable[float]): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(float): ...
    def Dispose (self) -> None: ...
class SimpleArrayPoint2d:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(Point2d): ...
    def Dispose (self) -> None: ...
class SimpleArrayPoint3d:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(Point3d): ...
    def Dispose (self) -> None: ...
class SimpleArrayArrayPoint3d:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def PointCountAt (self, index : int) -> int: ...
    @property
    def Item (self, index : int, pointIndex : int) -> Point3d: ...
    def Dispose (self) -> None: ...
class SimpleArrayPlane:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(Plane): ...
    def Dispose (self) -> None: ...
class SimpleArrayLine:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(Line): ...
    def Dispose (self) -> None: ...
class SimpleArray2dex:
    def __init__(self): ...
    def __init__(self, values : Iterable[IndexPair]): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def ToArray (self) -> Set(IndexPair): ...
    def Dispose (self) -> None: ...
class SimpleArraySurfacePointer:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    def ToNonConstArray (self) -> Set(Surface): ...
    def Dispose (self) -> None: ...
class SimpleArrayCurvePointer:
    def __init__(self): ...
    def __init__(self, curves : Iterable[Curve]): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    def ToNonConstArray (self) -> Set(Curve): ...
    def Dispose (self) -> None: ...
class SimpleArrayGeometryPointer:
    def __init__(self): ...
    def __init__(self, geometry : Iterable[GeometryBase]): ...
    def __init__(self, geometry : IEnumerable): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    def ToNonConstArray (self) -> Set(GeometryBase): ...
    def Dispose (self) -> None: ...
class SimpleArrayMeshPointer:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def Add (self, mesh : Mesh, asConst : bool) -> None: ...
    def Dispose (self) -> None: ...
    def ToNonConstArray (self) -> Set(Mesh): ...
class SimpleArrayBrepPointer:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def Add (self, brep : Brep, asConst : bool) -> None: ...
    def Dispose (self) -> None: ...
    def ToNonConstArray (self) -> Set(Brep): ...
class SimpleArrayLinetypePointer:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def Dispose (self) -> None: ...
    def ToNonConstArray (self) -> Set(Linetype): ...
class SimpleArrayExtrusionPointer:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def Add (self, extrusion : Extrusion, asConst : bool) -> None: ...
    def Dispose (self) -> None: ...
    def ToNonConstArray (self) -> Set(Extrusion): ...
class SimpleArrayBinaryArchiveReader:
    def __init__(self): ...
    def __init__(self, p : IntPtr): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    def Add (self, reader : BinaryArchiveReader) -> None: ...
    @property
    def Count (self) -> int: ...
    def Get (self, index : int) -> BinaryArchiveReader: ...
    def Dispose (self) -> None: ...
class ClassArrayString:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def Add (self, s : str) -> None: ...
    def Dispose (self) -> None: ...
    def ToArray (self) -> Set(str): ...
class ClassArrayObjRef:
    def __init__(self): ...
    def __init__(self, objrefs : Iterable[ObjRef]): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def Add (self, objref : ObjRef) -> None: ...
    def Dispose (self) -> None: ...
    def ToNonConstArray (self) -> Set(ObjRef): ...
class ClassArrayOnObjRef:
    def __init__(self): ...
    def __init__(self, objrefs : Iterable[ObjRef]): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def Add (self, objref : ObjRef) -> None: ...
    def Dispose (self) -> None: ...
    def ToNonConstArray (self) -> Set(ObjRef): ...
class SimpleArrayClippingPlaneObjectPointer:
    def __init__(self): ...
    def ConstPointer (self) -> IntPtr: ...
    def NonConstPointer (self) -> IntPtr: ...
    @property
    def Count (self) -> int: ...
    def Add (self, clippingplane : ClippingPlaneObject, asConst : bool) -> None: ...
    def Dispose (self) -> None: ...
class MeshPointDataStruct:
class StringWrapper:
    def __init__(self): ...
    def __init__(self, s : str): ...
    @property
    def ConstPointer (self) -> IntPtr: ...
    @property
    def NonConstPointer (self) -> IntPtr: ...
    def Dispose (self) -> None: ...
    def ToString (self) -> str: ...
    def SetString (self, s : str) -> None: ...
    def SetStringOnPointer (pON_wString : IntPtr, s : str) -> None: ...
    def GetStringFromPointer (pConstON_wString : IntPtr) -> str: ...
