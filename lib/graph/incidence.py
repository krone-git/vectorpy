from .abc import IncidenceGraphSingletonABC


__all__ = (
    "inc_graph", "incidence", "incidence_graph", "IncidenceGraph"
    )

class IncidenceGraphSingleton(IncidenceGraphSingletonABC):
    pass

inc_graph = incidence = incidence_graph = IncidenceGraph = IncidenceGraphSingleton()
