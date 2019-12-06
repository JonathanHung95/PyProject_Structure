import sys
import os
import unittest

sys.path.append("..")

from utils.get_root import get_root
from rename_file.rename_file import rename_file
from cleanup import cleanup

# set up

root_dir = get_root()
input_dir = root_dir + "\\Input"
output_dir = root_dir + "\\Output"

file = open(output_dir + "\\test_1_2_3", "w")
file.close()

# unit test

class TestRename_File(unittest.TestCase):

    def test_rename_file(self):
        """
        Unit test for file_rename().
        """

        rename_file("test_1_2_3", output_dir, "1", 1)
        
        self.assertEqual(os.listdir(output_dir),
                         ["test_1_1_2"],
                         "Should have the same file name.")

if __name__ == "__main__":
    unittest.main(exit = False)
    cleanup(input_dir, output_dir)
                         
