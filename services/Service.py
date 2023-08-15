from abc import ABC, abstractmethod
from services.ServiceInterface import ServiceInterface


class Service(ServiceInterface, ABC):
    def __init__(self):
        self.endpoint = "/services"
        self.data = None

    def set_endpoint(self, endpoint):
        self.endpoint = self.endpoint + endpoint

    def set_data(self, data):
        self.data = data

    def get_endpoint(self):
        return self.endpoint

    def get_data(self):
        return self.data()