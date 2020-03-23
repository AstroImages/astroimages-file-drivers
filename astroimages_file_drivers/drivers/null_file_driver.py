from astroimages_file_drivers.driver import GenericFileDriver
# from astroimages_file_drivers.handler_enums import FILE_HANDLER_TYPE
import astroimages_file_drivers.handler_enums as handler_enums


class NullFileDriver(GenericFileDriver):

    def get_type(self):
        return handler_enums.FILE_HANDLER_TYPE.NULL

    def get_files(self, folder_name):
        return ['NullFileDriver']

    def get_file(self, file_name):
        return {
            'NullFileDriver': NullFileDriver
        }
