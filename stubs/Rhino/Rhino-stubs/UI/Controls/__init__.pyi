from typing import Tuple, Set, Iterable, List

class FactoryBase:
    def Get (self, id : Guid) -> IntPtr: ...
    def Register (plugin : PlugIn) -> Set(Type): ...
    def Register () -> Set(Type): ...
class IHasCppImplementation:
    @property
    def CppPointer (self) -> IntPtr: ...
class IWindow:
    @property
    def Created (self) -> bool: ...
    @property
    def Shown (self) -> bool: ...
    @Shown.setter
    def Shown (self, value : bool) -> None: ...
    @property
    def Enabled (self) -> bool: ...
    @Enabled.setter
    def Enabled (self, value : bool) -> None: ...
    @property
    def Caption (self) -> LocalizeStringPair: ...
    @property
    def Parent (self) -> IntPtr: ...
    @Parent.setter
    def Parent (self, value : IntPtr) -> None: ...
    @property
    def Window (self) -> IntPtr: ...
    def Move (self, pos : Rectangle, bRepaint : bool, bRepaintBorder : bool) -> None: ...
class ICollapsibleSectionHolder:
    def Add (self, section : ICollapsibleSection) -> None: ...
    def Remove (self, section : ICollapsibleSection) -> None: ...
    @property
    def Sections (self) -> Iterable[ICollapsibleSection]: ...
    @property
    def SectionCount (self) -> int: ...
    def SectionAt (self, index : int) -> ICollapsibleSection: ...
    def IsSectionExpanded (self, section : ICollapsibleSection) -> bool: ...
    def ExpandSection (self, section : ICollapsibleSection, expand : bool, ensureVisible : bool) -> None: ...
    @BackgroundColor.setter
    def BackgroundColor (self, value : Color) -> None: ...
    @EmptyText.setter
    def EmptyText (self, value : str) -> None: ...
    def UpdateAllViews (self, flags : int) -> None: ...
    @property
    def TopMargin (self) -> int: ...
    @TopMargin.setter
    def TopMargin (self, value : int) -> None: ...
    @property
    def BottomMargin (self) -> int: ...
    @BottomMargin.setter
    def BottomMargin (self, value : int) -> None: ...
    @property
    def LeftMargin (self) -> int: ...
    @LeftMargin.setter
    def LeftMargin (self, value : int) -> None: ...
    @property
    def RightMargin (self) -> int: ...
    @RightMargin.setter
    def RightMargin (self, value : int) -> None: ...
    @property
    def ScrollPosition (self) -> int: ...
    @ScrollPosition.setter
    def ScrollPosition (self, value : int) -> None: ...
    @SettingsPathSubKey.setter
    def SettingsPathSubKey (self, value : str) -> None: ...
class Delegates:
    def __init__(self): ...
class ICollapsibleSection:
    @property
    def Height (self) -> int: ...
    @property
    def Hidden (self) -> bool: ...
    @property
    def InitiallyExpanded (self) -> bool: ...
    @property
    def Id (self) -> Guid: ...
    @property
    def SettingsTag (self) -> str: ...
    @property
    def Collapsible (self) -> bool: ...
    @property
    def BackgroundColor (self) -> Color: ...
    @BackgroundColor.setter
    def BackgroundColor (self, value : Color) -> None: ...
    @property
    def ViewModel (self) -> IRdkViewModel: ...
    @property
    def PlugInId (self) -> Guid: ...
    @property
    def CommandOptionName (self) -> LocalizeStringPair: ...
    def RunScript (self, vm : IRdkViewModel) -> int: ...
    @property
    def ViewModelId (self) -> Guid: ...
class IRdkViewModel:
    def GetData (self, uuidDataType : Guid, bForWrite : bool, bAutoChangeBracket : bool) -> Object: ...
    def Commit (self, uuidDataType : Guid) -> None: ...
    def Discard (self, uuidDataType : Guid) -> None: ...
class CollapsibleSectionViewModel:
    def __init__(self, section : ICollapsibleSection): ...
    def GetData (self, uuidDataType : Guid, bForWrite : bool, bAutoChangeBracket : bool) -> Object: ...
    def Commit (self, uuidDataType : Guid) -> None: ...
    def Discard (self, uuidDataType : Guid) -> None: ...
    def UndoHelper (self, description : str) -> UndoRecord: ...
    @property
    def CppPointer (self) -> IntPtr: ...
class UndoRecord:
    def __init__(self, description : str, viewModel : IRdkViewModel): ...
    def Dispose (self) -> None: ...
class CollapsibleSectionHolderImpl:
    def __init__(self, client : ICollapsibleSectionHolder): ...
    def Dispose (self) -> None: ...
    @property
    def CppPointer (self) -> IntPtr: ...
    def Find (cpp : IntPtr) -> ICollapsibleSectionHolder: ...
    def IsSameObject (self, cpp : IntPtr) -> bool: ...
    def NewNativeWrapper (cpp : IntPtr) -> ICollapsibleSectionHolder: ...
class CollapsibleSectionImpl:
    def __init__(self, section : ICollapsibleSection): ...
    def CreateHostedSection (section : ICollapsibleSection) -> None: ...
    def __InternalSetParent (self, parent : IntPtr) -> None: ...
    def Dispose (self) -> None: ...
    def ReplaceClient (self, client : ICollapsibleSection) -> None: ...
    @property
    def CppPointer (self) -> IntPtr: ...
    def Find (cpp : IntPtr) -> ICollapsibleSection: ...
    def NewNativeWrapper (cpp : IntPtr) -> ICollapsibleSection: ...
    def GetSibling (section : ICollapsibleSection, siblingSectionId : Guid) -> ICollapsibleSection: ...
    def GetSiblings (section : ICollapsibleSection) -> Set(ICollapsibleSection): ...
    @property
    def ViewModel (self) -> IRdkViewModel: ...
    @ViewModel.setter
    def ViewModel (self, value : IRdkViewModel) -> None: ...
    def IsSameObject (self, cpp : IntPtr) -> bool: ...
    def add_DataChanged (self, value : EventHandler) -> None: ...
    def remove_DataChanged (self, value : EventHandler) -> None: ...
    def add_ViewModelActivated (self, value : EventHandler) -> None: ...
    def remove_ViewModelActivated (self, value : EventHandler) -> None: ...
class InternalRdkViewModelFactory(FactoryBase):
    def __init__(self): ...
class CREATEFROMCPPPROC:
    def __init__(self, object : Object, method : IntPtr): ...
    def Invoke (self, hwndParent : IntPtr) -> IntPtr: ...
    def BeginInvoke (self, hwndParent : IntPtr, callback : AsyncCallback, object : Object) -> IAsyncResult: ...
    def EndInvoke (self, result : IAsyncResult) -> IntPtr: ...
class Factory(FactoryBase):
    def __init__(self): ...
class CREATEHOSTFROMCPPPROC:
    def __init__(self, object : Object, method : IntPtr): ...
    def Invoke (self, client : IntPtr) -> IntPtr: ...
    def BeginInvoke (self, client : IntPtr, callback : AsyncCallback, object : Object) -> IAsyncResult: ...
    def EndInvoke (self, result : IAsyncResult) -> IntPtr: ...
