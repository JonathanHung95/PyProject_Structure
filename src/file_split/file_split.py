import os

def file_split(filename, input_dir, output_dir, n):
    """
    Split the text file into smaller chunks.

    :param filename: Name of the file.
    :param input_dir: Path to the input directory.
    :param output_dir: Path to the output directory.
    :param n: Number of lines per chunk.

    :return: None.
    """

    smallfile = None
    name = os.path.splitext(filename)[0]

    with open(input_dir + "\\" + filename) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % n == 0:
                if smallfile:
                    smallfile.close()
                    
                small_filename = "{}_{}.txt".format(name, lineno + n)
                smallfile = open(output_dir + "\\" + small_filename, "w")
                
            smallfile.write(line)
            
        if smallfile:
            smallfile.close()
