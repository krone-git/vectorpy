from .abc import AdjacencyGraphSingletonABC


__all__ = (
    "adj_graph", "adjacency", "adjacency_graph", "AdjacencyGraph"
    )

class AdjacencyGraphSingleton(AdjacencyGraphSingletonABC):
    pass

adj_graph = adjacency = adjacency_graph = AdjacencyGraph = AdjacencyGraphSingleton()
