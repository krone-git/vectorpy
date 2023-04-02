from .abc import PlaneSingletonABC


__all__ = (
    "plane", "planend", "Plane", "PlaneND"
    )

class PlaneNDSingleton():
    pass

plane = planend = Plane = PlaneND = PlaneNDSingleton()
