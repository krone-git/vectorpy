from abc import ABC, abstractmethod


class KinematicsABC(ABC):
    __slots__ = ()

    @classmethod
    def position(cls, time, position, vectors):
        vector_count = len(vectors)
        if vector_count >= 3:
            return cls.position_jerk(time, position, *vectors)
        elif vector_count == 2:
            return cls.position_acceleration(time, position, *vectors)
        elif vector_count <= 1:
            return cls.position_velocity(time, position, *vectors)

    @classmethod
    def position_sum(cls, time, position, vectors):
        vector_count = len(vectors)
        if vector_count >= 3:
            return cls.position_jerk_sum(time, position, *vectors)
        elif vector_count == 2:
            return cls.position_acceleration_sum(time, position, *vectors)
        elif vector_count <= 1:
            return cls.position_velocity_sum(time, position, *vectors)

    @abstractmethod
    def position_velocity(time, position, velocity): raise NotImplementedError
    @abstractmethod
    def postition_velocity_sum(time, position, velocities):
        raise NotImplementedError
    @abstractmethod
    def position_acceleration(time, position, velocity, acceleration):
        raise NotImplementedError
    @abstractmethod
    def position_acceleration_sum(time, position, velocities, accelerations):
        raise NotImplementedError
    # @abstractmethod
    # def position_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # @abstractmethod
    # def position_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError


class MutableKinematicsABC(KinematicsABC):
    @classmethod
    def iposition(cls, time, position, vectors):
        vector_count = len(vectors)
        if vector_count >= 3:
            return cls.iposition_jerk(time, position, *vectors)
        elif vector_count == 2:
            return cls.iposition_acceleration(time, position, *vectors)
        elif vector_count <= 1:
            return cls.iposition_velocity(time, position, *vectors)

    @classmethod
    def iposition_sum(cls, time, position, vectors):
        vector_count = len(vectors)
        if vector_count >= 3:
            return cls.iposition_jerk_sum(time, position, *vectors)
        elif vector_count == 2:
            return cls.iposition_acceleration_sum(time, position, *vectors)
        elif vector_count <= 1:
            return cls.iposition_velocity_sum(time, position, *vectors)

    @abstractmethod
    def iposition_velocity(time, position, velocity): raise NotImplementedError
    @abstractmethod
    def ipostition_velocity_sum(time, position, velocities):
        raise NotImplementedError
    @abstractmethod
    def iposition_acceleration(time, position, velocity, acceleration):
        raise NotImplementedError
    @abstractmethod
    def iposition_acceleration_sum(time, position, velocities, accelerations):
        raise NotImplementedError
    # @abstractmethod
    # def iposition_jerk(time, position, velocity, acceleration, jerk):
    #     raise NotImplementedError
    # @abstractmethod
    # def iposition_jerk_sum(time, position, velocities, accelerations, jerks):
    #     raise NotImplementedError
