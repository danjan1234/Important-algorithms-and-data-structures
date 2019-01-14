from base_file import BaseFile


class File(BaseFile):
    """A file class"""
    def __init__(self, name, created_time=None, size=None):
        super().__init__(name, created_time, size)
