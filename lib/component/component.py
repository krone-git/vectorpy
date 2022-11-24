from ..element.abc import BaseElementABC, NodeElementType, LeafeElementType


__all__ = ("Component",)

class Component(BaseElementABC, NodeElementType):
    __slots__ = ()

    def __init__(cls, origin, basis, bodies, components):
        BaseElementABC.__init__(self, origin, basis)
        NodeElementType.__init__(self, components)
        self._bodies = bodies
        return component

    def bodies(self): return self._bodies

    def refresh(self):
        [body.refresh() for boby in self._bodies]
        [component.refresh() for component in self._components]
        return component

    def add_body(self, body):
        is_component = isinstance(body, ComponentElementType)
        is_mutable = isinstance(body, MutableComponentElementType)
        master = body.master()
        if  is_mutable or (is_component and master is self):
            self._bodies.append(body)
        if is_mutable and master is not self:
            body.set_master(self)
        return self

    def remove_body(self, body):
        if self.has_body(body):
            self._bodies.remove(body)
        if isinstance(body, MutableComponentElementType) \
        and body.master() is self:
            body.remove_master()
        return self
