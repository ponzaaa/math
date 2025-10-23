from abc import ABC, abstractmethod

class Function(ABC):
    @abstractmethod
    def evaluate(self, x):
        pass

    @abstractmethod
    def differentiate(self):
        pass

    @abstractmethod
    def integrate(self):
        pass
