from .abc import MutableKinematicsABC


__all__ = (
    "kin", "kinematics", "Kinematics"
    )

class KinematicsNDSingleton(): #MutableKinematicsABC
    pass

kin = kinematics = Kinematics = KinematicsNDSingleton()
