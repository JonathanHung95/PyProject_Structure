import os

def rename_file(filename, output_dir, to_add, location):
    """
    Function to rename files to the required style.

    :param filename: Name of the file.
    :param output_dir: Output directory path.
    :param to_add: Part to add to the filename.
    :param location: Index where to_add is to be inserted.

    :return: None.
    """

    lst = filename.split("_")
    lst.insert(location, to_add)
    lst.pop(-1)

    new_name = "_".join(lst)

    os.rename(output_dir + "\\" + filename,
              output_dir + "\\" + new_name + ".txt")
    

    
