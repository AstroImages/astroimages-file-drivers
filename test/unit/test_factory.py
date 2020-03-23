import unittest
import astroimages_file_drivers.drivers.null_file_driver as null_file_driver
import astroimages_file_drivers.drivers.local_file_driver as local_file_driver
import astroimages_file_drivers.drivers.s3_file_driver as s3_file_driver
import astroimages_file_drivers.drivers.minio_file_driver as minio_file_driver

import astroimages_file_drivers.factory as factory
import astroimages_file_drivers.handler_enums as handler_enums


class TestFactoryMethod(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creation_NullFileHandler(self):
        driver = factory.get_file_driver(handler_enums.FILE_HANDLER_TYPE.NULL)

        self.assertEqual(driver.get_type(), handler_enums.FILE_HANDLER_TYPE.NULL)
        self.assertTrue(type(driver) is null_file_driver.NullFileDriver)

    def test_creation_LocalFileHandler(self):
        driver = factory.get_file_driver(handler_enums.FILE_HANDLER_TYPE.LOCAL)

        self.assertEqual(driver.get_type(), handler_enums.FILE_HANDLER_TYPE.LOCAL)
        self.assertTrue(type(driver) is local_file_driver.LocalFileDriver)

    def test_creation_S3FileHandler(self):
        driver = factory.get_file_driver(handler_enums.FILE_HANDLER_TYPE.S3)

        self.assertEqual(driver.get_type(), handler_enums.FILE_HANDLER_TYPE.S3)
        self.assertTrue(type(driver) is s3_file_driver.S3FileDriver)

    def test_creation_MinioFileHandler(self):
        driver = factory.get_file_driver(handler_enums.FILE_HANDLER_TYPE.MINIO)

        self.assertEqual(driver.get_type(), handler_enums.FILE_HANDLER_TYPE.MINIO)
        self.assertTrue(type(driver) is minio_file_driver.MinioFileDriver)


if __name__ == '__main__':
    unittest.main()
