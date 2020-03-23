from abc import ABC, abstractmethod


class GenericFileDriver(ABC):

    @abstractmethod
    def list_from_folder(self, folder_name):
        pass

    @abstractmethod
    def get_file(self, file_name):
        pass


class NullFileDriver(GenericFileDriver):

    def list_from_folder(self, folder_name):
        return []

    def get_file(self, file_name):
        return {}
