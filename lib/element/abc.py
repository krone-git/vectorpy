from abc import ABC, abstractmethod


class CopyElementType(ABC):
    @abstractmethod
    def copy(element): raise NotImplementedError


class RefreshElementType(ABC):
    @abstractmethod
    def refresh(element): raise NotImplementedError


class MasterElementType(ABC):
    def __init__(self, components):
        self._components = []

    def components(self): return self._components

    def has_component(self, component):
        return component in self._components


class MutableMasterElementType(MasterElementType):
    @abstractmethod
    def add_component(self, component):
        self._components.append(component)
        return self

    @abstractmethod
    def remove_component(self, component):
        self._components.remove(component)
        return self


class ComponentElementType(ABC):
    def __init__(self, master):
        self._master = master

    def master(self): return self._master


class MutableComponentElementType(ComponentElementType):
    @abstractmethod
    def set_master(self, master):
        self._master = master
        return self

    @abstractmethod
    def remove_master(self):
        self._master = None
        return self

class ContentsElementType(ABC):
    "???"
    pass

class BasisElementType(ContentsElementType):
    def __init__(self, matrix):
        self._basis = matrix

    def basis(self): return self._basis

    def set_basis(self, matrix):
        self._basis = matrix
        return self


class OriginElementType(ContentsElementType):
    def __init__(self, origin):
        self._origin = origin

    def origin(self): return self._origin

    def set_origin(self, origin):
        self._origin = origin
        return self


class BaseElementABC(OriginElementType, BasisElementType, RefreshElementType):
    def __init__(self, origin, basis):
        OriginElementType.__init__(self, origin)
        BasisElementType.__init__(self, basis)


class RootElementType(MutableMasterElementType):
    def add_component(self, component):
        is_component = isinstance(component, ComponentElementType)
        is_mutable = isinstance(component, MutableComponentElementType)
        master = component.master()
        if  is_mutable or (is_component and master is self):
            super().add_component(component)
        if is_mutable and master is not self:
            component.set_master(self)
        return self

    def remove_component(self, component):
        if self.has_component(component):
            super().remove_component(component)
        if isinstance(component, MutableComponentElementType) \
        and component.master() is self:
            component.remove_master()
        return self


class LeafElementType(MutableComponentElementType):
    def set_master(self, master):
        is_component = isinstance(master, MasterElementType)
        is_mutable = isinstance(master, MutableMasterElementType)
        contains = master.has_component(self)
        if is_mutable or (is_component and contains):
            super().set_master(master)
        if is_mutable and not contains:
            master.add_component(self)
        return self

    def remove_master(self):
        master = self._master
        super().remove_master()
        if isinstance(master, MutableMasterElementType):
            master.remove_component(self)
        return self


class NodeElementType(RootElementType, LeafElementType):
    pass
