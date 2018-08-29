import os


class File(object):
    """
    File utility class.
    """

    def get_path(self, path) -> str:
        return os.path.abspath(path)

    def root_path(self) -> str:
        return os.getcwd()
