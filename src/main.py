import os

from file_split import file_split
from utils import get_root
from get_lines import get_lines
from rename_file import rename_file

# establish the necessary directories

root_dir = get_root()

input_dir = root_dir + "\Input"
output_dir = root_dir + "\Output"

os.chdir(root_dir)

# split the files

if __name__ == "__main__":
    counter = 1
    
    for f in os.listdir(input_dir):
        n = get_lines(f, input_dir)
        print(f, " has ", n, " lines.")
        
        print("Started splitting: " + f)
        n = (n + 2 // 2) // 2
        file_split(f, input_dir, output_dir, n)
        
        print("Finished splitting: " + f)
        
        print("Deleting: " + f)
        os.remove(input_dir + "\\" + f)
        
    for f in os.listdir(output_dir):
        print("Fixing output file name:" + f)
        rename_file(f, output_dir, str(counter), 1)
        counter += 1
        
    print("Finished job")
