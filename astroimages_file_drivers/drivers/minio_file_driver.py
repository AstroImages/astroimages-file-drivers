from astroimages_file_drivers import GenericFileDriver
from handler_enums import FILE_HANDLER_TYPE


class MinioFileDriver(GenericFileDriver):

    def get_type(self):
        return FILE_HANDLER_TYPE.MINIO

    def list_from_folder(self, folder_name):
        return []

    def get_file(self, file_name):
        return {}
