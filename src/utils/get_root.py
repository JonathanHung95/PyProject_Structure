from os.path import dirname, abspath

def get_root():
    """
    Get the root of the project.

    :return: Path to project root.
    """
    root_dir = dirname(dirname(dirname(abspath(__file__))))
        
    return root_dir

