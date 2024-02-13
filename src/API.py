from abc import ABC, abstractmethod


class BaseAPI(ABC):
    @abstractmethod
    def get_response(self):
        pass


class HeadHunterAPI(BaseAPI):
    def __init__(self):
        pass

    def get_response(self):
        pass

