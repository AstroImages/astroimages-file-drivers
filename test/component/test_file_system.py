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

temp_file_contents = "SIMPLE  =                    T / file does conform to FITS standard"


def mock_list_files_in_folder(folder, extension):
    return temp_files


def mock_store_file(path, file, overwrite=False):
    pass


def mock_read_full_file_in_bytes(path):
    return bytearray(temp_file_contents, 'utf-8')


class TestLocalFileSystem(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch('astroimages_file_drivers.drivers.local_file_driver.list_files_in_folder',
                side_effect=mock_list_files_in_folder)
    @mock.patch('astroimages_file_drivers.drivers.local_file_driver.read_full_file_in_bytes',
                side_effect=mock_read_full_file_in_bytes)
    @mock.patch('astroimages_file_drivers.drivers.local_file_driver.store_file',
                side_effect=mock_store_file)
    def test_happyFlow_LocalFileHandler(self, mock_list_files_in_folder, mock_read_full_file_in_bytes, mock_store_file):
        '>>>>>>>>> HAPPY FLOW'
        driver = local_file_driver.LocalFileDriver()
        # Retrieves the files in the folder
        files = driver.get_files('folder_name', '.fits')

        # Fetches the first element
        file = driver.get_physical_file(files[0])

        print('\nFILE: %s' % files[0])
        print('FILE CONTENTS: \'%s\'' % str(file))
        print('FILE LEN: %d' % len(file))

        array_files = [
            {'name': 'file1.txt', 'contents': 'CONTENTS FILE1'},
            {'name': 'file2.txt', 'contents': 'CONTENTS FILE2'},
        ]

        # If it does not raise an exception, it passed
        driver.store_files('local_folder', array_files)

        self.assertEqual(len(files), len(temp_files), "Should be %s" % len(temp_files))
        self.assertEqual(len(file), len(temp_file_contents), "Should be %s" % len(temp_files))


if __name__ == '__main__':
    unittest.main()
