import unittest

from unittest import mock
import astroimages_file_drivers.drivers.local_file_driver as local_file_driver


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
    str = "SIMPLE  =                    T / file does conform to FITS standard"
    return bytearray(str, 'utf-8')


class TestLocalFileSystem(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch('astroimages_file_drivers.drivers.local_file_driver.list_files_in_folder',
                side_effect=mock_list_files_in_folder)
    @mock.patch('astroimages_file_drivers.drivers.local_file_driver.read_full_file_in_bytes',
                side_effect=mock_read_full_file_in_bytes)
    def test_happyFlow_LocalFileHandler(self, mock_list_files_in_folder, mock_read_full_file_in_bytes):
        '>>>>>>>>> HAPPY FLOW'
        driver = local_file_driver.LocalFileDriver()
        # Retrieves the files in the folder
        files = driver.get_files('folder_name', '.fits')

        # Fetches the first element
        file = driver.get_physical_file(files[0])

        print('FILE: %s' % files[0])
        print(file)

        self.assertEqual(len(files), len(temp_files), "Should be %s" % len(temp_files))


if __name__ == '__main__':
    unittest.main()
