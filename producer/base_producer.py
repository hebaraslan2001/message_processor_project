from abc import ABC, abstractmethod

class BaseProducer(ABC):
    """
    Abstract base class for data sinks.
    """
    @abstractmethod
    def save_to_database(self, message, processed_value):
        pass
