from astroimages_file_drivers.driver import GenericFileDriver
from astroimages_file_drivers.handler_enums import FILE_HANDLER_TYPE


class MinioFileDriver(GenericFileDriver):

    def get_type(self):
        return FILE_HANDLER_TYPE.MINIO

    def get_files(self, folder_name):
        return []

    def get_file(self, file_name):
        return {}
