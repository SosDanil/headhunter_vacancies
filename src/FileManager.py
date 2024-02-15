from abc import ABC, abstractmethod


class FileManager(ABC):
    @abstractmethod
    def write_to_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def delete_from_file(self):
        pass
