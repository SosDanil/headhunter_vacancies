from abc import ABC, abstractmethod


class BaseAPI(ABC):
    @abstractmethod
    def get_response(self):
        pass

