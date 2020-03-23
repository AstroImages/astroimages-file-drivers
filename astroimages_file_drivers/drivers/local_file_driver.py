from astroimages_file_drivers import GenericFileDriver
from handler_enums import FILE_HANDLER_TYPE


class LocalFileDriver(GenericFileDriver):

    def get_type(self):
        return FILE_HANDLER_TYPE.LOCAL

    def list_from_folder(self, folder_name):
        return []

    def get_file(self, file_name):
        return {}
