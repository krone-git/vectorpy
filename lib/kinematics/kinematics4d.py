from .abc import MutableKinematicsABC
from ..vector.vector4d import Vector4D

__all__ = (
    "kin4d", "kinematics4d", "Kinematics4D"
)

class Kinematics4DSingleton(MutableKinematicsABC):
    def position_velocity(time, position, velocity):
        vec4d = Vector4D
        return vec4d.add_vector(
            position, vec4d.multiply_scalar(velocity, time)
            )

    def postition_velocity_sum(time, position, velocities):
        vec4d = Vector4D
        velocity = vec4d.sum_vectors(velocities)
        return vec4d.add_vector(
            position, vec4d.multiply_scalar(velocity, time)
            )

    def position_acceleration(time, position, velocity, acceleration):
        vec4d = Vector4D
        velocity = vec4d.multiply_scalar(velocity, time)
        acceleration = vec4d.multiply_scalar(acceleration, time**2 / 2)
        return vec4d.add_vector(
            position, vec4d.add_vector(velocity, acceleration)
            )

    def position_acceleration_sum(time, position, velocities, accelerations):
        vec4d = Vector4D
        velocity = vec4d.multiply_scalar(vec4d.sum_vectors(velocities), time)
        acceleration = vec4d.multiply_scalar(
            vec4d.sum_vectors(accelerations), time**2 / 2
            )
        return vec4d.add_vector(
            position, vec4d.add_vector(velocity, acceleration)
            )

    # def position_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # def position_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError

    def iposition_velocity(time, position, velocity):
        vec4d = Vector4D
        return vec4d.iadd_vector(
            position, vec4d.multiply_scalar(velocity, time)
            )

    def ipostition_velocity_sum(time, position, velocities):
        vec4d = Vector4D
        velocity = vec4d.sum_vectors(velocities)
        return vec4d.iadd_vector(
            position, vec4d.multiply_scalar(velocity, time)
            )

    def iposition_acceleration(time, position, velocity, acceleration):
        vec4d = Vector4D
        velocity = vec4d.multiply_scalar(velocity, time)
        acceleration = vec4d.multiply_scalar(acceleration, time**2 / 2)
        return vec4d.iadd_vector(
            position, vec4d.add_vector(velocity, acceleration)
            )

    def iposition_acceleration_sum(time, position, velocities, accelerations):
        vec4d = Vector4D
        velocity = vec4d.multiply_scalar(vec4d.sum_vectors(velocities), time)
        acceleration = vec4d.multiply_scalar(
            vec4d.sum_vectors(accelerations), time**2 / 2
            )
        return vec4d.iadd_vector(
            position, vec4d.add_vector(velocity, acceleration)
            )

    # def iposition_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # def iposition_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError

kin4d = kinematics4d = Kinematics4D = Kinematics4DSingleton()
