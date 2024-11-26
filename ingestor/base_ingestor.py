from abc import ABC, abstractmethod

class BaseIngestor(ABC):
    """
    Abstract base class for data sources.
    """
    @abstractmethod
    def read_messages(self):
        pass
