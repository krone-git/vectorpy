from .abc impoer GraphSingletonABC


class DegreeGraphSingleton(GraphSingletonABC):
    @staticmethod
    def remove_degree(graph, degree):
        raise NotImplementedError
    @staticmethod
    def remove_degree_range(graph, start, stop, step):
        raise NotImplementedError
    @classmethod
    def remove_degree_below(cls, graph, degree):
        return cls
    @classmethod
    def remove_isolated(cls, graph):
        return cls
    @classmethod
    def remove_pendant(cls, graph):
        return cls.remove_degree()
