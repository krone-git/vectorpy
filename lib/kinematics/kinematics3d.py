from .abc import MutableKinematicsABC
from ..vector.vector3d import Vector3D


__all__ = (
    "kin3d", "kinematics3d", "Kinematics3D"
)

class Kinematics3DSingleton(MutableKinematicsABC):
    def position_velocity(time, position, velocity):
        vec3d = Vector3D
        return vec3d.add_vector(
            position, vec3d.multiply_scalar(velocity, time)
            )

    def postition_velocity_sum(time, position, velocities):
        vec3d = Vector3D
        velocity = vec3d.sum_vectors(velocities)
        return vec3d.add_vector(
            position, vec3d.multiply_scalar(velocity, time)
            )

    def position_acceleration(time, position, velocity, acceleration):
        vec3d = Vector3D
        velocity = vec3d.multiply_scalar(velocity, time)
        acceleration = vec3d.multiply_scalar(acceleration, time**2 / 2)
        return vec3d.add_vector(
            position, vec3d.add_vector(velocity, acceleration)
            )

    def position_acceleration_sum(time, position, velocities, accelerations):
        vec3d = Vector3D
        velocity = vec3d.multiply_scalar(vec3d.sum_vectors(velocities), time)
        acceleration = vec3d.multiply_scalar(
            vec3d.sum_vectors(accelerations), time**2 / 2
            )
        return vec3d.add_vector(
            position, vec3d.add_vector(velocity, acceleration)
            )

    # def position_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # def position_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError

    def iposition_velocity(time, position, velocity):
        vec3d = Vector3D
        return vec3d.iadd_vector(
            position, vec3d.multiply_scalar(velocity, time)
            )

    def ipostition_velocity_sum(time, position, velocities):
        vec3d = Vector3D
        velocity = vec3d.sum_vectors(velocities)
        return vec3d.iadd_vector(
            position, vec3d.multiply_scalar(velocity, time)
            )

    def iposition_acceleration(time, position, velocity, acceleration):
        vec3d = Vector3D
        velocity = vec3d.multiply_scalar(velocity, time)
        acceleration = vec3d.multiply_scalar(acceleration, time**2 / 2)
        return vec3d.iadd_vector(
            position, vec3d.add_vector(velocity, acceleration)
            )

    def iposition_acceleration_sum(time, position, velocities, accelerations):
        vec3d = Vector3D
        velocity = vec3d.multiply_scalar(vec3d.sum_vectors(velocities), time)
        acceleration = vec3d.multiply_scalar(
            vec3d.sum_vectors(accelerations), time**2 / 2
            )
        return vec3d.iadd_vector(
            position, vec3d.add_vector(velocity, acceleration)
            )

    # def iposition_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # def iposition_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError

kin3d = kinematics3d = Kinematics3D = Kinematics3DSingleton()
