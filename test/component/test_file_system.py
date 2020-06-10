import unittest
import os

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


class TestLocalFileSystem(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_happyFlow_LocalFileHandler(self):
        'HAPPY FLOW'
        folder_name = './test/data/'

        try:
            driver = local_file_driver.LocalFileDriver()
            # Retrieves the files in the folder
            files = driver.get_files(folder_name, '.fits')

            # Fetches the first element
            file = driver.get_physical_file(files[0])

            contents = bytearray(files[0], 'utf-8')

            array_files = [
                {'name': 'file1.abc', 'contents': contents},
                {'name': 'file2.abc', 'contents': contents},
            ]

            # If it does not raise an exception, it passed
            driver.store_files(folder_name, array_files)

            # Retrieves the newly created files
            secondary_files = driver.get_files(folder_name, '.abc')

            self.assertEqual(len(files), 1, "Should get EXACTLY ONE fits file")
            self.assertEqual(len(file), 699840, "Should be 699840 bytes")

            self.assertEqual(len(secondary_files), 2, "Should get EXACTLY TWO abc files")
            for sec_file in secondary_files:
                sec_file_phys = driver.get_physical_file(sec_file)
                self.assertEqual(len(sec_file_phys), len(contents), "%s should have %d bytes" % (sec_file, len(contents)))

        finally:
            for file in array_files:
                os.remove('{}/{}'.format(folder_name, file['name']))


if __name__ == '__main__':
    unittest.main()
