from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    @abstractmethod
    def get_endpoint(self):
        pass

    @abstractmethod
    def get_data(self):
        pass
