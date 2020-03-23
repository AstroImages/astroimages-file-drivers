import unittest

import astroimages_file_drivers.driver as driver


class TestAbstractDrivers(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_NullFileDriver_list_from_folder(self):
        nullFileDriver = driver.NullFileDriver()
        self.assertEqual(len(nullFileDriver.list_from_folder('')), 0)

    def test_NullFileDriver_get_file(self):
        nullFileDriver = driver.NullFileDriver()
        self.assertEqual(len(nullFileDriver.get_file('')), 0)


if __name__ == '__main__':
    unittest.main()
