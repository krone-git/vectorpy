from abc import ABC, abstractmethod


class ViewABC(ABC):
    @abstractmethod
    def camera(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_camera(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def output(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_output(*args, **kwargs): raise NotImplementedError
