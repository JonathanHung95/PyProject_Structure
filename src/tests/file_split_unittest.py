import sys
import os
from shutil import copyfile
import unittest
from cleanup import cleanup

sys.path.append("..")

from file_split.file_split import file_split
from utils.get_root import get_root

# set up

root_dir = get_root()
input_dir = root_dir + "\\Input"
output_dir = root_dir + "\\Output"
test_dir = root_dir + "\\src\\tests"

copyfile(test_dir + "\\test_20191206_1140000.txt",
         input_dir + "\\test_20191206_1140000.txt")

# unit test

class TestFile_Split(unittest.TestCase):

    def test_file_split(self):
        """
        Unit test for file_split().
        """

        file_split("test_20191206_1140000.txt", input_dir, output_dir, 150)

        self.assertEqual(os.listdir(output_dir),
                         ["test_20191206_1140000_150.txt",
                          "test_20191206_1140000_300.txt"],
                         "Should have the same files.")

if __name__ == "__main__":
    unittest.main(exit = False)
    cleanup(input_dir, output_dir)
                         
