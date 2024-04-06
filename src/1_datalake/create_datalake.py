"""Create a datalake in the main directory"""

import os

# import pkg_resources

STRUCTURE_FILE = "src/1_datalake/datalake_strutcture.txt"


def get_datalake_dirs():
    """Returns the datalake directories stored in the file structure.txt"""

    with open(STRUCTURE_FILE, "r") as f:
        carpetas = f.readlines()

    dirs = [carpeta.strip() for carpeta in carpetas]

    return dirs


def create_datalake(dirs):
    """Creates datalake in the main directory.

    Args:
        dirs (list): List of directories to create

    Return:
        None

    """

    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path)
            os.chmod(path, 0o775)


def main():
    """Orchestrates the creation of the datalake"""

    dirs = get_datalake_dirs()
    create_datalake(dirs)


if __name__ == "__main__":
    main()
