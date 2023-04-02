from abc import ABC, abstractmethod


class GraphFactoryType(ABC):
    @abstractmethod
    def new(*args): raise NotImplementedError
    @classmethod
    def __call__(cls, *args, **kwargs): return cls.new(*args, **kwargs)

    @staticmethod
    def copy(graph): return graph.copy()


class GraphAccessibleType(ABC):
    @abstractmethod
    def edges(graph): raise NotImplementedError


class GraphPropertiesType(ABC):
    @abstractmethod
    def degree(graph, node): raise NotImplementedError

    @abstractmethod
    def is_connected_forward(graph, node, other): raise NotImplementedError
    @abstractmethod
    def is_connected_backward(graph, node, other): raise NotImplementedError
    @classmethod
    def is_connected_bidirectional(cls, *args):
        return cls.is_connected_forward(*args) and cls.is_connected_backward(*args)
    @classmethod
    def is_connected_unidirectional(cls, *args):
        forward = cls.is_connected_forward(*args)
        backward = cls.is_connected_backward(*args)
        return (forward and not backward) or (backward and not forward)
    @classmethod
    def is_connected(cls, *args):
        return cls.is_connected_forward(*args) or cls.is_connected_backward(*args)

    @abstractmethod
    def is_isomorphic(graph, other): raise NotImplementedError


class GraphMutableType(ABC):
    @abstractmethod
    def clear(graph): raise NotImplementedError

    @abstractmethod
    def reset(graph): raise NotImplementedError

    @abstractmethod
    def set_graph(graph, other): raise NotImplementedError

    @abstractmethod
    def connect_directed_weighted(graph, node, other, weight):
        raise NotImplementedError
    @classmethod
    def connect_directed_unweighted(cls, *args, **kwargs):
        return cls.connect_directed_weighted(*args, 1, **kwargs)
    @classmethod
    def connect_directed(cls, *args, **kwargs):
        return cls.connect_directed_unweighted(*args, **kwargs)

    @abstractmethod
    def connect_undirected_weighted(graph, node, other, weight):
        raise NotImplementedError
    @classmethod
    def connect_undirected_unweighted(cls, *args, **kwargs):
        return cls.connect_undirected_weighted(*args, 1, **kwargs)
    @classmethod
    def connect_undirected(cls, *args, **kwargs):
        return cls.connect_undirected_unweighted(*args, **kwargs)

    @classmethod
    def connect(cls, *args, **kwargs):
        return cls.connect_undirected_unweighted(*args, **kwargs)

    @abstractmethod
    def disconnect(graph, node, other): raise NotImplementedError


class GraphOperationType(ABC):
    pass


class GraphSingletonABC(GraphFactoryType,
                            GraphPropertiesType,
                            GraphAccessibleType,
                            GraphMutableType,
                            GraphOperationType):
    __slots__ = ()

class AdjacencyGraphSingletonABC(GraphSingletonABC):
    pass

class IncidenceGraphSingletonABC(GraphSingletonABC):
    pass
