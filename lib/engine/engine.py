from abc import ABC, abstractmethod


class EngineABC(ABC):
    def __init__(self, scene=None, views=None):
        self._scene = scene
        self._views = views if views else []


class Engine(EngineABC):
    pass
