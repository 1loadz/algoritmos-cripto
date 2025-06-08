from abc import ABC, abstractmethod


class classproperty(property):
    def __get__(self, obj, cls):
        return self.fget(cls)


class BaseAlgorithm(ABC):

    @classproperty
    @abstractmethod
    def input_format(cls):
        """Return a latex string describing the expected input format."""
        pass

    @staticmethod
    @abstractmethod
    def validate_input(input_value):
        """Validate the input. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def solve(self):
        """Run the algorithm solving logic. Must be implemented by subclasses."""
        pass
