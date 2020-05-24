from abc import ABC, abstractmethod


class GenericFileDriver(ABC):

    @abstractmethod
    def get_physical_file(self, file_name):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_files(self, folder_name, extension):
        pass

    def get_file(self, file_name):
        return self.get_physical_file(file_name)
