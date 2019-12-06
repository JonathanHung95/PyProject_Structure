import os

def cleanup(input_dir, output_dir):
    """
    Function to cleanup the input and output directories after unittests are
    run.

    :param input_dir: Path to the Input directory.
    :param output_dir: Path to the Output directory.

    :return: None.
    """

    for f in os.listdir(input_dir):
        os.remove(input_dir + "\\" + f)

    for f in os.listdir(output_dir):
        os.remove(output_dir + "\\" + f)
