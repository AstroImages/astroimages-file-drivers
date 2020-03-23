import astroimages_file_drivers.drivers as drivers
from handler_enums import FILE_HANDLER_TYPE


_handlers = {
        FILE_HANDLER_TYPE.NULL: drivers.null_file_driver.NullFileDriver,
        FILE_HANDLER_TYPE.LOCAL: drivers.local_file_driver.LocalFileDriver,
        FILE_HANDLER_TYPE.S3: drivers.s3_file_driver.S3FileDriver,
        FILE_HANDLER_TYPE.MINIO: drivers.minio_file_driver.MinioFileDriver
    }


def get_file_driver(handler_type):
    return _handlers[handler_type]
