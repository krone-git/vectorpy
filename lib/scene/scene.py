from ..element.abc import ElementTypeABC, MutableMasterElementType


class SceneABC(ElementTypeABC, MutableMasterElementType):
    def __init__(self, origin, basis, components):
        ElementTypeABC.__init__(self, origin, basis)
        MutableMasterElementType.__init__(self, components)

    def refresh(self):
        [component.refresh() for component in self._components]
        return self
