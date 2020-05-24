import unittest

from unittest import mock

import astroimages_file_drivers.drivers.local_file_driver as local_file_driver
import astroimages_file_drivers.factory as factory
import astroimages_file_drivers.handler_enums as handler_enums

temp_files = [
        '/tmp/tmpjor7_dvt/SAMPLE_9.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_8.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_7.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_6.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_5.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_4.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_3.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_2.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_1.fits',
        '/tmp/tmpjor7_dvt/SAMPLE_0.fits'
        ]


def mock_list_files_in_folder(folder, extension):
    return temp_files


def mock_read_full_file_in_bytes(path):
    return ['a', 'a', 'a', 'a']


class TestLocalFileHandler(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_type(self):
        driver = factory.get_file_driver(handler_enums.FILE_HANDLER_TYPE.LOCAL)

        self.assertEqual(driver.get_type(), handler_enums.FILE_HANDLER_TYPE.LOCAL)
        self.assertTrue(type(driver) is local_file_driver.LocalFileDriver)

    @mock.patch('astroimages_file_drivers.drivers.local_file_driver.list_files_in_folder',
                side_effect=mock_list_files_in_folder)
    def test_get_files(self, mock_list_files_in_folder):
        driver = local_file_driver.LocalFileDriver()

        files = driver.get_files('folder_name', '.fits')

        self.assertEqual(len(files), len(temp_files), "Should be %s" % len(temp_files))

    @mock.patch('astroimages_file_drivers.drivers.local_file_driver.read_full_file_in_bytes',
                side_effect=mock_read_full_file_in_bytes)
    def test_get_physical_file(self, mock_read_full_file_in_bytes):
        '>>>>>>>> test_get_physical_file <<<<<<<<'
        driver = local_file_driver.LocalFileDriver()

        file = driver.get_physical_file('../data/WFPC2u5780205r_c0fx.fits')
        print(file)

        self.assertNotEqual(file, None, 'Should not be None')


if __name__ == '__main__':
    unittest.main()
