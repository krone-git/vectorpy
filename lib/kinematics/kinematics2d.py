from .abc import MutableKinematicsABC
from ..vector.vector2d import Vector2D


__all__ = (
    "kin2d", "kinematics2d", "Kinematics2D"
)

class Kinematics2DSingleton(MutableKinematicsABC):
    def position_velocity(time, position, velocity):
        vec2d = Vector2D
        return vec2d.add_vector(
            position, vec2d.multiply_scalar(velocity, time)
            )

    def postition_velocity_sum(time, position, velocities):
        vec2d = Vector2D
        velocity = vec2d.sum_vectors(velocities)
        return vec2d.add_vector(
            position, vec2d.multiply_scalar(velocity, time)
            )

    def position_acceleration(time, position, velocity, acceleration):
        vec2d = Vector2D
        velocity = vec2d.multiply_scalar(velocity, time)
        acceleration = vec2d.multiply_scalar(acceleration, time**2 / 2)
        return vec2d.add_vector(
            position, vec2d.add_vector(velocity, acceleration)
            )

    def position_acceleration_sum(time, position, velocities, accelerations):
        vec2d = Vector2D
        velocity = vec2d.multiply_scalar(vec2d.sum_vectors(velocities), time)
        acceleration = vec2d.multiply_scalar(
            vec2d.sum_vectors(accelerations), time**2 / 2
            )
        return vec2d.add_vector(
            position, vec2d.add_vector(velocity, acceleration)
            )

    # def position_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # def position_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError

    def iposition_velocity(time, position, velocity):
        vec2d = Vector2D
        return vec2d.iadd_vector(
            position, vec2d.multiply_scalar(velocity, time)
            )

    def ipostition_velocity_sum(time, position, velocities):
        vec2d = Vector2D
        velocity = vec2d.sum_vectors(velocities)
        return vec2d.iadd_vector(
            position, vec2d.multiply_scalar(velocity, time)
            )

    def iposition_acceleration(time, position, velocity, acceleration):
        vec2d = Vector2D
        velocity = vec2d.multiply_scalar(velocity, time)
        acceleration = vec2d.multiply_scalar(acceleration, time**2 / 2)
        return vec2d.iadd_vector(
            position, vec2d.add_vector(velocity, acceleration)
            )

    def iposition_acceleration_sum(time, position, velocities, accelerations):
        vec2d = Vector2D
        velocity = vec2d.multiply_scalar(vec2d.sum_vectors(velocities), time)
        acceleration = vec2d.multiply_scalar(
            vec2d.sum_vectors(accelerations), time**2 / 2
            )
        return vec2d.iadd_vector(
            position, vec2d.add_vector(velocity, acceleration)
            )

    # def iposition_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # def iposition_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError


kin2d = kinematics2d = Kinematics2D = Kinematics2DSingleton()
