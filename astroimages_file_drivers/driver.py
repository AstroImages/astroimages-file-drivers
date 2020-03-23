from abc import ABC, abstractmethod


class GenericFileDriver(ABC):

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def list_from_folder(self, folder_name):
        pass

    @abstractmethod
    def get_file(self, file_name):
        pass
