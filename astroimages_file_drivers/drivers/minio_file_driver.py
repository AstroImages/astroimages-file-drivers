from astroimages_file_drivers import GenericFileDriver


class MinioFileDriver(GenericFileDriver):

    def list_from_folder(self, folder_name):
        return []

    def get_file(self, file_name):
        return {}
