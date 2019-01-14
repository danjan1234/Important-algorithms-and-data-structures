from base_file import BaseFile
from file import File
from collections import deque


class Directory(BaseFile):
    """A file class"""
    def __init__(self, name, created_time=None, size=None):
        super().__init__(name, created_time, size)
        self._children = {}

    def add_file(self, file_name):
        self._children[file_name] = File(file_name)

    def rm(self, file_name):
        if file_name not in self._children:
            print("File not found: {}".format(file_name))
            return
        self._children.pop(file_name)

    def mk_dir(self, dir_name):
        self._children[dir_name] = Directory(dir_name)

    def list_files(self):
        return [file.print() for file in self._children]

    def list_files_recursive(self):
        q = deque()
        q.append(self)
        res = []    # [[directory: file names in that directory]]
        while len(q) > 0:
            curr = q.popleft()
            res.append([curr.print(), []])
            for file_name, file in curr._children.items():
                if hasattr(file, '_children'):
                    q.append(file)
                res[-1][1].append(file.print())
        return res
