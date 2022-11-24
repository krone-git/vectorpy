from .abc import BaseFaceSingletonABC


__all__ = ("face", "Face")

class FaceSingleton(BaseFaceSingletonABC):
    pass

face = Face = FaceSingleton()
