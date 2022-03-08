from .abc import KinematicsABC


__all__ = (
    "kin1d", "kinematics1d", "Kineamtics1D"
)

class Kinematics1DSingleton(KinematicsABC):
    def position_velocity(time, position, velocity):
        return position + velocity * time
    def postition_velocity_sum(time, position, velocities):
        return position + sum(velocities) * time
    def position_acceleration(time, position, velocity, acceleration):
        return position + velocity * time + (acceleration * time**2) / 2
    def position_acceleration_sum(time, position, velocities, accelerations):
        return position + sum(velocities) * time + (sum(accelerations) * time**2) / 2
    # def position_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # def position_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError

kin1d = kinematics1d = Kinematics1D = Kinematics1DSingleton()
