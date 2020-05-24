import unittest

import tempfile
from astroimages_file_drivers.util.local_file_system import list_files_in_folder, read_full_file_in_bytes


class TestUtilFunctions(unittest.TestCase):

    def setUp(self):
        self.folders_per_layer = 3
        self.files_per_folder = 10

    def test_list_files_in_temporary_folder(self):
        "Testing listing files in temporary folder - Happy path."
        folder = tempfile.mkdtemp()

        for i in range(0, self.files_per_folder):
            file = open("{}/SAMPLE_{}.fits".format(folder, i), "w")
            file.write("SAMPLE DATA @ {}/SAMPLE_{}.fits".format(folder, i))
            file.close()

        files_in_folder = list_files_in_folder(folder, '.fits')

        self.assertEqual(len(files_in_folder), self.files_per_folder, "Should be %s" % self.files_per_folder)

    def test_list_files_in_folder_and_subfolders(self):
        "Testing listing files in folder and subfolders - Happy path."

        folder = tempfile.mkdtemp()

        for i in range(0, self.folders_per_layer):
            inner_folder = tempfile.mkdtemp(dir=folder)
            for k in range(0, self.files_per_folder):
                file = open("{}/SAMPLE_{}.fits".format(inner_folder, k), "w")
                file.write("SAMPLE DATA @ {}/SAMPLE_{}.fits".format(inner_folder, k))
                file.close()

        files_in_folder = list_files_in_folder(folder, '.fits')

        self.assertEqual(len(files_in_folder),
                         self.folders_per_layer * self.files_per_folder,
                         "Should be %s" % (self.folders_per_layer * self.files_per_folder))

    def test_read_full_file_in_bytes(self):
        "=============================================="

        file = read_full_file_in_bytes('./test/data/WFPC2u5780205r_c0fx.fits')
        print(file)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
