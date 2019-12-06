import os

def get_lines(file_name, input_dir):
    """
    Find out the number of lines in the txt file.

    :param file_name: Name of the file.
    :param input_dir: Path to the input directory.

    :return: Number of lines in the file.
    """

    with open(input_dir + "\\" + file_name) as f:
        for i, l in enumerate(f):
             pass

    return i + 1
